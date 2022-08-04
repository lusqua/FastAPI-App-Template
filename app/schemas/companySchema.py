from pydantic import BaseModel, validator
from datetime import datetime

class Company(BaseModel):
    name: str
    user_limit: int = 5
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    cnpj: int

    class Config:
        orm_mode = True

    @validator('cnpj')
    def cnpj_validator(cls, v):
        if not v:
            raise ValueError('CNPJ is required')
        if len(str(v)) != 14:
            raise ValueError('CNPJ must be 14 digits')
        return v

    @validator('name')
    def name_validator(cls, v):
        if not v:
            raise ValueError('Name is required')
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters')
        return v