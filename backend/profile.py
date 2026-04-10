from fastapi import APIRouter, Form
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["userdb"]
collection = db["profiles"]

@router.get("/profile-data")
def get_profile(email: str):
    user = collection.find_one({"email": email}, {"_id": 0})
    return user if user else {}

@router.post("/update-profile")
def update_profile(
    email: str = Form(...),
    nickname: str = Form(""),
    gender: str = Form(""),
    country: str = Form(""),
    language: str = Form(""),
    timezone: str = Form("")
):
    collection.update_one(
        {"email": email},
        {"$set": {
            "nickname": nickname,
            "gender": gender,
            "country": country,
            "language": language,
            "timezone": timezone
        }},
        upsert=True
    )

    return {"status": "updated"}