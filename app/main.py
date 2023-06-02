from contextlib import asynccontextmanager
from logging.config import dictConfig
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api import apolice
from app.config.log_config import LogConfig
from app.config.rabbit_connection import rabbit_conn
import logging

# dictConfig(LogConfig().dict())
# logger = logging.getLogger("insurance_service")

# logger.info("StartApp")
# logger.error("Dummy Error")
# logger.debug("Dummy Debug")
# logger.warning("Dummy Warning")

@asynccontextmanager
async def lifespan(_: FastAPI):
    await rabbit_conn.connect()
    yield
    await rabbit_conn.disconnect()


app = FastAPI(lifespan=lifespan)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(exc)
    content = {'message': 'please, include valid input data.'}
    return JSONResponse(content=content)
	# exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	# print(exc_str)
	# # logging.error(f"{request}: {exc_str}")
	# content = {'status_code': 10422, 'message': exc_str, 'data': None}
	# return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


app.include_router(apolice.router)
