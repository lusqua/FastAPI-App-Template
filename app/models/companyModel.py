from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


class Company(Base):
    __tablename__ = "Companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(String, default=datetime.utcnow)
    updated_at = Column(String, default=datetime.utcnow)
    user_limit = Column(Integer, default=5)
    CNPJ = Column(String, unique=True, index=True, nullable=False)
