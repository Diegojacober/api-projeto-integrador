from typing import Optional

from pydantic import BaseModel

class CarSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    description: Optional[str]
    combustivel: Optional[str]
    cambio: Optional[str]
    ano: Optional[str]
    valor: Optional[float]
    url_image: Optional[str]
    categoria_id: Optional[int]
    marca_id: Optional[int]
    
    
    class Config:
        orm_mode = True