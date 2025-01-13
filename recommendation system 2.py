# Import required packages
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
file_path = 'combined_learning_materials.csv'
data = pd.read_csv(file_path)

# Preprocess the data: Combine Title and Description into a single feature
data['Combined_Features'] = data['Title'].fillna('') + ' ' + data['Description'].fillna('')

# Create a TfidfVectorizer object to transform the combined features into a Tf-idf representation
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['Combined_Features'])

# Calculate the cosine similarity matrix between all learning materials
cosine_sim = cosine_similarity(tfidf_matrix)

# Ask the user for a title and description they are interested in
user_title = input('Enter a title you are interested in: ')
user_description = input('Enter a description of the material you are looking for: ')

# Combine the user input into a single string
user_input = user_title + ' ' + user_description

# Transform the user input into a Tf-idf vector
user_tfidf = tfidf.transform([user_input])

# Calculate the cosine similarity between the user input and all learning materials
user_similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)

# Create a Pandas Series to map the similarity scores to the titles
user_similarity_series = pd.Series(user_similarity_scores[0], index=data['Title'])

# Deduplicate by keeping only the first occurrence of each unique title
deduplicated_series = user_similarity_series[~user_similarity_series.index.duplicated(keep='first')]

# Get the top 3 most similar learning materials to the user input
top_3 = deduplicated_series.sort_values(ascending=False).head(3)

# Print the top 3 most similar learning materials
print(f'\nTop 3 learning materials similar to your input:')
for i, (title, score) in enumerate(top_3.items(), start=1):
    # Fetch the corresponding row from the dataset
    row = data.loc[data['Title'] == title].iloc[0]
    description = row['Description']
    url = row['URL'] if not pd.isna(row['URL']) else "No link available"
    subject = row['Subject'] if not pd.isna(row['Subject']) else "No subject area provided"
    author = row['Author'] if not pd.isna(row['Author']) else "No author"
    print(f'{i}. {title} (Similarity Score: {score:.2f})\n   Author: {author}\n   Subject Area: {subject}\n   Description: {description}\n   Link: {url}\n')
