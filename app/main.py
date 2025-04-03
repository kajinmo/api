from fastapi import FastAPI
from typing import List, Dict


app = FastAPI()

#45:38


@app.get("/")
def ola_mundo():
    return {"Olá": "Mundo"}


produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "um telefone",
        "preco": 1500.0
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "um computador portátil",
        "preco": 3500.0
    }
]


@app.get("/")
def ola_mundo():
    return {"Olá": "Mundo"}


# definir a rota
@app.get("/produtos") # recebe requisições GET
def listar_produtos(): #response
     return produtos



"""
# definir a rota
@app.get("/") # recebe requisições GET
def ola_mundo(): #response
        return {'Olá': 'Mundo'}


# definir a rota que puxa produto
# response_model: a saída da validação
@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
        return lista_de_produtos.listar_produtos()


@app.get("/produtos/{id}", response_model=ProdutosSchema)
def buscar_produto(id: int):
        return lista_de_produtos.buscar_produto(id)


@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
        return lista_de_produtos.adicionar_produto(produto.model_dump())
"""