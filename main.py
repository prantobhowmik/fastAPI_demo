from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []
class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

@app.get("/")
def read_root():
    return {"name": "Pranto"}


@app.get("/items")
def read_items():
    return db

@app.get("/items/{id}")
def read_item(id: int):
    item = id - 1
    return db[item]

@app.post("/items")
def create_item(item: Item):
    db.append(item.dict())
    return db - 1

@app.delete("/items/{id}")
def delete_item(id: int):
    db.pop(id-1)
    return {"message": "Item deleted"}
