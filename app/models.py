# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import declarative_base
from .database import Base 
from .schemas import Categoria
# Importa a função declarative_base do SQLAlchemy ORM.
# Cria uma classe base para modelos declarativos.

# Define uma nova classe Produto, herdando de Base.
# Esta classe representa uma tabela no banco de dados.
class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
    categoria = Column(Enum(Categoria), nullable=True)