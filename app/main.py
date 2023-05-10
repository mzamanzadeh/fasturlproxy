from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    url: str
    method: str
    data: str
    jsonn: str
    timeout: int
    headers : dict

@app.post("/send")
async def root(req:Item):
    try:
        res = requests.request(
            method=req.method,
            url=req.url,
            data=req.data,
            json=req.json,
            timeout=req.timeout,
            headers=req.headers
        )
        return {'status_code':res.status_code,'json':res.json()}
    except:
        return -1,[]

