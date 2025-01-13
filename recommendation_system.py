import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from google_nlp_api import note_analyser


filePath = 'combined_learning_materials.csv'
data = pd.read_csv(filePath)

data['Combined_Features'] = data['Title'].fillna('') + '' + data['Description'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['Combined_Features'])

cosineSimilarity = cosine_similarity(tfidf_matrix)

def recommend_learning_materials(title, content):
    keywordsTitle = note_analyser(title)
    keywordsContent = note_analyser(content)
    keywordsCombined = ' '.join(keywordsTitle + keywordsContent)

    print(keywordsCombined)

    user_tfidf = tfidf.transform([keywordsCombined])

    userSimilarityScores = cosine_similarity(user_tfidf, tfidf_matrix)

    userSimilaritySeries = pd.Series(userSimilarityScores[0], index=data['Title'])

    noDuplicatedSeries = userSimilaritySeries[userSimilaritySeries.index.duplicated(keep='first') == False]

    top3 = noDuplicatedSeries.sort_values(ascending=False).head(3)

    recommendations = []
    for title, score in top3.items():
        row = data.loc[data['Title'] == title].iloc[0]
        resourceType = 'Book' if pd.isna(row['URL']) else 'Link'
        recommendations.append({
            'title': title,
            'description': row['Description'] if not pd.isna(row['Description']) else "No description available",
            'url': row['URL'] if not pd.isna(row['URL']) else "No link available",
            'subject': row['Subject'] if not pd.isna(row['Subject']) else "No subject area provided",
            'author': row['Author'] if not pd.isna(row['Author']) else "No author",
            'similarity': score,
            'type': resourceType
        })
    
    return recommendations


