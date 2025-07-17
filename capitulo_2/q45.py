# Arquivo capitulo_2/q45.py

import random

# Classe AnimalMontaria
class AnimalMontaria:
    def montar(self, criatura):
        print(f"Montando no(a) {criatura} e se preparando para a batalha!")

# Classe Jogador tranformada em Classe Guerreiro
class Guerreiro:
    def __init__(self,nome, energia):
        self.nome = nome
        self.__energia = energia
        self.pontos = Pontuacao(0)

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if self.__energia >= 0:
            self.__energia = valor
            
    def atacar(self, inimigo):
        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeiro...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontos.adicionar_pontos(10)
        
    def descansar(self):
        if self.__energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        self.__energia -= valor
        if self.__energia < 0:
            print("Sem energia suficiente!")
        else:
            print(f"Energia usada: {valor} Restante: {self.energia}")
        
    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = valor

        self.__energia += recuperado
        print(f"Jogador recuperou {recuperado} de energia. Energia atual: {self.__energia}")


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca
    
    @forca.setter
    def forca(self, valor):
        if valor >=5 and valor <= 20:
            self.__forca = valor
        else:
            print("A força deve ser no mínimo 5 e no máximo 20!")


    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
            return True
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")
            return False
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com {self.__forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
            print(f"Energia de {alvo.nome} acabou.")
            
        print(f"Energia do Jogador: {alvo.energia}")

# Classe Pontuação
class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        
    def mostrar_pontos(self):
        return self.__pontos
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, valor):
        if valor < 0:
            raise ValueError("A pontuação não pode ser negativa.") # O raise é usado para gerar uma excessão
        self.__pontos = valor


# Classe Cavaleiro herda de Guerreiro e AnimalMontaria
class Cavaleiro(Guerreiro, AnimalMontaria):
    def __init__(self, nome, energia):
        super().__init__(nome, energia)
        self.criatura = None
        self.montado = False

    def montar_criatura(self, criatura):
        self.criatura = criatura
        self.montado = True
        self.montar(criatura)  # usa o método da classe AnimalMontaria


# Testando Cavaleiro

cavaleiro = Cavaleiro("Sir Lancelot", 100)
inimigo = Inimigo("Orc", 50, 10)

cavaleiro.montar_criatura("Cavalo de Guerra")
cavaleiro.atacar(inimigo)  # usa o método da classe Guerreiro, sem sobrescrever