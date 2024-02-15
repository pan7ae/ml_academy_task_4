from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from joblib import dump, load
from scipy.sparse import csr_matrix
from fuzzywuzzy import process
import numpy as np
import pandas as pd

# Data model declaration for API input
class BeerRequest(BaseModel):
    user_beers: List[str]
    
# Create an instance of FastAPI
app = FastAPI()

# Load the KNN model from the file
FILE_PATH = 'models/model_knn.joblib'
model_knn = load(FILE_PATH)

# File path for the interaction matrix data
PATH = "data/interaction_matrix.csv"

# Load the interaction matrix and create a sparse matrix
interaction_matrix = pd.read_csv(PATH, index_col=0)
beer_features_df_matrix = csr_matrix(interaction_matrix.values)


# Function to get the list of user's beers considering closest matches
def get_beers_list(beers: List[str]) -> List[str]:
    """
    Filters a list of beers based on their presence in the interaction matrix or closest match.

    Parameters:
    - beers (List[str]): List of beers to filter.

    Returns:
    - user_beers (List[str]): Filtered list of beers, considering their presence or closest match in the interaction matrix.
    """
    user_beers = []
    for beer in beers:
        if beer in interaction_matrix.index:
            user_beers.append(beer)
        else:
            closest_match = process.extractOne(beer, interaction_matrix.index)[0]
            user_beers.append(closest_match)
    return user_beers

# Function to get recommendations using the KNN model
def get_recommendations_knn(user_beers: List[str], beers_length: int):
    """
    Generates recommendations based on user's beer preferences.

    Parameters:
    - user_beers (List[str]): List of beers representing user preferences.
    - beers_length (int): Number of beers to include in recommendations.

    Returns:
    - distances (ndarray): Array of distances to nearest neighbors.
    - indices (ndarray): Array of indices of nearest neighbors.
    """
    user_preferences = np.zeros((1, len(interaction_matrix.columns)))
    for beer in user_beers:
        if beer in interaction_matrix.index:
            user_preferences[0, :] += interaction_matrix.loc[beer, :].values
    
    distances, indices = model_knn.kneighbors(user_preferences, n_neighbors=7 + beers_length)
    return distances, indices

# Handler for the API route to get recommendations
@app.post("/recommendations/")
async def get_recommendations(beer_request: BeerRequest):
    """
    Generates recommendations based on user's beer preferences.

    Parameters:
    - beer_request (BeerRequest): Data model representing user's beer preferences.

    Returns:
    - recommendations (List[dict]): List of recommended beers with distances.
    """
    user_beers = beer_request.user_beers
    user_beers = get_beers_list(user_beers)
    beers_length = len(user_beers)
    distances, indices = get_recommendations_knn(user_beers, beers_length)
    recommendations = []
    for i in range(beers_length, len(distances.flatten())):
        idx = i - beers_length + 1
        recommendation = {
            "beer_name": interaction_matrix.index[indices.flatten()[i]],
            "distance": distances.flatten()[i]
        }
        recommendations.append(recommendation)
    return recommendations


