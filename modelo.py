from mailbox import NotEmptyError


class Playlist:

    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def dar_like(self):
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

    def __str__(self):
        return (f'{self.__nome} - {self.ano} : {self.__likes} likes.')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return(f'{self.nome} - {self.ano} - {self.duracao} minutos : {self.likes} likes.')



class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
       return (f'{self.nome} - {self.ano} - {self.temporadas} temporadas: {self.likes} likes.')


tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
vingadores = Filme('Vingadores guerra infinita', 2018, 160)
suits = Serie('suits', 2018, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
suits.dar_like()
suits.dar_like()
suits.dar_like()




lista_programas = [vingadores, suits, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', lista_programas)
print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
    print(programa)



