from sentence_transformers import SentenceTransformer
import numpy as np


def get_embeddings(texts: list[str]) -> np.ndarray:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    return embeddings


def calculate_embedding_similarities(
    synthetic_embeddings: np.ndarray, db_embeddings: np.ndarray, threshold: float = 0.7
) -> list[int]:
    """
    Optimized function to compare synthetic embeddings with database embeddings.
    Returns indices of synthetic embeddings that are not highly similar to any database embedding.
    
    Parameters:
    - synthetic_embeddings: np.ndarray (n_synthetic, embedding_dim)
    - db_embeddings: np.ndarray (n_db, embedding_dim)
    - threshold: float, similarity threshold for rejection (default=0.7)
    
    Returns:
    - List of indices of synthetic embeddings that are not highly similar to any db embeddings.
    """
    # Compute cosine similarity using dot product (efficient computation)
    similarities = np.dot(synthetic_embeddings, db_embeddings.T)  # Shape: (n_synthetic, n_db)
    print("SIMILARITIES MATRIX")
    print(np.round(similarities, 2))
    # Find the max similarity for each synthetic embedding
    max_similarities = np.max(similarities, axis=1)

    # Get indices where max similarity is below threshold
    valid_indices = np.where(max_similarities < threshold)[0]

    return valid_indices.tolist()
