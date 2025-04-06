from pydantic import BaseModel, PositiveInt
from typing import Optional

# validação na api antes de chegar no banco
class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveInt