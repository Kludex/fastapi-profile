import time
from typing import Callable

from fastapi import Request
from fastapi.responses import Response
from fastapi.routing import APIRoute


class ProfileRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            print(request.scope)
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler
