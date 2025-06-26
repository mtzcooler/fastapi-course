from fastapi import FastAPI, Depends
from dto.blogdto import BlogDTO
from domain.blog import Blog
from database import engine, Base, get_db
from sqlalchemy.orm import Session

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post('/blog')
def create(request: BlogDTO, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def index(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{id}')
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog
