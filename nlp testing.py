from google.cloud import language_v1
import os

keyPath = "D:/note taking - recommendation system - dissertation/argon-retina-447101-r7-44067e46bbcd.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keyPath
print("Environment variable set for credentials:", os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


# Initialize the Google Cloud NLP client
def analyze_note_and_extract_keywords(note_text):
    try:
        # Create the LanguageServiceClient
        client = language_v1.LanguageServiceClient()

        # Prepare the note as a document
        document = language_v1.Document(
            content=note_text, type_=language_v1.Document.Type.PLAIN_TEXT
        )

        # Perform entity analysis to extract keywords
        response = client.analyze_entities(document=document)

        # Extract and print educational keywords and their salience
        print("Extracted Keywords:")
        keywords = []
        for entity in response.entities:
            # Only include entities with a high salience (importance) score
            if entity.salience > 0.02:  # Adjust threshold as needed
                keywords.append((entity.name, language_v1.Entity.Type(entity.type_).name, entity.salience))
                print(f"Keyword: {entity.name}, Type: {language_v1.Entity.Type(entity.type_).name}, Salience: {entity.salience}")

        return keywords
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example student note
student_note = """
Machine learning is a branch of artificial intelligence that focuses on building systems that can learn and improve from experience. 
Key concepts include supervised learning, unsupervised learning, neural networks, decision trees, and reinforcement learning. 
Applications include recommendation systems, natural language processing, and image recognition.
"""

# Analyze the student's note
keywords = analyze_note_and_extract_keywords(student_note)

# Display the keywords
print("\nFinal Extracted Keywords:")
for keyword, entity_type, salience in keywords:
    print(f"- {keyword} (Type: {entity_type}, Salience: {salience})")