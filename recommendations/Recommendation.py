import csv
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy
import difflib
import json

class Recommendation:
    def __init__(self, rid, similarRatings):
        self.rid = rid
        #this will be a list of tuples with tuple[0] being other recipes as objects and tuple
        #[1] being a number that is the similarity between this recipe and the recipe in the tuple
        self.similarities = similarRatings
        self.allrankings = dict() #{'id': similarity rating}
        self.recommendDataFile = open('recommend_data.csv', 'w', newline='')
        self.recipeData = json.load(open('./testrecipes.json'))
        self.datawriter = csv.writer(self.recommendDataFile)

    def compute_similarity(self, input_string, reference_string):
    #The ndiff method returns a list of strings representing the differences between the two input strings.
        diff = difflib.ndiff(input_string, reference_string)
        diff_count = 0
        for line in diff:
        # a "-", indicating that it is a deleted character from the input string.
            if line.startswith("-"):
                diff_count += 1
    # calculates the similarity by subtracting the ratio of the number of deleted characters to the length of the input string from 1
        return 1 - (diff_count / len(input_string))
    
    #function that will retrieve all recipes in the current DB and determine a similarity between 
    #them for user recommendations
    def defineSimilarities(self):
        #find current recipe in recipeData
        #get ingredients and steps
        this_recipe = None
        this_string = None
        for recipe in self.recipeData['recipes']:
            if recipe['id'] == self.rid:
                this_ingredient = "".join(recipe['ingredients'])
                this_steps = "".join(recipe['steps'])
                this_string = this_ingredient + this_steps
                this_recipe = recipe
                break
        if not this_recipe:
            return -1
        
        for recipe in self.recipeData['recipes']:
            if recipe == this_recipe:
                continue
            else:
                curr_ingredient = "".join(recipe['ingredients'])
                curr_steps = "".join(recipe['steps'])
                string_compare = curr_ingredient + curr_steps
                similarity = self.compute_similarity(this_string, string_compare)
                if not recipe['id'] in self.allrankings:
                    self.allrankings[recipe['id']] = []
                    self.allrankings[recipe['id']].append(similarity)
                    self.allrankings[recipe['id']].append(recipe['name'])
                print(similarity)

        self.datawriter.writerow([this_recipe['id']]) 
        
        return

    def writeNewSimilarityForRecipe(self, r2data):
        #this function will be to write in the csv file the similarity rating calculated from
        #defineSimilarites function between rid (this current recipe) and rid2 (the recipe being
        #compared)
        #Future: add these similarity ratings to IPFS Node information about the current recipe
        None

    def closeCSVFile(self):
        self.recommendDataFile.close()

    def __str__(self):
        return str(self.rid) + '\n' + str(self.similarities)


#r1 = Recommendation(1, [])
#r1.defineSimilarities()
#print(r1.allrankings[2])
#r1.closeCSVFile()