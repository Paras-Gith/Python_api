# <..01...Additional validation...>
# "We are going to enforce that even though q is optional, 
# whenever it is provided, its length doesn't exceed 50 characters."
# Add Query to Annotated in the q parameter

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# <...02...Alternative (old): Query as the default value...>

#  @app.get("/items/")
# async def read_items(q: str | None, Query(default=None, max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Add more validations¶
# You can also add a parameter min_length

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50)] = "fixedquery",
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# <..03...Query parameter list / multiple values...>

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items

# <...Query parameter list / multiple values with defaults...>
# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items



# <..04...Declare more metadata...>
# You can add a title and discription

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(
#         title = "Query String",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3)] = None,
# ):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results



# <..05...Alias parameters...>
# <You can’t use item-query directly as a Python variable, 
# so declare it as item_query and set alias="item-query"—FastAPI 
# will then map the request parameter correctly.>

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results



# <..06...Deprecating parameters...>
# <Now let's say you don't like this parameter anymore.>
# You have to leave it there a while because there are 
# clients using it, but you want the docs to clearly show it as deprecated.
# Then pass the parameter deprecated=True to Query>

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(
#         alias= "item-query",
#         title = "Query String",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=50,
#         pattern="^fixedquery$",
#         deprecated=True
#         ),
#         ] = None,
# ):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results



# <..07...EXclude parameter from OpenAi...>
# To exclude a query parameter from the generated OpenAPI schema
# we use set the parameter include_in_schema of Query to False

# @app.get("/items/")
# async def read_items(
#         hidden_query: Annotated[str | None, Query(include_in_schema = False)]= None,
# ):
#     if hidden_query:
#         return{"hidden_query": hidden_query}
#     else:
#         return{"hidden_query": "Not found"}



# <..08...Custom Validation...>
# There could be cases where you need to 
# do some custom validation that can't be done with the parameters shown above.
# use a custom validator function that is applied after the normal validatio

# import random
# from pydantic import AfterValidator

# data =  {
#     "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
#     "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
#     "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
# }

# def check_valid_id(id: str):
#     if not id.startswith(("isbn-", "imdb-")):
#         raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
#     return id

# @app.get("/items/")
# async def read_items(
#     id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
# ):
#     if id:
#         item = data.get(id)
#     else:
#         id, item = random.choice(list(data.items()))
#     return {"id": id, "name": item}