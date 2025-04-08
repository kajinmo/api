# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
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
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={
        'client_encoding': 'utf8',
        'options': '-c timezone=UTC -c client_encoding=utf8'
    }
)

# Cria uma fábrica de sessões do SQLAlchemy que será usada para criar sessões.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para os modelos do SQLAlchemy.
Base = declarative_base()


def import_models():
    # Isso garante que todos os modelos sejam registrados antes da criação das tabelas
    from . import models  # Ajuste o caminho conforme sua estrutura
    return Base

# Verifica e cria tabelas se necessário
def verify_tables():
    inspector = inspect(engine)
    import_models()
    required_tables = {table.name for table in Base.metadata.tables.values()}  # Adicione outras tabelas se necessário
    
    try:
        existing_tables = set(inspector.get_table_names())
        missing_tables = required_tables - existing_tables
        
        if missing_tables:
            print(f"Criando tabelas faltantes: {missing_tables}")
            Base.metadata.create_all(bind=engine)
            print("Tabelas criadas com sucesso!")
        else:
            print("Todas as tabelas necessárias já existem")
            
        return True
    except Exception as e:
        print(f"Erro ao verificar/criar tabelas: {e}")
        return False

# Define uma função geradora que fornece uma sessão de banco de dados e garante o fechamento da sessão.
def get_db():
    db = SessionLocal()
    try:
        # Fornece a sessão para a operação (utilizado em dependências do FastAPI).
        yield db
        print("Conexão com o banco de dados realizado!")
    finally:
        # Garante que a sessão seja fechada após o uso.
        db.close()