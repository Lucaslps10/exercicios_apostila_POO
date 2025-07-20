# Arquivo capitulo_3/q59.py

# Arquivo capitulo_2/q21.py

import random;

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        self.__vida = valor
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        if valor >= 0 and valor <= 100:
            self.__defesa = valor
           
        else:
            print("Valor tem que estar entre 0 e 100.")
    
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

    @staticmethod
    def calcular_dano_base(forca):
        return forca * 1.5
    
    # Esse método serve para padronizar o cálculo de dano de ataque, com base em um atributo 
    # (como a força), sem precisar de uma instância do personagem.

personagem = Personagem("Gasparzinho", 100)
print(personagem.nome)
print(personagem.vida)
print(personagem.defesa)
personagem.falar()

dano_base = Personagem.calcular_dano_base(10)
print(f"Dano base com força 10: {dano_base}")




