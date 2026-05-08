# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
from fastapi import FastAPI

app = FastAPI()

# <.01...Query Parameter...>
# fake_items_db  = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]




# <.02...Optional Query Parameter...>
# you can declare optional query parameters, by setting their default to "None"

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}



# <.03...Query parameter type conversion...>

# @app.get("/items/{item_id}")
# async def read_item(item_id : str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing Item that has a long description"}

#         )
#     return item


# <.04...Multiple path and query parameters...>
# (We can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.)

# @app.get("/users/{user_id}/items/{item_id}/")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
