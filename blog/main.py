from fastapi import FastAPI, Depends
from dto.blogdto import BlogDTO
from domain.blog import Blog
from database import engine, Base, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: BlogDTO, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

