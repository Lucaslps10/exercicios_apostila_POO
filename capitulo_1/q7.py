# Arquivo capitulo_1/q7.py

class Pontuacao:
    def __init__(self, pontos = 0):
        self.pontos = pontos

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
        print(f"Você ganhou {quantidade} pontos!")
        
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")

pontuacao = Pontuacao()
pontuacao.adicionar_pontos(50)
pontuacao.mostrar_pontos()