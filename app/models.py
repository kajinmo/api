# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Importa a função declarative_base do SQLAlchemy ORM.
# declarative_base é usado para criar uma classe base para modelos declarativos.
# Cria uma classe base para modelos declarativos.
# Classes que herdam de Base são automaticamente mapeadas para tabelas.
Base = declarative_base()


# Define uma nova classe Produto, herdando de Base.
# Esta classe representa uma tabela no banco de dados.
class Produto(Base):
    __tablename__ = "produtos"      # Define o nome da tabela no banco de dados.
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)