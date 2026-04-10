from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from backend.db import get_db
from backend.session import create_session

router = APIRouter()

@router.post("/login")
def login_user(
    email: str = Form(...),
    password: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    if user:
        create_session(email)

        return JSONResponse({
            "status": "success",
            "name": user[1] + " " + user[2],
            "email": user[3]
        })
    else:
        return JSONResponse({"status": "fail"})