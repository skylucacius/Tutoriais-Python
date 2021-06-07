class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__sobrenome = sobrenome
    
    def exibe_nome(self):
        print(self.__nome)
    def exibe_sobrenome(self):
        print(self.__sobrenome)
    def exibe_idade(self):
        print(self.__idade)
    def exibe_nome_Completo(self):
        print(self.__nome + " " + self.__sobrenome)

p1 = Pessoa("Lucas", "Santos", 30)
p1.exibe_nome_Completo()
print(p1._Pessoa__idade)