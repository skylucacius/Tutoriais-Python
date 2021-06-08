# usando o método mágico __repr__
# lista = [1, 2, 4, 5]
# print(repr(lista))

# Herança de uma classe com métodos abstratos
from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao
        
    def __len__(self):
        pass

lista = MinhaListagem("teste")
print(lista)