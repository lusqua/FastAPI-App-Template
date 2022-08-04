from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from logging import info
from app import crud, schemas, models, get_db

router = APIRouter(
    prefix="/api/v1/users",
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["Users"])
async def read_users(db: Session = Depends(get_db)):
    info("List users - GET /api/v1/users")
    return crud.get_users(db)

@router.get("/{email}", tags=["User"])
async def read_user(email: str, db: Session = Depends(get_db)):
    info(f"Get user by email - GET /api/v1/users/{email}")
    return crud.get_user_by_email(db, email)

@router.post("/", tags=["User"])
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    info(f"Create user - POST /api/v1/users")
    return crud.create_user(db, user)