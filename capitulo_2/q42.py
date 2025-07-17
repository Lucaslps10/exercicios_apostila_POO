# Arquivo capitulo_2/q42.py

import random

class Voador:
    def voar(self):
        print(f"{self.nome} está voando pelos céus com grandes asas!")

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

# Classe Dragao herda de Inimigo e Voador
class Dragao(Inimigo, Voador):
    def __init__(self, nome, vida, forca, cor):
        super().__init__(nome, vida, forca)
        self.cor = cor

    def rugir(self):
        print(f"{self.nome} solta um rugido aterrorizante!")


class Jogador:
    def __init__(self, nome, energia):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = Pontuacao()

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        self.__energia = valor
        
    def adicionar_pontos(self, valor):
        self.pontuacao.adicionar_pontos(valor)

    def atacar(self, oponente):

        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {oponente.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = oponente.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        self.__energia -= valor
        print(f"Energia usada: {valor} Restante: {self.energia}")
        if self.__energia < 0:
            self.__energia = 0
            print("Sem energia suficiente!")

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


# Exemplo de uso
jogador = Jogador("Super Mario", 200)
dragao = Dragao("Dragão branco de olhos azuis", 100, 15, "vermelho") # Dragão herda nome, vida e força de Inimigo
dragao.voar() # Dragão herda o método voar da classe Voador
dragao.rugir()
dragao.atacar(jogador) # Dragão herda o método atacar() de Inimigo
