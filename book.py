from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@app.get("/books/", summary="Get a list of books", tags=["Books"])
async def get_books():
    return books

@app.get("/books/{book_id}/", summary="Get a book by ID", tags=["Books"])
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books", tags=["Books"], summary="Create a new book")
async def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"ok": True, "message": "Book created successfully"}
