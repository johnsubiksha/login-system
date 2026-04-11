from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend import login, register, profile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register.router)
app.include_router(login.router)
app.include_router(profile.router)