from typing import List

from fastapi import APIRouter

from fastapi_profile import config
from fastapi_profile.databases import DBSession
from fastapi_profile.models import Measures
from fastapi_profile.schemas import MeasuresOut

router = APIRouter()


@router.get("/", response_model=List[MeasuresOut])
def dashboard():
    with DBSession(config.profile_config.engine) as session:
        return session.query(Measures).all()
