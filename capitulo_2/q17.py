# Arquivo capitulo_2/q17.py

import random

class Jogador:
    def __init__(self, energia):
        self.__energia = energia
        self.pontuacao = Pontuacao(0)

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

class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        print(f"Adicionando {valor} pontos...")
        
    def mostrar_pontos(self):
        return f"Pontos: {self.__pontos}"
    

        
jogador1 = Jogador(100)
jogador1.usar_energia(50)
jogador1.recuperar_energia(10)



