from fastapi import APIRouter

from api.v1.endpoints import car
from api.v1.endpoints import user

api_router = APIRouter()

api_router.include_router(car.router, prefix='/artigos', tags=['Artigos'])
api_router.include_router(user.router, prefix='/user', tags=['Users'])