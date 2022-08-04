from sqlalchemy.orm import Session
from logging import info
from app import models, schemas


def get_company_by_id(db: Session, company_id: int):
    info(f"Get company by id - CRUD function")
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    info(f"Get companies - CRUD function")
    return db.query(models.Company).offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.Company):
    info(f"Create company - CRUD function")
    db_company = models.Company(name=company.name, CNPJ=company.cnpj)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
