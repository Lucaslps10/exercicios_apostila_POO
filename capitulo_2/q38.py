# Arquivo capitulo_2/q38.py
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
    def __init__(self,nome, energia, pontuacao = Pontuacao()):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = pontuacao

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


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
            return True
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")
            return False
    
    # Mostrando a força do ataque sem acesso direto a força
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com {self.forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
        print(f"Energia do Jogador: {alvo.energia}")

class JogadorPremium(Jogador):
   
    def __init__(self, nome, energia, bonus=5, multiplicador=2):
        super().__init__(nome, energia)
        self.bonus = bonus  # Pontos extras por vitória
        self.multiplicador = multiplicador

    def adicionar_pontos(self, valor):
        valor_com_multiplicador = valor*self.multiplicador
        print(f"{self.nome} recebeu {valor_com_multiplicador} pontos (multiplicador aplicado).")
        self.pontuacao.adicionar_pontos(valor_com_multiplicador)

    def atacar(self, oponente):
        if self.energia < 10:
            print("Energia insuficiente para atacar, descanse primeiro...")
            self.descansar()
            return

        dano = random.randint(5, 20)
        print(f"Jogador Premium atacou {oponente.nome} e causou {dano} de dano!")

        self.energia -= 10
        print(f"Energia restante: {self.energia}")

        derrotado = oponente.tomar_dano(dano)
        if derrotado:
            print(f"{self.nome} derrotou {oponente.nome} e recebeu pontos com bônus!")
            self.adicionar_pontos(10 + self.bonus)
    

jp = JogadorPremium("Super boy", 50)
i = Inimigo("Chan", 5, 10)
print("Pontuação inicial: ", jp.pontuacao.mostrar_pontos())
jp.adicionar_pontos(10)
print("Pontos: ", jp.pontuacao.mostrar_pontos())
jp.atacar(i)