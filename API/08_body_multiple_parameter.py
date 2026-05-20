# <..01...Mix Path, Query and body parameters...>

# We can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.
# And you can also declare body parameters as optional, by setting the default to None
from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id : Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
#     q: str | None = None,
#     item: Item | None = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results



# <..02...multiple body parameter...>
# We can also declare multiple body parameters, e.g. item and user:


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class user(BaseModel):
#     username: str
#     fullname: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id : Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
#     q: str | None = None,
#     item: Item | None = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results



# <..03...Singular values in body...>


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class user(BaseModel):
#     username: str
#     fullname: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id : int, item: Item, user: user, importance: Annotated[int, Body()],
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results



# <..04...Multiple body params and query...>


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_items(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q":q})
#     return results 


# <..05...Embed a single body parameter...>
# if you want it to expect a JSON with a key item and inside of it the model contents, 
# as it does when you declare extra body parameters, you can use the special Body parameter "embed"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None





@app.put("/items/{item_id}")
async def update_items(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results



