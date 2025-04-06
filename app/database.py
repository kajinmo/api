# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Acessa e armazena variáveis de ambiente específicas - credenciais do banco de dados).
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Constrói a URL de conexão do banco de dados usando as variáveis de ambiente.
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria um motor de banco de dados SQLAlchemy que gerencia as conexões à base de dados.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma fábrica de sessões do SQLAlchemy que será usada para criar sessões.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para os modelos do SQLAlchemy.
Base = declarative_base()

# Define uma função geradora que fornece uma sessão de banco de dados e garante o fechamento da sessão.
def get_db():
    db = SessionLocal()
    try:
        # Fornece a sessão para a operação (utilizado em dependências do FastAPI).
        yield db
    finally:
        # Garante que a sessão seja fechada após o uso.
        db.close()