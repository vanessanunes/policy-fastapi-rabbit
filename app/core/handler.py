from fastapi import FastAPI

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def configure_error_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        errors = exc.errors()

        return JSONResponse(
            status_code=400,
            content={
                "erro": [err["msg"] for err in errors],
            },
        )
