from fastapi import FastAPI, Depends, status, HTTPException
from dto.blogdto import BlogDTO
from domain.blog import Blog
from database import engine, Base, get_db
from sqlalchemy.orm import Session

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post('/blog', status_code=status.HTTP_201_CREATED)
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


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog
