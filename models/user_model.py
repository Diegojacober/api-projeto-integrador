from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UserModel(settings.DB_BASEMODEL):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    