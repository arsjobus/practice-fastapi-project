from fastapi import FastAPI
from app.database import init_db, sessionmaker, engine
from app.models import Items

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

Session = sessionmaker(bind=engine)
session = Session()

# GET Root /
@app.get("/")
def get_root():
    return { "API": "/" }

# GET Items
@app.get("/items")
def list_items(limit: int = 10):
    all_items = session.query(Items).all()
    return all_items

# GET an item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return session.query(Items).filter(Items.id == item_id).first()

# Create an Item
@app.post("/items")
def create_item(item_name: str) -> str:
    new_item = Items(name=item_name)
    session.add(new_item)
    session.commit()
    return item_name