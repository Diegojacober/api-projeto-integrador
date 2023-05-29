from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.marca_model import MarcaModel
from models.user_model import UserModel

from schemas.marca_schema import MarcaSchema
from schemas.marca_schema import MarcaSchemaCarros

from core.deps import get_session, get_current_user

router = APIRouter()


@router.get('/{categoria_id}', response_model=MarcaSchemaCarros, status_code=status.HTTP_200_OK)
async def get_user(categoria_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

   
    async with db as session:
        query = select(MarcaModel).filter(MarcaModel.id == categoria_id)
        results = await session.execute(query)
        categoria: MarcaSchemaCarros = results.scalars().unique().one_or_none()
        
        if categoria:
            return categoria
        else:
            raise HTTPException(
                detail='marca não encontrada',
                status_code=status.HTTP_404_NOT_FOUND)