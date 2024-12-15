from fastapi import FastAPI

import csv
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ACF Ratings API"}

@app.get("/players/{player_id}")
@app.get("/players/{player_id}/ratings")
async def read_player_ratings(player_id: int):

    df = pd.read_csv('master-ratings-unsorted.csv')
    player_data = df[df['ID'] == player_id]

    # print(player_id)

    if not player_data.empty:
        numerical_rating = int(player_data.iloc[0]['NumericalRating'])
        return {"player_id": player_id, "NumericalRating": numerical_rating}
    else:
        return {"error": "Player not found"}
        
    
@app.get("/players/{player_id}/info")
async def read_player_info(player_id: int):

    df = pd.read_csv('master-ratings-unsorted.csv')
    player_data = df[df['ID'] == player_id]

    if not player_data.empty:
        rating = player_data.iloc[0]['Rating']
        federation = player_data.iloc[0]['Federation']
        name = player_data.iloc[0]['Name']
        active = player_data.iloc[0]['Active']
        isRated = player_data.iloc[0]['Unrated']
        isNew = player_data.iloc[0]['New']
        confidence_level = player_data.iloc[0]['ConfidenceLevel']
        numericalRating = int(player_data.iloc[0]['NumericalRating'])

        return {"player_id": player_id, "Rating": rating, "Federation": federation, "Name": name, "Active": active, "Unrated": isRated, "New": isNew, "ConfidenceLevel": confidence_level, "NumericalRating": numericalRating}
    else:
        return {"error": "Player not found"}