# -*- coding: utf-8 -*-
from enum import Enum
from typing import Optional
from pydantic import BaseModel, PositiveFloat, ConfigDict, field_serializer


# Define o Enum para categorias
class Categoria(str, Enum):
    ELETRONICO = "eletronico"
    CURSO = "curso"
    ALIMENTO = "alimento"


# Modelo para um item de produto
class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    categoria: Optional[Categoria]
    
    # Adiciona o campo 'categoria', que deve ser um valor do Enum 'Categoria'
    # Configuração para ORM
    model_config = ConfigDict(from_attributes=True)

    # Serializador para converter o Enum para string ao exportar
    @field_serializer('categoria')
    def serialize_categoria(self, categoria: Categoria, _info):
        return categoria.value if categoria else None