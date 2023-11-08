import pandas as pd

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# vars
sim_thresh = 0.5

# incorporate smart contracts

# loading data
data = pd.read_csv("recipes.csv")
data = pd.DataFrame(data)

# TFIDF: Term Freuquency Inverse Document Frequency
tfidf_vectorizer = TfidVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['ingredients'])

# cosine similarity function
cosim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# format
cosim_data = pd.DataFrame(cosim)