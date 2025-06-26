from pydantic import BaseModel
from typing import Optional


class BlogDTO(BaseModel):
    title: str
    body: str
    published: Optional[bool]
