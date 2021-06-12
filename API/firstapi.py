from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# databases
menu = [{'id':0, 'name': 'Plain Rice','price':100.50} ,
{'id':1, 'name': 'Daal','price':80.00},
{'id':2, 'name': 'Chicken','price':200.00, 'pieces_per_plate':4},
{'id':3, 'name': 'Mutton','price':300.00, 'pieces_per_plate':4},
{'id':4, 'name': 'Fish','price':150.00,'pieces_per_plate':4}
]
my_orders = []
# restaurant model to store food details
class Restaurant(BaseModel):
    id: int
    name: str
    price: float
    pieces_per_plate: Optional[int] = None

# Home/welcome route
@app.get("/")
def read_root():
    return {"Name": "My Restaurant",
            "What You Can do here": "View menu, add items, remove items from orders"
    }

# Get all items
@app.get("/restaurant")
def get_menu():
    return menu

# Get my_orders
@app.get("/show_my_orders")
def get_my_orders():
    return my_orders

# get an item
@app.get("/menu/{id}")
def get_an_item(id: int):
    item = id - 1
    return menu[item]

# add a new item
@app.post("/additem")
def add_order(additem: Restaurant):
    my_orders.append(additem.dict())
    return my_orders[-1]

# delete an order
@app.delete("/myorder/{id}")
def delete_order(id: int):
    for i in my_orders:
        if i['id'] == id:
            my_orders.remove(i)
    return {"task": "deletion successful"}