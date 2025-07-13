# Arquivo capitulo_2/q20.py

class Jogo:
    def __init__(self, dificuldade, turno):
        self.__dificuldade = dificuldade
        self.turno = turno

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor

        else:
            print("Só há três níveis de dificuldade: 1, 2, 3;")


    def iniciar(self):
        print("O jogo começou!")
    
    def iniciar_combate(self, guerreiro, inimigo):
        self.iniciar()
        while guerreiro.energia > 0 and inimigo.vida > 0:
            print(f"/n--- Turno {self.turno} ---")
            guerreiro.atacar(inimigo)
            if inimigo.vida <= 0:
                print("PersonagemDois venceu a batalha!")
                break

            inimigo.atacar(guerreiro)
            if guerreiro.energia <= 0:
                print("O inimigo venceu a batalha!")
                break
    
            self.turno += 1

        
jogo1 = Jogo(2, 1) # O primeiro parâmetro é o número de turnos e o segundo a dificuldade.

print(jogo1.dificuldade)
        
jogo2 = Jogo(1, 1)
print(jogo2.dificuldade)

jogo2.dificuldade = 3
print(jogo2.dificuldade)


jogo2.dificuldade = 5
print(jogo2.dificuldade)

