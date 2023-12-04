from flask import Blueprint, render_template, request
import time
import json
from moralis import evm_api
import sys
import gcoin_connection

# print the original sys.path
#print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('c:\\Users\\David Fuentes\\Documents\\Fall 2023\\CSCI 4964 - AI & Blockchain\\F23_BakedBliss\\recommendations')

# print the updated sys.path
#print('Updated sys.path:', sys.path)

# now you can import your module
from Recommendation import Recommendation
from web3 import Web3
import base64
import website.text_similarity as text_similarity

api_key = "%%%encoded%%%"

auth = Blueprint('auth', __name__)
#recommendations_for_recipe = Recommendation(recipe, [])
#recommendations_for_recipe.defineSimilarities()
#recommendations[recommendations_for_recipe.rid] = recommendations_for_recipe.allrankings

@auth.route("/", methods=["GET", "POST"])
def home():
    time.sleep(.001)
    if request.method == 'POST':
        searched_recipe = request.form.get("search_recipe")
        with open("testrecipes.json", "r") as readfile: 
            json_object = json.load(readfile)
        for item in json_object["recipes"]:
            if searched_recipe in item["lower_name"]:
                ingredients_to_html = ""
                for ingredient in item["ingredients"]:
                    ingredients_to_html += f'{ingredient}\n'
                return render_template("search_result.html", recipe_name=item["name"], ingredients_text=ingredients_to_html, steps_text=item["steps"])
    return render_template("home.html")

@auth.route("/upload", methods=["GET", "POST"])
def upload():
    time.sleep(.001)
    if request.method == 'POST':
        recipe_name = request.form.get("recipe_name")
        ingredient1 = request.form.get("ingredient1")
        ingredient2 = request.form.get("ingredient2")
        ingredient3 = request.form.get("ingredient3")
        ingredient4 = request.form.get("ingredient4")
        ingredient5 = request.form.get("ingredient5")
        ingredient6 = request.form.get("ingredient6")
        ingredient7 = request.form.get("ingredient7")
        ingredient8 = request.form.get("ingredient8")
        ingredient9 = request.form.get("ingredient9")
        ingredient10 = request.form.get("ingredient10")
        ingredient11 = request.form.get("ingredient11")
        ingredient12 = request.form.get("ingredient12")
        recipe_steps = request.form.get("recipe_steps")
        user_address = request.form.get("metamask_address")

        ingredients = [ingredient1,
                       ingredient2,
                       ingredient3,
                       ingredient4,
                       ingredient5,
                       ingredient6,
                       ingredient7,
                       ingredient8,
                       ingredient9,
                       ingredient10,
                       ingredient11,
                       ingredient12]
        
        recipe_ingredients = []
        
        for i in ingredients:
            if i != '':
                recipe_ingredients.append(i)

        recipe = {
            "name": recipe_name,
            "lower_name": recipe_name.lower(),
            "ingredients": recipe_ingredients,
            "steps": recipe_steps
        }

        print("Recipe:", recipe) 

        new_recipe_data = text_similarity.get_recipe_words(recipe)
        all_data = text_similarity.get_data()
        recipe_data_with_addition = all_data + [new_recipe_data]
        similarity_model = text_similarity.train_model(recipe_data_with_addition)

        good_recipe = False
        for i in range(len(similarity_model.loc[len(similarity_model) - 1])):
            if similarity_model.loc[len(similarity_model) - 1][i] > .85 and i != len(similarity_model) - 1:
                good_recipe = True

        if good_recipe:
            print("GODOD RECIPE")
            
            json_recipe = json.dumps(recipe, indent=4)
            with open("testrecipes.json", "w") as outfile:
                outfile.write(json_recipe)

            encoded = base64.b64encode(bytes(json.dumps(recipe), "ascii")).decode("ascii")

            body = [
                {
                    "path": f"BakedBliss/{recipe_name}.json",
                    "content": encoded
                }
            ]

            ipfs_hash = evm_api.ipfs.upload_folder(
                api_key=api_key,
                body=body,
            )
            print(ipfs_hash)
            # Call contract to write hash and award user
            if user_address != "":
                gcoin_connection.reward_user()


        else:
            pass
            #error message here


        
    return render_template("upload.html")
