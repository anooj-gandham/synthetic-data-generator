from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DataDeduplicator:
    def remove_duplicates(self, data_list, similarity_threshold=0.8):
        vectorizer = TfidfVectorizer().fit_transform(data_list)
        vectors = vectorizer.toarray()
        unique_data = []

        for i, vector in enumerate(vectors):
            is_duplicate = False
            for j in range(i):
                sim = cosine_similarity([vector], [vectors[j]])[0][0]
                if sim > similarity_threshold:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_data.append(data_list[i])

        return unique_data
