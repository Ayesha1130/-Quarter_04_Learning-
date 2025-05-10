from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# Path Parameter Example
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # Required
        title="Item ID",
        description="A unique identifier for the item",
        ge=1  # Must be >= 1
    )
):
    return {"item_id": item_id}

# Query Parameters Example
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}

# Path + Query + Body Example
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Item data in JSON format")
):
    result = {"item_id": item_id}
    if q:
        result["q"] = q
    if item:
        result["item"] = item.model_dump()
    return result
