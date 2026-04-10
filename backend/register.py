from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from backend.db import get_db
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
mdb = client["userdb"]
collection = mdb["profiles"]

@router.post("/register")
def register_user(
    fname: str = Form(...),
    lname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()

    # MySQL (Prepared Statement)
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (fname, lname, email, password))
    db.commit()

    # MongoDB (profile)
    collection.insert_one({
    "email": email,
    "nickname": "",
    "gender": "",
    "country": "",
    "language": "",
    "timezone": ""
})

    return JSONResponse({"status": "registered"})