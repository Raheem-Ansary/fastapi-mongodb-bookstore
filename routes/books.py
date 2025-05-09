from fastapi import APIRouter, Depends, HTTPException
from models.book import Book
from db import db
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from bson import ObjectId



SECRET_KEY = "9b3a1f2e78e21bc6adadf3d95e2e0cc4f5dfce158e93b7398e5dc8638b2b6de7"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



router = APIRouter(
    prefix="/books",
    tags=["books"]

    )




async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = await db.users.find_one({"email": payload["sub"]})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")



@router.post("/add_books")
async def add_book(book: Book, user: dict = Depends(get_current_user)):
    await db.books.insert_one(book.dict())
    return {"msg": "Book added"}



@router.get("/get_books")
async def get_books_by_author(author: str):
    books = await db.books.find({"author": author}).to_list(100)
    if not books:
        raise HTTPException(status_code=404, detail=f"No books found for author '{author}'")
    return [{**book, "_id": str(book["_id"])} for book in books]




@router.put("/edit_books/{book_id}")
async def update_book(book_id: str, book: Book, user: dict = Depends(get_current_user)):
    result = await db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": book.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Book not found or unchanged")
    return {"msg": "Book updated"}




@router.delete("/delete_books/{book_id}")
async def delete_book(book_id: str, user: dict = Depends(get_current_user)):
    result = await db.books.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"msg": "Book deleted"}