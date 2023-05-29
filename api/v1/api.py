from fastapi import APIRouter

from api.v1.endpoints import car
from api.v1.endpoints import user
from api.v1.endpoints import categoria
from api.v1.endpoints import marca

api_router = APIRouter()

api_router.include_router(car.router, prefix='/car', tags=['Cars'])
api_router.include_router(marca.router, prefix='/marca', tags=['Marcas'])
api_router.include_router(categoria.router, prefix='/categoria', tags=['Categorias'])
api_router.include_router(user.router, prefix='/user', tags=['Users'])