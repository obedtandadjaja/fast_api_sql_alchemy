"""Summary here.

Description here.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


# Before running this, make sure that the database exists
db_url = {
    'drivername': 'postgres',
    'username': 'obedtandadjaja',
    'password': '',
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'fast_api_sql_alchemy',
}
engine = create_engine(URL(**db_url))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
