import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0
        self.energia = 100  # Adicionado para compatibilidade com ataque do Inimigo

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor tem que estar entre 0 e 100.")

    def falar(self):
        print(f"Meu nome é {self.nome}")

    def tomar_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            print(f"{self.nome} foi derrotado")
        else:
            print(f"{self.nome} tomou {dano} de dano e tem {self.__vida} de vida restante!")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca

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
        print(f"{self.nome} atacou com {self.forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
        print(f"Energia do Jogador: {alvo.energia}")


class Jogo:
    def __init__(self, dificuldade, turno, nome_jogador, vida_jogador, nome_inimigo, vida_inimigo, forca_inimigo):
        self.__dificuldade = dificuldade
        self.turno = turno
        # Composição: o jogo possui os objetos
        self.__personagem = Personagem(nome_jogador, vida_jogador)
        self.__inimigo = Inimigo(nome_inimigo, vida_inimigo, forca_inimigo)

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

    def iniciar_combate(self):
        self.iniciar()
        while self.__personagem.energia > 0 and self.__inimigo.vida > 0:
            print(f"\n--- Turno {self.turno} ---")
            self.__personagem.atacar(self.__inimigo)
            if self.__inimigo.vida <= 0:
                print(f"{self.__personagem.nome} venceu a batalha!")
                break

            self.__inimigo.atacar(self.__personagem)
            if self.__personagem.energia <= 0:
                print("O inimigo venceu a batalha!")
                break

            self.turno += 1

jogo = Jogo(
    dificuldade=2,
    turno=1,
    nome_jogador="Arus",
    vida_jogador=100,
    nome_inimigo="Goblin",
    vida_inimigo=80,
    forca_inimigo=15
)

jogo.iniciar_combate()

"""
# Jogo compõe os objetos Personagem e Inimigo: eles são criadas dentro do Jogo e não existem fora 
  dele.

# Quando o objeto jogo é destruído, os objetos internos (__personagem e __inimigo) também são.

# Isso garante que o combate só exista dentro do sistema de jogo.
"""