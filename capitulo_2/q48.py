# Arquivo capitulo_2/q48.py

import random

class Pontuacao:
    def __init__(self, pontos=0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor

    def mostrar_pontos(self):
        return self.__pontos

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor < 0:
            raise ValueError("A pontuação não pode ser negativa.")
        self.__pontos = valor


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, valor):
        if 5 <= valor <= 20:
            self.__forca = valor
        else:
            print("A força deve ser entre 5 e 20!")

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
        print(f"{self.nome} atacou com {self.__forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
            print(f"Energia de {alvo.nome} acabou.")
        print(f"Energia do Jogador: {alvo.energia}")


class Jogador:
    def __init__(self, nome, energia):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = Pontuacao()

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        self.__energia = valor

    def adicionar_pontos(self, valor):
        self.pontuacao.adicionar_pontos(valor)

    def atacar(self, oponente):
        if self.__energia < 10:
            print("Energia insuficiente para atacar. Descansando...")
            self.descansar()
            return

        dano = random.randint(5, 20)
        print(f"Jogador atacou {oponente.nome} e causou {dano} de dano!")
        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        if oponente.tomar_dano(dano):
            self.pontuacao.adicionar_pontos(10)

    def descansar(self):
        recuperado = min(20, 100 - self.__energia)
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        self.__energia -= valor
        if self.__energia < 0:
            self.__energia = 0
            print("Sem energia suficiente!")
        print(f"Energia usada: {valor}. Restante: {self.__energia}")

    def recuperar_energia(self, valor):
        recuperado = min(valor, 100 - self.__energia)
        self.__energia += recuperado
        print(f"Jogador recuperou {recuperado} de energia. Energia atual: {self.__energia}")


class Menu:
    def __init__(self, jogo):
        self.jogo = jogo

    def exibir(self):
        while True:
            print("\n########## MENU ##########")
            print("1. Iniciar Jogo")
            print("2. Mostrar Opções")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogo.iniciar_partida()
            elif opcao == "2":
                self.mostrar_opcoes()
            elif opcao == "3":
                print("Saindo do jogo. Bye bye!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def mostrar_opcoes(self):
        print("\nOpções do jogo: ")
        print("• Cada ataque gasta 10 pontos de energia.")
        print("• Descansar recupera até 20 pontos de energia (máximo 100).")
        print("• Cada inimigo derrotado vale 10 pontos.")


class Jogo:
    def __init__(self, dificuldade, turno=1):
        self.__dificuldade = dificuldade
        self.turno = turno
        self.menu = Menu(self)  # Composição: Jogo cria e controla o Menu  <----------

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor
        else:
            print("Dificuldade deve ser 1 (fácil), 2 (médio) ou 3 (difícil).")

    def iniciar(self):
        print("O jogo começou!")

    def iniciar_partida(self):
        jogador = Jogador("Super Mário", 100)
        nomes = ["Freeza", "Majin-Boo", "Dabura", "Baby", "Cell"]
        num_inimigos = random.randint(1, 3)
        inimigos = [Inimigo(random.choice(nomes), 100, 10) for _ in range(num_inimigos)]

        print(f"\nIniciando o jogo com {num_inimigos} inimigo(s)!")
        turnos = 10

        for inimigo in inimigos:
            print(f"\nLutando contra {inimigo.nome}")
            while inimigo.vida > 0:
                jogador.atacar(inimigo)
                turnos -= 1
                if inimigo.vida <= 0:
                    break
                if jogador.energia < 10:
                    jogador.descansar()
                    turnos -= 1
                if turnos <= 0:
                    break

        print("\nFim da partida!!!")
        print(f"Pontuação final: {jogador.pontuacao.pontos}")
        if jogador.pontuacao.pontos == num_inimigos * 10:
            print("Parabéns! Você venceu todos os inimigos!")
        else:
            print("Você sobreviveu, mas não venceu todos os inimigos.")

    def iniciar_menu(self):
        self.menu.exibir()


# Criar e iniciar o jogo com o menu
jogo = Jogo(dificuldade=1)
jogo.iniciar_menu()
