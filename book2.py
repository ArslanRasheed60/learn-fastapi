from typing import Optional
from fastapi import Body, FastAPI,Path, Query, HTTPException

from pydantic import BaseModel, Field
from starlette import status

# status.HTTP_204_NO_CONTENT
# api is successfull but it is not returning in data

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(ge=0, le=5)
    
    class Config:
        json_schema_extra = {
            'example': {
                    "title": "A need book",
                    "author": "byarslan",
                    "description": "A new description",
                    "rating": 5
                    }
        }
    
def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
    

BOOKS = [
    Book(1, 'Computer Science Pro', 'arslan', 'A very nice book', 5),
    Book(2, 'Be fast with Fastpai', 'arslan', 'A very nice book', 5),
    Book(3, 'Master Endpoints', 'arslan', 'A very nice book', 5),
    Book(4, 'HP1', 'author 1', 'Book Description', 1),
    Book(5, 'HP2', 'author 2', 'Book Description', 2),
    Book(6, 'HP3', 'author 3', 'Book Description', 3),
]

@app.get("/api/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

# path parameters
@app.get("/api/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS: 
        if book.id == book_id:
            return book
    
    return HTTPException(status_code=404, detail="Not found")

# query parameters
@app.get("/api/books/", status_code=status.HTTP_200_OK)
async def read_book_by_category(book_rating: int = Query(gt=0, lt=6)):
    return [book for book in BOOKS if book.rating == book_rating]    


# create book post request
@app.post("/api/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(new_book: BookRequest):
    print()
    print("**new_book")
    print(*new_book)
    BOOKS.append(find_book_id(Book(**new_book.model_dump())))
    return BOOKS






# # create book put request
# @app.put("/api/books/update_book")
# async def update_book(update_book=Body()):
    
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["title"].lower() == update_book["title"].lower():
#             BOOKS[i] = update_book
    
#     return BOOKS


# @app.delete("/api/books/delete_book/{book_title}")
# async def delete_book(book_title):
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["title"].lower() == book_title.lower():
#             BOOKS.pop(i)
#             break
    
#     return BOOKS