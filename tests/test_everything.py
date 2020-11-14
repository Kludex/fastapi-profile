from fastapi import APIRouter, FastAPI
from sqlalchemy import create_engine

from fastapi_profile import ProfilerRouteFactory
from fastapi_profile.router import router as profiler

app = FastAPI()

engine = create_engine("sqlite:///test.db")


ProfileRoute = ProfilerRouteFactory(engine=engine, debug=True)
router = APIRouter(route_class=ProfileRoute)


@router.get("/")
def home():
    return "Hello World!"


app.include_router(router)
app.include_router(profiler, prefix="/dashboard")
