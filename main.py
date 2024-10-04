# uvicorn main:app --reload で立ち上げ

from fastapi import FastAPI,Query,Header,Response
from typing import Annotated
from pydantic import BaseModel
from typing import Union
import asyncio

app = FastAPI()

items=["Tシャツ","スカート","ブーツ","コート"]

class item(BaseModel):
    name: str
    price: float
    description: Union[str,None]=None

@app.get("/items")
def read_items(skip:int=0,limit:Annotated[int,Query(ge=1,le=10)]=10):
    return{"items":items[skip:skip+limit]}

@app.post("/items/")
def create_item(item:item):
    print(f"データを登録します:{item.name},{item.price},{item.description}")
    return item

@app.get("/sample/")
def read_sample(authorization:Union[str,None]=Header(default=None)):
    print(authorization)
    return{"message":"ヘッダー情報を取得しました"}

@app.get("/response/")
def read_sample(
    response:Response,
    authorization:Union[str,None]=Header(default=None)
):
    print(authorization)
    response.headers["custom-header"]="12345"
    return {"message":"ヘッダー情報を取得しました"}

@app.get("/sleep_time/")
async def sleep_time(sec:int):
    await asyncio.sleep(sec)
    return{"message":f"{sec}秒"}