from sqlalchemy.engine import Engine

from fastapi_profile import config
from fastapi_profile.config import ProfileConfig
from fastapi_profile.databases import DBSession
from fastapi_profile.models import Measures
from fastapi_profile.route import ProfileRoute


def ProfilerRouteFactory(engine: Engine, debug: bool = False):
    config.profile_config = ProfileConfig(debug=debug, engine=engine)

    Measures.__table__.create(engine, checkfirst=True)

    if debug:
        print(config.profile_config)
        with DBSession(engine) as session:
            print(session.query(Measures).all())

    return ProfileRoute
