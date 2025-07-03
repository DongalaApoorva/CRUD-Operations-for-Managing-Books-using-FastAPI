from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }
