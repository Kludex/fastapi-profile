from time import time
from typing import Any, Callable, Dict

from fastapi import Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRoute
from starlette.routing import Match

from fastapi_profile import config
from fastapi_profile.databases import DBSession
from fastapi_profile.models import Measures


class ProfileRoute(APIRoute):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:

            start = time()
            response = await original_route_handler(request)
            elapsed = round(time() - start, 6)

            measurements = await self._measure(request)
            measurements["elapsed"] = elapsed
            print(config.profile_config)

            with DBSession(config.profile_config.engine) as session:
                session.add(Measures(**jsonable_encoder(measurements)))
                session.commit()
                print(session.query(Measures).all())

            print(measurements)
            return response

        return custom_route_handler

    async def _get_the_path(self, request: Request) -> str:
        routes = request.app.router.routes
        for route in routes:
            match, _ = route.matches(request)
            if match == Match.FULL:
                path = route.path

        return path

    async def _measure(self, request: Request) -> Dict[str, Any]:
        return {
            "path": await self._get_the_path(request),
            "method": request.method,
            "headers": request.headers,
            "url": str(request.url),
            "query_params": request.query_params.__dict__["_dict"],
            "path_params": request.path_params,
            "body": await request.body(),
            "form": await request.form(),
        }
