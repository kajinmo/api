import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de conexão com o banco de dados
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Codificar a senha para evitar problemas com caracteres especiais
#encoded_password = urllib.parse.quote_plus(DB_PASSWORD)
print(DB_USER)
print(DB_PASSWORD)
print(DB_NAME)
print(DB_HOST)
print(DB_PORT)


# String de conexão com parâmetros adicionais para lidar com problemas de codificação
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criando engine do SQLAlchemy com opções adicionais
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        'client_encoding': 'utf8',
        'options': '-c timezone=UTC -c client_encoding=utf8'
    }
)

# Base para os modelos
Base = declarative_base()

# Definindo modelo Produto
class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    preco = Column(Integer)  # preço em centavos
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f"<Produto(nome='{self.nome}', preco={self.preco/100:.2f})>"


def test_connection():
    """Testa a conexão com o banco de dados sem criar tabelas"""
    try:
        # Tenta obter uma conexão
        conn = engine.connect()
        conn.close()
        print("Conexão com o banco estabelecida com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return False


def main():
    # Primeiro testa a conexão
    if not test_connection():
        return
    
    try:
        # Verifica se a tabela já existe antes de criá-la
        inspector = inspect(engine)
        if not inspector.has_table('produtos'):
            # Cria as tabelas no banco de dados
            Base.metadata.create_all(engine)
            print("Tabela 'produtos' criada com sucesso!")
        
        # Cria uma sessão
        Session = sessionmaker(bind=engine)
        session = Session()
        
        try:
            # Verificar se já existem produtos
            produtos_existentes = session.query(Produto).all()
            
            if not produtos_existentes:
                # Adicionar alguns produtos de exemplo
                produtos = [
                    Produto(nome="Notebook", descricao="Notebook Dell XPS 13", preco=799900),
                    Produto(nome="Smartphone", descricao="iPhone 15 Pro", preco=699900),
                    Produto(nome="Monitor", descricao="Monitor LG Ultrawide 34\"", preco=149900),
                    Produto(nome="Teclado", descricao="Teclado Mecanico Keychron K2", preco=39900),
                    Produto(nome="Mouse", descricao="Mouse Logitech MX Master 3", preco=29900)
                ]
                
                session.add_all(produtos)
                session.commit()
                print("Produtos de exemplo adicionados com sucesso!")
            
            # Consultar todos os produtos
            produtos = session.query(Produto).all()
            print("\nProdutos cadastrados:")
            for p in produtos:
                print(f"ID: {p.id}, Nome: {p.nome}, Preço: R$ {p.preco/100:.2f}")
                
            print("\nOperações no banco de dados realizadas com sucesso!")
            
        except Exception as e:
            print(f"Erro ao manipular dados: {e}")
            session.rollback()
        finally:
            session.close()
            
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")


if __name__ == "__main__":
    main()