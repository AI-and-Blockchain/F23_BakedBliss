import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load your data into a Pandas DataFrame (replace with your data)
data = pd.read_csv("recommend_data.csv")  # Columns: user_id, item_id, rating

# Create a Surprise Dataset from the DataFrame
reader = Reader(rating_scale=(1, 5))  # Define the rating scale
data = Dataset.load_from_df(data[['user_id', 'item_id', 'rating']], reader)

# Split the data into a training and testing set
trainset, testset = train_test_split(data, test_size=0.2)

# Create and train the SVD model
model = SVD()
model.fit(trainset)

# Recommend items for a specific user
user_id = 1
items_to_recommend = set(data.df['item_id']) - set(data.df[data.df['user_id'] == user_id]['item_id'])
user_item_pairs = [(user_id, item, 0) for item in items_to_recommend]  # Use a constant rating of 0

# Predict ratings for the user-item pairs
user_item_predictions = model.test(user_item_pairs)

# Sort predictions and recommend top items
user_item_predictions.sort(key=lambda x: x.est, reverse=True)
top_n = 10  # Number of recommendations
recommended_items = [prediction.iid for prediction in user_item_predictions[:top_n]]
print("Top {} recommendations for user {}: {}".format(top_n, user_id, recommended_items))
