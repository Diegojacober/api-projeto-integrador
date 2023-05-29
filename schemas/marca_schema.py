from typing import Optional, List

from pydantic import BaseModel

from schemas.car_schema import CarSchema

class MarcaSchema(BaseModel):
    id: Optional[int] = None
    nome: Optional[str]
    
    
    
    class Config:
        orm_mode = True
        
class MarcaSchemaCarros(MarcaSchema):
    carros: Optional[List[CarSchema]]