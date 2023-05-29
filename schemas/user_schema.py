from typing import Optional, List


from pydantic import BaseModel, EmailError, EmailStr

class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    
    
    class Config:
        orm_mode = True
        

class UserSchemaCreate(UserSchemaBase):
    password: str
    

class UserSchemaUp(UserSchemaBase):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
