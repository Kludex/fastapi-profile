from time import time
from typing import Any, Callable, Dict

from fastapi import Request, Response
from fastapi.routing import APIRoute
from starlette.routing import Match


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
        measurements = {
            "path": await self._get_the_path(request),
            "method": request.method,
            "headers": request.headers,
            "url": str(request.url),
            "query_params": request.query_params.__dict__["_dict"],
            "path_params": request.path_params,
        }

        if await request.form():
            measurements["form"] = await request.form()
        else:
            measurements["form"] = {}

        if await request.body():
            measurements["body"] = await request.body()
        else:
            measurements["body"] = ""

        return measurements
