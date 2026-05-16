# In the same way that you can declare more validations and metadata for query parameters with Query, 
# you can declare the same type of validations and metadata for path parameters with Path

# <..01...how to use path for this...>
# <....Declare metadata...>
# using "Title"


from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results



# <..02...Order the parameters as you need...>


# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: int = Path(title="The ID of the item to get")
#     ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# If you want to:
# declare the "q" query parameter without a Query nor any default value
# declare the path parameter item_id using Path
# have them in a different order
# not use Annotated
# ...Python has a little special syntax for that.
# Pass "*", as the first parameter of the function


# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results



# <..03...Number validations: greater than or equal...>

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated [int, Path(title="This Id of the items to get", ge=1)], q=str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results


# <...Number validations: greater than and less than or equal...>


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated [int, Path(title="This Id of the items to get", ge=0, le=1000)], q=str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results


# <...Number validations: floats, greater than and less than...>


# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: Annotated [int, Path(title="This Id of the items to get", ge=0, le=1000)], 
#     q=str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     if size:
#         results.update({"size":size})
#     return results
