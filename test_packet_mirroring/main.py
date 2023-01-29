from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    name: str


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/item/")
async def create_item(item: Item):
    return item
