from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from core.configs import settings

class CarModel(settings.DB_BASEMODEL):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256))
    description = Column(String(256))
    combustivel = Column(String(256))
    cambio = Column(String(256))
    ano = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    marca_id = Column(Integer, ForeignKey('marcas.id'))
    categoria = relationship("CategoriaModel",
                           back_populates='cars',
                           lazy='joined')
    marca = relationship("MarcaModel",
                           back_populates='cars',
                           lazy='joined')