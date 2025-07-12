# Arquivo capitulo_1/q8.py

class PersonagemDois:
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if dano > 0 and self.vida > 0:
            print(f"Dano: {dano} Vida restante: {self.vida}")
        else:
            print("Game Over")

pdois = PersonagemDois()
pdois.tomar_dano(10)
pdois.tomar_dano(5)
pdois.tomar_dano(10)
pdois.tomar_dano(10)
pdois.tomar_dano(65)