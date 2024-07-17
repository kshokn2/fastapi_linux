# fastapi
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models.my_models import Data

# router
from routes.my_routes import test_router

from utils import sleep_func

import os
import sys
import httpx
import requests

sys.path.append( os.path.abspath(os.path.dirname(__file__)) )

# fastapi
my_app = FastAPI(docs_url=None, redoc_url=None) # No use swagger API docs

# routers
my_app.include_router(test_router)

# GET api
@my_app.post("/get")
async def get_func(request: Request):
    """
    get functions
    """
    return "Done"

# POST api
@my_app.post("/url")
async def predict(request: Request, my_data: Data):
    print(my_data.user)
    print(my_data.code)

    try:
        result = await sleep_func(t=5)
        async with httpx.AsyncClient() as client:
            response = await client.post("http://url:8000", headers={"Content-Type":"application/json"}, data={"data":"data"})
            print(response)
    except Exception as e:
        return JSONResponse(content={"result":"fail"})
    
    return JSONResponse(content={"result":"success"})