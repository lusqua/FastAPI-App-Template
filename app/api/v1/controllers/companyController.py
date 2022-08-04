from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from logging import info
from app import schemas, crud, models, main, get_db

router = APIRouter(
    prefix="/api/v1/company",
    responses={ 404: {"description": "Not found"} },
)


@router.get("/", tags=["Companies"])
async def list_companies(db: Session = Depends(get_db)):
    info("List companies - GET /api/v1/company")
    return crud.get_companies(db)

@router.get("/{company_id}", tags=["Company"])
async def read_company(company_id: int, db: Session = Depends(get_db)):
    info(f"Company by id - GET /api/v1/company/{company_id}")
    return crud.get_company_by_id(db, company_id)

@router.post("/", tags=["Company"])
async def create_company(company: schemas.Company, db: Session = Depends(get_db)):
    info("Create company - POST /api/v1/company")
    return crud.create_company(db=db, company=company)