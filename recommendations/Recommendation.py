class Recommendation:
    def __init__(self, rid):
        self.rid = rid
        #this will be a list of tuples with tuple[0] being other recipes as objects and tuple
        #[1] being a number that is the similarity between this recipe and the recipe in the tuple
        self.similarities = list()
    
    #function that will retrieve all recipes in the current DB and determine a similarity between 
    #them for user recommendations
    def defineSimilarities(self, recipes):
        print(recipes)

    def __str__(self):
        return str(self.rid) + '\n' + str(self.similarities)


r1 = Recommendation(23)
print(r1)