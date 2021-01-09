from fastapi import FastAPI, Request
import json
import os
import pickle
import numpy as np

app = FastAPI()

number_to_text = {0: 'P2P', 1: 'audio', 2: 'chat', 3: 'email',
    4: 'file_transfer', 5: 'tor', 6: 'video'
}

# Load RandomForest
model_filename = os.path.join( '..','..','..','ml_kit', 'pre-trained-models','rf_model.pkl' )

with open(model_filename, 'rb') as m:
    rf_model = pickle.load(m)

app = FastAPI()

@app.post('/predict')
async def predict(request: Request):

    data = await request.body()

    instance = json.loads(data)

    id = instance['id']
    del instance['id']

    # reshape(-1, 1) if it contains a single feature
    # reshape(1, -1) if it contains a single instance
    instance = np.array( list(instance.values()) ).reshape(1, -1)

    prediction = rf_model.predict( instance )

    return {
        "id":id,
        "label": number_to_text[ prediction[0] ]
    }
