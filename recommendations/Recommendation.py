import csv
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

class Recommendation:
    def __init__(self, rid):
        self.rid = rid
        #this will be a list of tuples with tuple[0] being other recipes as objects and tuple
        #[1] being a number that is the similarity between this recipe and the recipe in the tuple
        self.similarities = list()
        self.recommendDataFile = open('recommend_data.csv', 'w', newline='')
        self.datawriter = csv.writer(self.recommendDataFile)
    
    #function that will retrieve all recipes in the current DB and determine a similarity between 
    #them for user recommendations
    def defineSimilarities(self, model, recipe1, recipe2):
        user_id = 0  # Using a single user for simplicity
        items_to_recommend = list(range(max(len(recipe1.ingredients), len(recipe2.ingredients))))
        
        # Convert Recipe objects to Surprise testset format
        user_item_pairs = [(user_id, item_id, 0) for item_id in items_to_recommend]  # Using a constant rating of 0
        
        # Predict ratings for the user-item pairs
        user_item_predictions = model.test(user_item_pairs)
        
        # Extract predicted ratings
        predicted_ratings = [prediction.est for prediction in user_item_predictions]
        
        # Calculate similarity based on predicted ratings
        similarity = sum(predicted_ratings) / len(predicted_ratings)
        
        return similarity

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


r1 = Recommendation(23)
print(r1)
r1.closeCSVFile()