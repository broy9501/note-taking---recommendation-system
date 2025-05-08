import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from google_nlp_api import note_analyser  # Custom module for keyword extraction

# Load the dataset containing learning materials
filePath = 'combined_learning_materials.csv'
data = pd.read_csv(filePath)

# Combine ‘Title’ and ‘Description’ into a single feature for text analysis
data['Combined_Features'] = data['Title'].fillna('') + '' + data['Description'].fillna('')

# Initialise TF-IDF Vectorization to convert text into numerical vectors while removing English stop words
tfidf = TfidfVectorizer(stop_words='english')

# Transform the combined features into a TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(data['Combined_Features'])

# Compute the cosine similarity matrix for all learning materials
cosineSimilarity = cosine_similarity(tfidf_matrix)

def recommend_learning_materials(title, content):
    keywordsTitle = note_analyser(title)       # Extract keywords from the note title
    keywordsContent = note_analyser(content)   # Extract keywords from the note content
    
    # Combine keywords from title and content of the note
    keywordsCombined = ' '.join(keywordsTitle + keywordsContent)

    # Transform user input keywords into a TF-IDF vector
    user_tfidf = tfidf.transform([keywordsCombined])

    # Compute cosine similarity between user input and learning materials
    userSimilarityScores = cosine_similarity(user_tfidf, tfidf_matrix)

    # Convert similarity scores into a Pandas Series indexed by material titles
    userSimilaritySeries = pd.Series(userSimilarityScores[0], index=data['Title'])

    # Remove duplicated material titles, keeping the first occurrence
    noDuplicatedSeries = userSimilaritySeries[userSimilaritySeries.index.duplicated(keep='first') == False]

    # Select top 3 most relevant learning materials
    top3 = noDuplicatedSeries.sort_values(ascending=False).head(3)

    # Create recommendation list with details
    recommendations = []
    for title, score in top3.items():
        # Retrieve the first matching row
        row = data.loc[data['Title'] == title].iloc[0]

        # Determine if the material is a book or an online resource (with URL)
        resourceType = 'Book' if pd.isna(row['URL']) else 'Link'
        
        # Create a dictionary with material details and add it to the recommendation list
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
