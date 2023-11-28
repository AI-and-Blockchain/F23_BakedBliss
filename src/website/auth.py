from flask import Blueprint, render_template, request
import time
import json
from moralis import evm_api

api_key = "%%%encoded%%%"

auth = Blueprint('auth', __name__)

@auth.route("/", methods=["GET", "POST"])
def home():
    time.sleep(.001)
    if request.method == 'POST':
        searched_recipe = request.form.get("search_recipe")
        with open("testrecipes.json", "r") as readfile: 
            json_object = json.load(readfile)
        for item in json_object:
            if searched_recipe in item["name"].lower():
                return render_template("search_result.html")
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

        good_recipe = True

        if good_recipe:
            json_recipe = json.dumps(recipe, indent=4)
            with open("testrecipes.json", "w") as outfile:
                outfile.write(json_recipe)

            result = evm_api.ipfs.upload_folder(
                api_key=api_key,
                body=[recipe],
            )
            ipfs_hash = result
        
    return render_template("upload.html")
