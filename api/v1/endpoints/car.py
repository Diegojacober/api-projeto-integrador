from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.car_model import CarModel 
from models.user_model import UserModel

from schemas.car_schema import CarSchema

from core.deps import get_session, get_current_user

router = APIRouter()

#POST Car
@router.post('/', response_model=CarSchema, status_code=status.HTTP_201_CREATED)
async def create_car(car: CarSchema, logged_user: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    new_car: CarModel = CarModel(
       name = car.name,
        description = car.description,
        combustivel =car.combustivel,
        cambio = car.cambio,
        ano = car.ano,
        url_image=car.url_image,
        marca_id=car.marca_id,
        categoria_id = car.categoria_id,
    )
    
    db.add(new_car)
    await db.commit()
    return new_car

# GET cars
@router.get('/', response_model=List[CarSchema])
async def get_cars(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarModel)
        result = await session.execute(query)
        cars: List[CarModel] = result.scalars().unique().all()
        
        return cars
    

# GET car
@router.get('/{car_id}', response_model=CarSchema, status_code=status.HTTP_200_OK)
async def get_artigo(car_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarModel).filter(CarModel.id == car_id)
        result = await session.execute(query)
        car: CarModel = result.scalars().unique().one_or_none()
        
        if car:
            return car
        else:
            raise HTTPException(detail='Car not found',
                                status_code=status.HTTP_404_NOT_FOUND)
            

# PUT car
@router.put('/{car_id}', response_model=CarSchema, status_code=status.HTTP_202_ACCEPTED)
async def get_artigo(car_id: int, car: CarSchema , db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):
    async with db as session:
        query = select(CarModel).filter(CarModel.id == car_id)
        print(f"O usuário {logged_user.id} - {logged_user.name} modificou o artigo {car_id}")
        result = await session.execute(query)
        car_up: CarModel = result.scalars().unique().one_or_none()
        
        if car_up:
            if car.name:
                car_up.name = car.name
            
            if car.description:
                car_up.description = car.description
                
            if car.ano:
                car_up.ano = car.ano
                
            if car.combustivel:
                car_up.combustivel = car.combustivel
                
            if car.cambio:
                car_up.cambio = car.cambio
                
            if car.url_image:
                car_up.url_image = car.url_image
                
            if car.categoria_id:
                car_up.categoria_id = car.categoria_id
                
            if car.marca_id:
                car_up.marca_id = car.marca_id
                
                
                
     
            await session.commit()
            
            return car_up
        else:
            raise HTTPException(detail='Car not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE car
@router.delete('/{car_id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_artigo(car_id: int, db: AsyncSession = Depends(get_session), logged_user: UserModel = Depends(get_current_user)):

    async with db as session:
        query = select(CarModel).filter(CarModel.id == car_id)
        print(f"O usuário {logged_user.id} - {logged_user.nome} deletou o carro {car_id}")
        result = await session.execute(query)
        car_del: CarModel = result.scalars().unique().one_or_none()
        
        
        if car_del:
            await session.delete(car_del)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Carro não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)

