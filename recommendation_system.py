import numpy as np
import pandas as pd

# Load the catalog of learning materials
_data_path = 'combined_learning_materials.csv'
_data = pd.read_csv(_data_path)
_data['Combined_Features'] = (
    _data['Title'].fillna('') + ' ' + _data['Description'].fillna('')
)


def recommend_learning_materials(title: str, content: str, top_n: int = 3):
    """
    Recommend the top_n learning materials most similar to the user's note.

    If sklearn or scipy fail to import (e.g., due to DLL/page-file errors),
    returns an empty list instead of crashing.
    """
    # import to avoid module-level scipy/sklearn DLL load issues
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError as e:
        print(f"Warning: sklearn or scipy import failed: {e}")
        return []

    # Prepare texts
    combined_series = _data['Combined_Features']

    # Vectorize full catalog
    tfidf = TfidfVectorizer(stop_words='english', dtype=np.float32)
    tfidf_matrix = tfidf.fit_transform(combined_series)

    # Build query from title+content
    query = f"{title or ''} {content or ''}".strip()
    user_vec = tfidf.transform([query])

    # Compute similarities (1×N)
    sims = cosine_similarity(user_vec, tfidf_matrix)[0]

    # Rank & dedupe
    sim_series = pd.Series(sims, index=_data['Title'])
    sim_series = sim_series[~sim_series.index.duplicated(keep='first')]
    top_items = sim_series.nlargest(top_n)

    # Assemble recommendations
    recs = []
    for doc_title, score in top_items.items():
        row = _data.loc[_data['Title'] == doc_title].iloc[0]
        recs.append({
            'title':       doc_title,
            'description': row['Description'] if pd.notna(row['Description']) else "No description available",
            'url':         row['URL']         if pd.notna(row['URL'])         else "No link available",
            'subject':     row['Subject']     if pd.notna(row['Subject'])     else "No subject area provided",
            'author':      row['Author']      if pd.notna(row['Author'])      else "No author",
            'similarity':  float(score),
            'type':        'Book' if pd.isna(row['URL']) else 'Link'
        })
    return recs
