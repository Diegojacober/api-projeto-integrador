from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.car_model import ArtigoModel 
from models.user_model import UserModel

from schemas.car_schema import ArtigoSchema

from core.deps import get_session, get_current_user

router = APIRouter()

#POST Artigo
@router.post('/', response_model=ArtigoSchema, status_code=status.HTTP_201_CREATED)
async def create_post(artigo: ArtigoSchema, usuario_logado: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    novo_artigo: ArtigoModel = ArtigoModel(
        titulo=artigo.titulo,
        descricao=artigo.descricao,
        url_fonte=artigo.url_fonte,
        usuario_id=usuario_logado.id
    )
    
    db.add(novo_artigo)
    await db.commit()
    return novo_artigo

# GET artigos
router.get('/', response_model=List[ArtigoSchema])
async def get_artgos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel)
        result = await session.execute(query)
        artigos: List[ArtigoModel] = result.scalars().unique().all()
        
        return artigos
    

# GET artigo
router.get('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_200_OK)
async def get_artigo(artigo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).filter(ArtigoModel == artigo_id)
        result = await session.execute(query)
        artigo: ArtigoModel = result.scalars().unique().one_or_none()
        
        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Artigo não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
            

# PUT artigo
router.put('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_202_ACCEPTED)
async def get_artigo(artigo_id: int, artigo: ArtigoSchema , db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):
    async with db as session:
        query = select(ArtigoModel).filter(ArtigoModel == artigo_id)
        print(f"O usuário {logged_user.id} - {logged_user.nome} modificou o artigo {artigo_id}")
        result = await session.execute(query)
        artigo_up: ArtigoModel = result.scalars().unique().one_or_none()
        
        if artigo_up:
            if artigo.titulo:
                artigo_up.titulo = artigo.titulo
            
            if artigo.descricao:
                artigo_up.descricao = artigo.descricao
                
            if artigo.url_fonte:
                artigo_up.url_font = artigo.url_fonte

            if logged_user.id != artigo_up.usuario_id:
                artigo_up.usuario_id = logged_user.id
                
            await session.commit()
            
            return artigo_up
        else:
            raise HTTPException(detail='Artigo não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE artigo
router.delete('/{artigo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_artigo(artigo_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

    if logged_user.is_admin: 
        async with db as session:
            query = select(ArtigoModel).filter(ArtigoModel == artigo_id)
            print(f"O usuário {logged_user.id} - {logged_user.nome} deletou o artigo {artigo_id}")
            result = await session.execute(query)
            artigo_del: ArtigoModel = result.scalars().unique().one_or_none()
            
            
            if artigo_del:
                await session.delete(artigo_del)
                await session.commit()
                
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                raise HTTPException(detail='Artigo não encontrado',
                                    status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(detail='O usuário não tem permissão para deletar',
                            status_code=status.HTTP_403_FORBIDDEN)

