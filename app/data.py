from typing import List, Dict

class Produtos:
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


    def listar_produtos(self):
        return self.produtos
    

    def buscar_produto(self, id):
        for produto in Produtos.produtos:
            if produto['id'] == id:
                return produto
        return {'Status': 404, 'Mensagem': 'Produto não encontrado'}
    

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto