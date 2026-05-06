from fastapi import FastAPI

# app = FastAPI()


#<..01.....Path Parameters......>

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


#<..02.....Path Parameters with Types......>

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


#<..03.....Path Parameters should in Order......>

# ou need to make sure that the path for /users/me is declared before the one for /users/{user_id}
# you cannot redefine a path operation

# @app.get("/user/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/user/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


#<..04.....Path Parameters Predefined Values using Enum......>

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning HEllo!!"}

    if model_name.value == "lenet":
        return {"model_name": model_name,"message": "LeCNN all the Image"}

    return {"model_name": model_name, "message": "Have some residuals"}

