# Arquivo capitulo_3/q56.py

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
    total_jogadores = 0  # Atributo de classe

    def __init__(self, nome, energia, pontuacao=None):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = pontuacao if pontuacao else Pontuacao()
        
        Jogador.total_jogadores += 1  # Incrementa sempre que um jogador é criado

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

    

    
jogador1 = Jogador("Irmão do jorel", 100)
print(jogador1.nome)
print(jogador1.energia)
print(jogador1.pontuacao.mostrar_pontos())

j2 = Jogador("Lucas", 80)
j3 = Jogador("Jales
", 90)

print(f"Total de jogadores criados: {Jogador.total_jogadores}")  # Saída: 3




