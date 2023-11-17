import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TFIDF: Term Freuquency Inverse Document Frequency
vectorizer = TfidfVectorizer()

# read recipe data and create dataframe (table)
recipe_data = pd.read_json("../recipes_raw_test_data/recipes_raw_nosource_fn.json")
recipe_data = pd.DataFrame(recipe_data)

print("RECIPE DATA")
print(recipe_data)

# vectorize recipes
tfidf_matrix = vectorizer.fit_transform(recipe_data)

print("VECTORIZED DATA")
print(tfidf_matrix)

# view voac and values
#print("WORDS + VALUES")
words = vectorizer.vocabulary_
#print(words)

# cosine similarity function
cosim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("COSINE SIMILARITY")
print(cosim[0,0])

# format
cosim_data = pd.DataFrame(cosim)
print(cosim_data)