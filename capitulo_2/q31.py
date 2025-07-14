# Arquivo capitulo_2/q31.py

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
        return f"{self.nome} realiza um corte poderoso! e causa {dano} de dano!"
    
class Arco(Arma):
    def __init__(self, nome):
        super().__init__(nome)

    def atacar(self):
        dano = random.randint(5, 15)
        return f"{self.nome} dispara uma flecha à distância e causa {dano} de dano!"

espada = Espada("Espada Lendária")
arco = Arco("Arco Insano")

print(espada.atacar())
print(arco.atacar())