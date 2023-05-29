from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class CategoriaModel(settings.DB_BASEMODEL):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    carsm = relationship(
        "CarModel",
        cascade='all, delete-orphan',
        uselist=True,
        lazy="joined",
        back_populates='categoria_mae'
    )
    