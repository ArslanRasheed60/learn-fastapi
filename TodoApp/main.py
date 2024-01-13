from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
from models import Todos
from database import SessionLocal, engine
import auth

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]


app.include_router(auth.router)
        
@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()