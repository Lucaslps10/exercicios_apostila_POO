# Arquivo capitulo_2/q11.py
import random;
class PersonagemDois:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado")

        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)

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

class Jogo:
    def __init__(self, turno):
        self.turno = turno

    def iniciar(self):
        print("O jogo começou!")
    
    def iniciar_combate(self, guerreiro, inimigo):
        self.iniciar()
        while guerreiro.vida > 0 and inimigo.vida > 0:
            print(f"/n--- Turno {self.turno} ---")
            guerreiro.atacar(inimigo)
            if inimigo.vida <= 0:
                print(f"{guerreiro.nome} venceu a batalha!")
                break

            inimigo.atacar(guerreiro)
            if guerreiro.vida <= 0:
                print(f"{inimigo.nome} venceu a batalha!")
                break
    
            self.turno += 1

guerreiro = PersonagemDois("Guerreiro", 100)
inimigo = Inimigo("Inimigo", 100)
jogo = Jogo(1)
jogo.iniciar_combate(guerreiro, inimigo)