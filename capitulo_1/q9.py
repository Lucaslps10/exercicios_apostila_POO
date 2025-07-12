# Arquivo capitulo_1/q9.py

class Jogador:
    def __init__(self):
        self.energia = 50

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Aumentou {quantidade} de energia; Energia = {self.energia}")
        

    def usar_energia(self, quantidade):
        self.energia -= quantidade
        if self.energia <= 0:
            self.energia = 0
            print("Sem energia suficiente!")
        else:
            print(f"Energia usada: {quantidade} Restante: {self.energia}")
            

jogador = Jogador()
jogador.usar_energia(60)
jogador.recuperar_energia(20)
