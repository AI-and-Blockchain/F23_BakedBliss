import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recipe_words(recipe):
    recipe_data = ""
    for i in recipe.keys():
        if i != "ingredients":
            words = recipe[i].split(" ")
            for word in words:
                recipe_data += word + " "
        else:
            for item in recipe[i]:
                words = item.split(" ")
                for word in words:
                    recipe_data += word + " "

    return recipe_data

def train_model(recipe_data_lists):
    # TFIDF: Term Freuquency Inverse Document Frequency
    vectorizer = TfidfVectorizer()
    # vectorize recipes
    tfidf_matrix = vectorizer.fit_transform(recipe_data_lists)

    # cosine similarity function
    cosim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # format
    cosim_data = pd.DataFrame(cosim)
    
    return cosim_data

def get_data():
    
    # read recipe data and create dataframe (table)
    recipe_data = pd.read_json("testrecipes.json")
    recipe_data = pd.DataFrame(recipe_data)

    all_recipes = recipe_data["recipes"]

    recipe_data_lists = []
    for recipe in all_recipes:
        recipe_list_ = get_recipe_words(recipe)
        recipe_data_lists.append(recipe_list_)

    return recipe_data_lists

def append_to_model_data(data_list):
    new_data = get_data().append(data_list)
    return new_data

    



# .85 measure