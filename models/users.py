from typing import Optional, List
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }