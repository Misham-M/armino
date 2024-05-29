from fastapi import FastAPI
from pydantic import BaseModel
from lib1 import *
app = FastAPI()
class Chracter(BaseModel):
    name: str
    details:str
@app.get("/")
async def root():
    return {"message": "Hello Story Generator"}
@app.post("/api/create_character")
async def create_character(character:Chracter):
    d=check_user(character.name)
    if(d>0):
        return {"message":"Username Already Exists"}
    else:
        id=getnextid()
        create_user(id,character.name,character.details)
    return character
@app.post("/api/generate_story")
async def generate_story(character:Chracter):
    return {"message":"Generate Story"}