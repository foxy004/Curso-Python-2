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
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')



class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

suits = Serie('suits', 2018, 2)
suits.dar_likes()
suits.dar_likes()
print(f'Nome: {suits.nome} - Ano: {suits.ano} - Temporadas: {suits.temporadas} - Likes :{suits.likes}')


