from fastapi import FastAPI
from .schemas import Blog
from .database import engine, Base

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post('/blog')
def create(request: Blog):
    return request

