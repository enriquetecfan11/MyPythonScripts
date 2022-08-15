from typing import Union
from fastapi import FastAPI, File, UploadFile

import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Create and new endpoint called /items return productos.json
@app.get("/items/")
def read_items():
    with open("productos.json") as f:
        # Get inside json file and return it
        return json.load(f)
