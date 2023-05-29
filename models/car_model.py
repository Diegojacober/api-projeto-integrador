from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship

from core.configs import settings
from models.marca_model import MarcaModel
from models.categoria_model import CategoriaModel

class CarModel(settings.DB_BASEMODEL):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256))
    description = Column(String(256))
    combustivel = Column(String(256))
    cambio = Column(String(256))
    ano = Column(String(4))
    url_image = Column(String(256))
    valor = Column(Float(2))
    marca_id = Column(Integer, ForeignKey('marcas.id'))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    
    marca_responsavel = relationship("MarcaModel",
                            back_populates='cars',
                           lazy='joined')
    
    categoria_mae = relationship("CategoriaModel",
                            back_populates='carsm',
                           lazy='joined')