# dúvida de um aluno do curso no fórum
from abc import ABC

class Beak (ABC):
    @property
    def has_beak(self):
        return True

    def __str__(self):
        return f'It has a beak.'
class Oviparous (ABC):
    @property
    def lay_eggs(self):
        return True

    def __str__(self):
        return f'It can lay eggs.'
class Bird(Vertebrate, Beak, Oviparous):
    def __init__(self, name):
        Vertebrate.__init__(self, name)

    def __str__(self):
        return f'{Vertebrate.__str__(self)}\n' \
               f'{self.name} is a Bird.\n' \
               f'{Oviparous.__str__(self)}\n'\
               f'{Beak.__str__(self)}'
