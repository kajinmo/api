from contextlib import asynccontextmanager
from fastapi import FastAPI
from .router import router
from .database import Base, engine, verify_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Verifica e cria tabelas se necessário
    if not verify_tables():
        raise Exception("Falha ao verificar/criar tabelas no banco de dados")
    else:
        print("Tabelas verificadas com sucesso")
    
    yield  # A aplicação roda aqui
    
    # Opcional: limpeza ao encerrar
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(router)