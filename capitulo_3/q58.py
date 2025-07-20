# Arquivo capitulo_3/q58.py

class Jogo:
    dificuldade_global = 1  # Atributo de classe (valor padrão)

    def __init__(self, dificuldade=None, turno=1):
        # Usa a dificuldade_global se nenhuma dificuldade for passada
        if dificuldade in [1, 2, 3]:
            self.__dificuldade = dificuldade
        else:
            self.__dificuldade = Jogo.dificuldade_global
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

    @classmethod
    def definir_dificuldade_global(cls, valor):
        if valor in [1, 2, 3]:
            cls.dificuldade_global = valor
            print(f"Dificuldade global definida para {valor}")
        else:
            print("Dificuldade global inválida. Use 1, 2 ou 3.")

    @classmethod
    def obter_dificuldade_global(cls):
        return cls.dificuldade_global

    def iniciar(self):
        print("O jogo começou!")

    def iniciar_combate(self, guerreiro, inimigo):
        self.iniciar()
        while guerreiro.energia > 0 and inimigo.vida > 0:
            print(f"\n--- Turno {self.turno} ---")
            guerreiro.atacar(inimigo)
            if inimigo.vida <= 0:
                print("PersonagemDois venceu a batalha!")
                break

            inimigo.atacar(guerreiro)
            if guerreiro.energia <= 0:
                print("O inimigo venceu a batalha!")
                break

            self.turno += 1

Jogo.definir_dificuldade_global(3) # Padrão

jogo1 = Jogo()  # Vai usar dificuldade_global (3)
jogo2 = Jogo(2)  # Vai usar dificuldade própria (2)

print(jogo1.dificuldade)  # Dificuldade: 3
print(jogo2.dificuldade)  # Dificuldade: 2
