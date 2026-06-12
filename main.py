from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api import policy_v2
from app.core.database import mongo_manager
from app.core.handler import configure_error_handlers
from app.core.settings import get_settings

settings = get_settings


# dictConfig(LogConfig().dict())
# logger = logging.getLogger("insurance_service")

# logger.info("StartApp")
# logger.error("Dummy Error")
# logger.debug("Dummy Debug")
# logger.warning("Dummy Warning")


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_manager.connect()
    yield
    mongo_manager.disconnect()
    # await rabbit_conn.connect()
    # yield
    # await rabbit_conn.disconnect()


app = FastAPI(title=settings.app_name, lifespan=lifespan)

configure_error_handlers(app)

app.include_router(policy_v2.router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
