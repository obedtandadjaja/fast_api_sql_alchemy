"""Summary here.

Description here.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import app.db.base
from app.db.base_class import Base
from app.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    # You can choose to seed the database here...
