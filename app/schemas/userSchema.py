from pydantic import BaseModel, validator
from sqlalchemy.orm import Session
from fastapi import Depends
from app import crud, get_db
from datetime import datetime

class User(BaseModel):
    name:str
    email: str
    password: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    company_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "",
                "password": "",
                "company_id": 1
            }
        }

    @validator('email')
    def email_validator(cls, v):
        if not v:
            raise ValueError('Email is required')
        if len(v) < 3:
            raise ValueError('Email must be at least 3 characters')
        if not '@' in v or not '.' in v:
            raise ValueError('Email must be valid')
        return v

    @validator('password')
    def password_validator(cls, v):
        if not v:
            raise ValueError('Password is required')
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

    @validator('name')
    def name_validator(cls, v):
        if not v:
            raise ValueError('Name is required')
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters')
        return v

    @validator('company_id')
    def company_id_validator(cls, v):
        if not v:
            raise ValueError('Company is required')
        if not crud.get_company_by_id(next(get_db()),v):
            raise ValueError('Company need exists')
        return v