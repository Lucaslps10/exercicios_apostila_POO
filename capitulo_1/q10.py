# Arquivo capitulo_1/q10.py

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        

    def atacar(self, alvo):
        print(f"{self.nome} atacou!")
        alvo.tomar_dano(10)

class PersonagemDois:
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if dano > 0 and self.vida > 0:
            print(f"Dano: {dano} Vida restante: {self.vida}")
        else:
            print("Game Over")
            
guerreiro = PersonagemDois()
inimigo = Inimigo("Morte", 100)
inimigo.atacar(guerreiro)
