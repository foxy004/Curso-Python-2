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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

vingadores = Filme('Vingadores guerra infinita', 2018, 160)
vingadores.dar_likes()
#print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} : {vingadores.likes}')



class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

suits = Serie('suits', 2018, 2)
suits.dar_likes()
suits.dar_likes()
#print(f'{suits.nome} - {suits.ano} - {suits.temporadas} : {suits.likes}')

lista_programas = [vingadores, suits]

for programa in lista_programas:
    detalhes = programa.temporadas if hasattr(programa, 'temporadas') else programa.duracao
    print(f'{programa.nome} - {programa.ano} - {detalhes} D : {programa.likes}')



