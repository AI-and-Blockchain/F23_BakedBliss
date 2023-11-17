import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import csv
from pathlib import Path

# Load your data into a Pandas DataFrame
script_dir = Path(__file__).resolve().parent
file_path = script_dir / 'recommend_data.csv'
df = pd.read_csv(file_path)  # Columns: rid, rid2, rating

# Create a Surprise Dataset from the DataFrame
reader = Reader(rating_scale=(1, 5))  # Define the rating scale
data = Dataset.load_from_df(df[['rid', 'rid2', 'rating']], reader)

# convert data into a full trainset
trainset = data.build_full_trainset()

# Create and train the SVD model
model = SVD()
model.fit(trainset)

# Recommend items for a specific user
rid = 1
items_to_recommend = set(data.df['rid2']) - set(data.df[data.df['rid'] == rid]['rid2'])
user_item_pairs = [(rid, item, 0) for item in items_to_recommend]  # Use a constant rating of 0

# Predict ratings for the user-item pairs
user_item_predictions = model.test(user_item_pairs)

# Sort predictions and recommend top items
user_item_predictions.sort(key=lambda x: x.est, reverse=True)
top_n = 10  # Number of recommendations
recommended_items = [prediction.iid for prediction in user_item_predictions[:top_n]]
print("Top {} recommendations for user {}: {}".format(top_n, rid, recommended_items))
