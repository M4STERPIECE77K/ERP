from fastapi import APIRouter

from routers.v1 import health

router = APIRouter(prefix="/v1")
router.include_router(health.router)
