import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import apolice
from app.rabbitmq.rabbit_connection import rabbit_conn

from dotenv import load_dotenv

config = load_dotenv()

# def get_env():


# dictConfig(LogConfig().dict())
# logger = logging.getLogger("insurance_service")

# logger.info("StartApp")
# logger.error("Dummy Error")
# logger.debug("Dummy Debug")
# logger.warning("Dummy Warning")


# @asynccontextmanager
# async def lifespan(_: FastAPI):
#     await rabbit_conn.connect()
#     yield
#     await rabbit_conn.disconnect()


app = FastAPI()
# app = FastAPI(lifespan=lifespan)


app.include_router(apolice.router)
