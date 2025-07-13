# Arquivo capitulo_2/q18.py

import random;
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
    
    @property
    def vida(self):
        return f"{self.nome} tem {self.__vida} pontos de vida."
    
    def falar(self):
        print(f"Meu nome é {self.nome}")
    
    def tomar_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            print(f"{self.nome} foi derrotado")

        else:
            print(f"{self.nome} tomou {dano} de dano e tem {self.__vida} de vida restante!")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)

personagem = Personagem("Gasparzinho", 100)
print(personagem.vida)
personagem.falar()