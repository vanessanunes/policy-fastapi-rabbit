from logging import FileHandler
from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME_SERVICE: str = "insurance_service"
    LOGGER_NAME_RABBIT: str = "rabbit_service"
    
    LOG_FORMAT: str = "%(levelprefix)s [%(asctime)s] -> %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            
        },
        "rabbit": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "args": "(./logs/consumer.log, w)"
            # "class": "logging.StreamHandler",
            # "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME_SERVICE: {"handlers": ["default"], "level": LOG_LEVEL},
        LOGGER_NAME_RABBIT: {"handlers": ["rabbit"], "level": LOG_LEVEL},
    }
