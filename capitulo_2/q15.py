# Arquivo capitulo_2/q15.py
class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        print(f"Adicionando {valor} pontos...")
        
    def mostrar_pontos(self):
        return f"Pontos: {self.__pontos}"
    

pontuacao = Pontuacao()
print(pontuacao.mostrar_pontos())
pontuacao.adicionar_pontos(10)
print(pontuacao.mostrar_pontos())
