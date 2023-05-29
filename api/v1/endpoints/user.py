from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from models.car_model import ArtigoModel 
from models.user_model import UserModel

from schemas.car_schema import ArtigoSchema

from schemas.user_schema import UserSchemaArtigos
from schemas.user_schema import UserSchemaBase
from schemas.user_schema import UserSchemaCreate
from schemas.user_schema import UserSchemaUp

from core.security import generate_hash_pass
from core.auth import authenticate, create_access_token

from core.deps import get_session, get_current_user

router = APIRouter()

#GET usuário logado
@router.get('/logado', response_model=UserSchemaBase)
def get_logado(logged_user: UserModel = Depends(get_current_user)):
    return logged_user

# POST / SignUp -> Criar conta
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def post_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(
        nome=user.nome,
        sobrenome=user.sobrenome,
        email=user.email,
        senha=generate_hash_pass(user.senha)
    )
    
    async with db as session:
        try:
            session.add(new_user)
            await session.commit()

        
            return new_user
        except IntegrityError as e:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Email já cadastrado')
    
#GET usuários
@router.get('/allusers', response_model=List[UserSchemaBase])
async def get_users(db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):
    if logged_user.is_admin:
        async with db as session:
            query = select(UserModel)
            result = await session.execute(query)
            usuarios: List[UserSchemaBase] = result.scalars().unique().all()

            return usuarios
    else:
        raise HTTPException(detail='Apenas administradores podem ter essa informação',
                            status_code=status.HTTP_401_UNAUTHORIZED)
        
@router.get('/{user_id}', response_model=UserSchemaArtigos, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

    if user_id == logged_user.id or logged_user.is_admin:
        async with db as session:
            query = select(UserModel).filter(UserModel.id == user_id)
            results = await session.execute(query)
            user: UserSchemaArtigos = results.scalars().unique().one_or_none()
            
            if user:
                return user
            else:
                raise HTTPException(
                    detail='Usuário não encontrado',
                    status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(detail='Acesso negado',
                            status_code=status.HTTP_401_UNAUTHORIZED)
        
#PUT user
@router.put('/{user_id}', response_model=UserSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_user(user_id: int,user: UserSchemaUp, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

    if user_id == logged_user.id or logged_user.is_admin:
        async with db as session:
            query = select(UserModel).filter(UserModel.id == user_id)
            results = await session.execute(query)
            user_up: UserSchemaUp = results.scalars().unique().one_or_none()
            
            if user_up:
                if user.nome:
                    user_up.nome = user.nome
                
                if user.sobrenome:
                    user_up.sobrenome = user.sobrenome
                    
                if user.email:
                    user_up.email = user.email
                    
                if user.is_admin:
                    user_up.is_admin = user.is_admin
                
                if user.senha:
                    user_up.senha = generate_hash_pass(user.senha)
                
                await session.commit()
                
                return user_up
            else:
                raise HTTPException(
                    detail='Usuário não encontrado',
                    status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(detail='Acesso negado',
                            status_code=status.HTTP_401_UNAUTHORIZED)


# DELETE user
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

    if user_id == logged_user.id or logged_user.is_admin:
        async with db as session:
            query = select(UserModel).filter(UserModel.id == user_id)
            results = await session.execute(query)
            user_del: UserSchemaBase = results.scalars().unique().one_or_none()
            
            if user_del:
                await session.delete(user_del)
                await session.commit()
                
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                raise HTTPException(
                    detail='Usuário não encontrado',
                    status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(detail='Acesso negado',
                            status_code=status.HTTP_401_UNAUTHORIZED)
        
# POST login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(email=form_data.username, password=form_data.password, db=db)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Dados incorretos'
        )
        
    return JSONResponse(content={"access_token": create_access_token(sub=user.id), "token_type": "bearer"})
        
        