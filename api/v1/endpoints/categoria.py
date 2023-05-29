from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.categoria_model import CategoriaModel
from models.user_model import UserModel

from schemas.categoria_schema import CategoriaSchemaACarros
from schemas.categoria_schema import CategoriaSchema

from core.deps import get_session, get_current_user

router = APIRouter()


@router.get('/{categoria_id}', response_model=CategoriaSchemaACarros, status_code=status.HTTP_200_OK)
async def get_user(categoria_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

   
    async with db as session:
        query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
        results = await session.execute(query)
        categoria: CategoriaSchemaACarros = results.scalars().unique().one_or_none()
        
        if categoria:
            return categoria
        else:
            raise HTTPException(
                detail='categoria não encontrada',
                status_code=status.HTTP_404_NOT_FOUND)