# Arquivo capitulo_2/q12.py
import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.pontuacao = Pontuacao()

    def atacar(self, inimigo):
        if self.energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

        self.energia -= 10
        print(f"Energia restante: {self.energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.energia + 20 > 100:
            recuperado = 100 - self.energia
        else:
            recuperado = 20
        self.energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor
        print(f"Você tem {self.pontos} pontos!")

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

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
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)
  
        
jogador = Jogador("Meliodas")
inimigo = Inimigo("Bárbaro", 100)

inimigos = [Inimigo("Bárbaro", 100), Inimigo("Giagante", 100), Inimigo("Bruxa", 100)]

# Loop para testar o sistema

for inimigo in inimigos:
    print(f"\nLutando contra {inimigo.nome}")
    while inimigo.vida > 0:
        jogador.atacar(inimigo)

print(f"\nJogo encerrado. Pontuação final: {jogador.pontuacao.pontos}")


