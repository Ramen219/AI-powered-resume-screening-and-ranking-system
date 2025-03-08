from sklearn.feature_extraction.text import TfidfVectorizer 

def rank_resumes(resume_texts, job_description):
    """
    Rank multiple resumes against a job description using TF-IDF and cosine similarity.
    
    :param resume_texts: List of extracted resume texts.
    :param job_description: Job description text.
    :return: List of similarity scores.
    """
    corpus = [job_description] + resume_texts  # Job description first, then resumes
    vectorizer = TfidfVectorizer(stop_words='english')  # Exclude common words
    tfidf_matrix = vectorizer.fit_transform(corpus)  # Transform text into TF-IDF matrix
    
    job_vector = tfidf_matrix[0]  # Job description vector
    resume_vectors = tfidf_matrix[1:]  # Resume vectors

    scores = (resume_vectors * job_vector.T).toarray().flatten()  # Compute cosine similarity
    return [round(score * 100, 2) for score in scores]  # Convert to percentage
