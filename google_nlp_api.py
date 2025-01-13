import os
from google.cloud import language_v1

keyPath = "API KEY"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keyPath
print("Environment variable set for credentials:", os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

def note_analyser(noteContent):
    print("Analyzing content:", noteContent)  # Debug: Check the input

    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=noteContent,
        type=language_v1.Document.Type.PLAIN_TEXT
    )

    try:
        response = client.analyze_entities(document=document)

        keywords = []
        for entity in response.entities:
            if entity.type_ in [
                language_v1.Entity.Type.ORGANIZATION,  # e.g., Universities, institutions
                language_v1.Entity.Type.LOCATION,     # e.g., educational regions
                language_v1.Entity.Type.EVENT,        # e.g., conferences, workshops
                language_v1.Entity.Type.WORK_OF_ART,  # e.g., books, publications
                language_v1.Entity.Type.CONSUMER_GOOD,  # e.g., learning tools
                language_v1.Entity.Type.OTHER         # Catch-all for other terms
            ]:
                keywords.append(entity.name)

        return list(set(keywords))
    except Exception as e:
        print("Error during analysis:", e)  # Debug
        return []
