from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from backend.db import get_db
from backend.session import create_session
import bcrypt

router = APIRouter()

@router.post("/login")
def login_user(
    email: str = Form(...),
    password: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()

    email = email.strip()

    # 🔍 get user
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        stored_password = user[4]   # hashed password

        # 🔐 check password
        if bcrypt.checkpw(password.encode(), stored_password.encode()):
            token = create_session(email)

            return JSONResponse({
                "status": "success",
                "token": token,
                "name": user[1] + " " + user[2],
                "email": user[3]
            })

    return JSONResponse({"status": "fail"})