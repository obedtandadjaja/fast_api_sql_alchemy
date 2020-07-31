"""Summary here.

Details here.
"""

from fastapi import APIRouter

from app.api.v1 import login


router = APIRouter()
router.include_router(login.router, prefix='/login', tags=['login'])
