from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/") # decorator
async def root():
    return {"message": "hello world!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/createposts")
def create_posts(payload: dict = Body (...)): # this is to retrieve that body data
    print(payload)
    return {"new_post" : f"title {payload['title']} content: {payload['content']}"}
# title str, content str