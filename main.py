import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database."}
    else:
        return {"data": f"{limit} blogs from the database."}


@app.get('/blog/unpublished')
def unpublished():
    return {"data": "All unpublished blogs"}


@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {"data": {'Comment A', 'Comment B'}}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
