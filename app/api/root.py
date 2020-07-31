"""Summary here.

Details here.
"""

from fastapi import APIRouter

from app.api import health
from app.api.v1 import root as v1_root


router = APIRouter()
router.include_router(health.router, prefix='/health', tags=['health'])
router.include_router(v1_root.router, prefix='/v1', tags=['v1'])
