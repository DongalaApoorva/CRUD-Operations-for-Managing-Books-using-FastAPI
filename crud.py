from sqlalchemy.orm import Session
import models, schemas

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book

def update_book(db: Session, book_id: int, updated: schemas.BookCreate):
    book = get_book(db, book_id)
    if book:
        for field, value in updated.dict().items():
            setattr(book, field, value)
        db.commit()
        db.refresh(book)
    return book
