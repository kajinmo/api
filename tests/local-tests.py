# -*- coding: utf-8 -*-
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base
from app.models import Produto

# Configuração do banco de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para limpar e preparar o banco de testes
@pytest.fixture(scope="function")
def test_db():
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

client = TestClient(app)

# Dados de teste
PRODUTO_TESTE = {
    "titulo": "Notebook Gamer",
    "descricao": "RTX 4090, 32GB RAM",
    "preco": 15000.99,
    "categoria": "eletronico"
}

def test_criar_produto(test_db):
    response = client.post("/produtos", json=PRODUTO_TESTE)
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == PRODUTO_TESTE["titulo"]
    assert "id" in data

def test_listar_produtos(test_db):
    # Primeiro cria um produto
    client.post("/produtos", json=PRODUTO_TESTE)
    
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_obter_produto_por_id(test_db):
    # Primeiro cria um produto
    produto = client.post("/produtos", json=PRODUTO_TESTE).json()
    
    response = client.get(f"/produtos/{produto['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == produto["id"]

def test_atualizar_produto(test_db):
    # Primeiro cria um produto
    produto = client.post("/produtos", json=PRODUTO_TESTE).json()
    
    # Dados completos para atualização
    dados_atualizacao = {
        "titulo": "Notebook Gamer Atualizado",
        "descricao": "RTX 4090, 32GB RAM, SSD 1TB",  # Mantém ou atualiza
        "preco": 14999.99,
        "categoria": "eletronico"  # Mantém o valor original
    }
    
    response = client.put(
        f"/produtos/{produto['id']}",
        json=dados_atualizacao
    )
    assert response.status_code == 200
    data = response.json()
    assert data["preco"] == dados_atualizacao["preco"]
    assert data["titulo"] == dados_atualizacao["titulo"]

def test_remover_produto(test_db):
    # Primeiro cria um produto
    produto = client.post("/produtos", json=PRODUTO_TESTE).json()
    
    response = client.delete(f"/produtos/{produto['id']}")
    assert response.status_code == 200
    
    # Verifica se foi removido
    response = client.get(f"/produtos/{produto['id']}")
    assert response.status_code == 404

def test_produto_nao_encontrado(test_db):
    response = client.get("/produtos/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"