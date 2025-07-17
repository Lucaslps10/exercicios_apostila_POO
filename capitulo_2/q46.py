# Arquivo capitulo_2/q46.py

import random

class Arma:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print("Este método deve ser implementado pelas subclasses.")

class Espada(Arma):
    def __init__(self, nome):
        super().__init__(nome)

    def atacar(self):
        dano = random.randint(5, 15)
        return f"{self.nome} realiza um corte poderoso! e causa {dano} de dano!\n"
    
class Arco(Arma):
    def __init__(self, nome):
        super().__init__(nome)

    def atacar(self):
        dano = random.randint(5, 15)
        return f"{self.nome} dispara uma flecha à distância e causa {dano} de dano!\n"
    
class Jogador:
    def __init__(self,nome, energia):
        self.nome = nome
        self.__energia = energia
        self.pontos = Pontuacao(0)
        self.arma = None  # Associação com a classe Arma  <-------------

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

    def equipar_arma(self, arma): 
        self.arma = arma
        print(f"{self.nome} equipou a arma: {arma.nome}")

    def usar_arma(self):
        if self.arma:
            print(self.arma.atacar())
        else:
             print(f"{self.nome} não tem uma arma equipada.")

        
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


espada = Espada("Espada Flamejante")
arco = Arco("Arco Élfico")

jogador = Jogador("Arthur", 100)
inimigo = Inimigo("Goblin", 30, 5)

jogador.equipar_arma(espada)
jogador.usar_arma()  # Usa a arma equipada

jogador.equipar_arma(arco)
jogador.usar_arma()

jogador.atacar(inimigo)  # Ataca normalmente (sem arma)
