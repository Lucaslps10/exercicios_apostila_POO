# Arquivo capitulo_1/q6.py

class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        print(f"Meu nome é {self.nome}!")

p = Personagem("Lucas")
p.dizer_nome()