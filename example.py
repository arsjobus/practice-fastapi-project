from fastapi import FastAPI

app = FastAPI()

# temporary in memory fake DB
items = []

# Initialize SQLAlchemy DB on Startup of API
# @app.on_event("startup")
# def on_startup():
#     print("Running database installer...")
#     init_db()

# 1 - make a root level API response
@app.get("/")
def root():
    return {"API": "/"}

# 2 - make a way to create a new item via query param
@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"item": item}

# 3 - make a way to lookup a item via url pattern matching
@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    return items[item_id]

# 4 - make a way to query to get all items back as a list
@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]