from fastapi import Depends, FastAPI, HTTPException
import logging.config

from app import crud, models, schemas
from app.db.database import SessionLocal, engine
from app.api.v1 import controllers

models.Base.metadata.create_all(bind=engine)

logging.config.fileConfig('./logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()


app.include_router(controllers.companyController_router)
app.include_router(controllers.userController_router)