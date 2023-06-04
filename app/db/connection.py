import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


Base = declarative_base()


class DBConnection:
    def __init__(self) -> None:
        print(SQLALCHEMY_DATABASE_URL)
        self.__connection_string = SQLALCHEMY_DATABASE_URL
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_session(self):
        Session = sessionmaker(bind=self.__engine)
        return Session()
