from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/home")
async def home():
    return {"message": "Home page"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "None"):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: dict):
    return item


@app.get("/query/")
async def read_item(skip: int = 0, limit: int = 10):
    return {
        "message": skip + limit
    }
