from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Lê as variáveis de ambiente
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Monta a URL de conexão
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
print("Tentando conectar com a URL:")
print(DATABASE_URL)

# Cria a engine e testa a conexão
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("Conexão bem-sucedida! ✅")
except Exception as e:
    print("Erro ao conectar no banco de dados ❌")
    print(e)
