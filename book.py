from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'math'},
]

@app.get("/api/books")
async def read_all_books():
    return BOOKS

# path parameters
@app.get("/api/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS: 
        if book["title"].lower() == book_title.lower():
            return book
    
    return {"details": "Not Found"}


# query parameters
@app.get("/api/books/")
async def read_book_by_category(category: str):
    return [book for book in BOOKS if book["category"].lower() == category.lower()]    

# create book post request
@app.post("/api/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


# create book put request
@app.put("/api/books/update_book")
async def update_book(update_book=Body()):
    
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].lower() == update_book["title"].lower():
            BOOKS[i] = update_book
    
    return BOOKS


@app.delete("/api/books/delete_book/{book_title}")
async def delete_book(book_title):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].lower() == book_title.lower():
            BOOKS.pop(i)
            break
    
    return BOOKS