import logging
import joblib
import pandas as pd
import numpy as np
import os
import io
import azure.functions as func
from azureml.core import Model, Workspace


def main(inputBlob: func.InputStream, predictions: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputBlob.name}\n"
                 f"Blob Size: {inputBlob.length} bytes")


    ws = Workspace.from_config()
    # model_list = Model.list(ws)
    model_path = Model.get_model_path('liner_regression', _workspace=ws)
    model = joblib.load(model_path)
    logging.info(f"model loaded")

    data =pd.read_csv(io.BytesIO(inputBlob.read()), sep=',', header=None)
    # data = data.to_numpy()
    logging.info(f"{data}")


        # Reshape into a 2-dimensional array for model input
    prediction = model.predict(data.to_numpy().reshape(1, -1)) 
    # # [ 66.42063515,  92.83081999, 119.16201124, 145.4932025 ]
    logging.info(f"{prediction}")
    if (prediction[0] < 92.83081999):
        output = 'low'
    elif (92.83081999 <= prediction[0] <= 119.16201124):
        output = 'medium'
    else:
        output = 'high'  

    logging.info(f"OUTPUT: {output}")    

    predictions.set(output)             
