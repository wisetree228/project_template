from pydantic import BaseModel, EmailStr, ValidationError
from datetime import datetime


class RegisterFormData(BaseModel):
    email: EmailStr
    username: str
    name: str
    surname: str
    password: str

class LoginFormData(BaseModel):
    email: EmailStr
    password: str