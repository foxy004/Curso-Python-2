class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def dar_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def imprime(self):
        print(f'{self.__nome} - {self.ano} : {self.__likes} likes.')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} minutos : {self.likes} likes.')


vingadores = Filme('Vingadores guerra infinita', 2018, 160)
vingadores.dar_likes()
#print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} : {vingadores.likes}')



class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temporadas: {self.likes} likes.')

suits = Serie('suits', 2018, 2)
suits.dar_likes()
suits.dar_likes()
#print(f'{suits.nome} - {suits.ano} - {suits.temporadas} : {suits.likes}')

lista_programas = [vingadores, suits]

for programa in lista_programas:
    programa.imprime()



