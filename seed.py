"""Seeds the database with initial data.

This step includes creating the tables based on SQL Alchemy models. Afterwards,
initial data gets written to the database.
"""

import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info('Begin seed')
    db = SessionLocal()
    init_db(db)
    logger.info('End seed')

if __name__ == '__main__':
    main()
