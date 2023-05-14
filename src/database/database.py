from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.dbconfig import pgsql_connection_string

engine = create_engine(pgsql_connection_string)


def get_session():
    return sessionmaker(engine)
