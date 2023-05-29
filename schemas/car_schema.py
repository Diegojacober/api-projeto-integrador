from typing import Optional

from pydantic import BaseModel

class CarSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    description: Optional[str]
    combustivel: Optional[str]
    cambio: Optional[str]
    ano: Optional[int]
    categoria_id: Optional[int]
    
    
    class Config:
        orm_mode = True