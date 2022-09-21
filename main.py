from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PostBody(BaseModel):
    first_val: int
    second_val: int


@app.post("/sum/")
async def return_sum(post_body: PostBody):
    return post_body.first_val + post_body.second_val


@app.post("/subtract/")
async def return_difference(post_body: PostBody):
    return post_body.first_val - post_body.second_val


@app.post("/multiplication/")
async def return_product(post_body: PostBody):
    return post_body.first_val * post_body.second_val


@app.post("/division/")
async def return_dividend(post_body: PostBody):
    return post_body.first_val / post_body.second_val