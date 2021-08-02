import logging

import azure.functions as func


def main(inputBlob: func.InputStream, predictions: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputBlob.name}\n"
                 f"Blob Size: {inputBlob.length} bytes")
    result = "HEllo"
    predictions.set(result)             
