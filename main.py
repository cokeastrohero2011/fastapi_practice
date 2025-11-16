from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health_check")
def health_check():
    return {"message": "FastAPI is running properly"}


# path parameters

@app.get("/items/{item_id}")
def items(item_id:int):
    return {"data":f"{item_id}"}

# multiple path parameters
@app.get("/items/{item_id}/{item_name}")
def items(item_id:int, item_name:str):
    return {
        "item_name":item_name,
        "item_id": item_id
    }


#query parameters

@app.get("/query_param1")
def query_param1(data1: int, data2: str= "Jacob"):
    return{
        "return_param1": data1,
        "return_param2": data2
    }

# query and path params


@app.get("/items2/{item_name2}")
def items2(item_name2: str, item_price2: float):
    return {
        "return_param1": item_name2,
        "return_param2": item_price2
    }


# pydantic base model

class temp(BaseModel):
    data1: str
    data2: int
    data3: float

@app.post("/temp2")
def temp2(dummy: temp):
    return{
        "my_data": dummy
    }