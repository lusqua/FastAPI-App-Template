from sqlalchemy.orm import Session
from datetime import datetime
from logging import info
from app import models, schemas


def get_user(db: Session, user_id: int):
    info(f"Getting user with id:  {user_id} - CRUD function")
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    info(f"Getting user with email:  {email} - CRUD function")
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    info(f"Getting users - CRUD function")
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    info(f"Creating user - CRUD function")
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email,
        password=fake_hashed_password,
        name = user.name,
        company_id = user.company_id,
        created_at = datetime.now(),
        updated_at = datetime.now(),
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
