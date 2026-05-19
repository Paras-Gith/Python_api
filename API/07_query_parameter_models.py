# <..01...Query Parameter Models...>
# If you have a group of query parameters that are related, 
# you can create a Pydantic model to declare them


from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


# class FilterParams(BaseModel):
#     limit: int = Field(100, ge=0, le=100)
#     offset: int = Field(0, ge=0)
#     oder_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []

# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query



# <..02...Forbid Extra Query Parameters...>
# In some special use cases (probably not very common), 
# you might want to restrict the query parameters that you want to receive.
# You can use Pydantic's model configuration to "forbid" any "extra" fields


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


