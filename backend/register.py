from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from backend.db import get_db
import bcrypt

router = APIRouter()

@router.post("/register")
def register_user(
    fname: str = Form(...),
    lname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()
    # 🔐 hash password
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    # check email already exists
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    existing = cursor.fetchone()

    if existing:
        return JSONResponse({"status": "exists"})  # ❌ already exists

    # insert new user
    cursor.execute(
        "INSERT INTO users (first_name, last_name, email, password) VALUES (%s,%s,%s,%s)",
        (fname, lname, email, hashed_password)
    )
    db.commit()

    return JSONResponse({"status": "registered"})