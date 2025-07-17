# Arquivo capitulo_2/q51.py

import random

class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        print(f"Adicionando {valor} pontos...")
        
    def mostrar_pontos(self):
        return f"Pontos: {self.__pontos}"

class Jogador:
    def __init__(self, nome, energia, pontuacao=None):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = pontuacao if pontuacao else Pontuacao() # Agregação
        # Dentro do método, é feita uma verificação:
        # Se o usuário passar uma pontuação, ela será usada.
        # Caso contrário (pontuacao == None), será criada uma nova instância de Pontuacao().
        # Agora se for criado mais de um objeto jogador, a pontoação é diferente.


    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if valor < 0:
            self.__energia = 0
        else:
            self.__energia = valor


            
    def atacar(self, inimigo):
        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeiro...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {inimigo.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.__energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        if self.__energia < valor:
            print("Sem energia suficiente!")
        else:
            self.__energia -= valor
            print(f"Energia usada: {valor} Restante: {self.energia}")
        
    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = valor

        self.__energia += recuperado
        print(f"Jogador recuperou {recuperado} de energia. Energia atual: {self.__energia}")

# Os jogadores não dependem da existência da guilda (ou seja, podem existir fora dela).
class Guilda:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  # Lista de jogadores (agregação)

    def adicionar_jogador(self, jogador):
        if jogador not in self.jogadores:
            self.jogadores.append(jogador)
            print(f"{jogador.nome} entrou na guilda {self.nome}.")
        else:
            print(f"{jogador.nome} já está na guilda.")

    def remover_jogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
            print(f"{jogador.nome} saiu da guilda {self.nome}.")
        else:
            print(f"{jogador.nome} não está na guilda.")

    def listar_jogadores(self):
        print(f"Guilda: {self.nome} - Jogadores:")
        for jogador in self.jogadores:
            print(f"- {jogador.nome} | {jogador.pontuacao.mostrar_pontos()} | Energia: {jogador.energia}")

# Criando jogadores independentes
j1 = Jogador("Lucas", 80)
j2 = Jogador("Jales", 70)
j3 = Jogador("Irmão do Jorel", 100)

# Criando a guilda
guilda_heroes = Guilda("Heróis da Luz")

# Adicionando jogadores à guilda (agregação)
guilda_heroes.adicionar_jogador(j1)
guilda_heroes.adicionar_jogador(j2)

# Jogador ainda existe fora da guilda
print(f"{j3.nome} não entrou na guilda mas continua existindo!")  # Irmão do Jorel

# Listando membros da guilda
guilda_heroes.listar_jogadores()

# Remover jogador
guilda_heroes.remover_jogador(j1)

# Verificando novamente
guilda_heroes.listar_jogadores()
