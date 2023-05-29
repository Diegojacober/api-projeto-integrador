from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class MarcaModel(settings.DB_BASEMODEL):
    __tablename__ = 'marcas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    carros = relationship(
        "CarModel",
        cascade='all, delete-orphan',
        back_populates="carros",
        uselist=True,
        lazy="joined"
    )
    