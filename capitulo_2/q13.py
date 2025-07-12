# Arquivo capitulo_2/q13.py
import random

class Jogador:
    def __init__(self):
        self.energia = 100
        self.pontuacao = Pontuacao()

    def atacar(self, inimigo):
        if self.energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {inimigo.nome} e causou {dano} de dano!")

        self.energia -= 10
        print(f"Energia restante: {self.energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.energia + 20 > 100:
            recuperado = 100 - self.energia
        else:
            recuperado = 20
        self.energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor
        print(f"Você tem {self.pontos} pontos!")

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

########################### Criando um Sistema de Menu Interativo ####################################

class Menu:
    def exibir(self):
        while True:
            print("\n###### MENU ######")
            print("1. Iniciar Jogo")
            print("2. Mostrar Opções")
            print("3. Sair")
            opcao_escolhida = input("Escolha uma opção: ")

            if opcao_escolhida == "1":
                self.iniciar_jogo()
            elif opcao_escolhida == "2":
                self.mostrar_opcoes()
            elif opcao_escolhida == "3":
                print("Saindo do jogo. Bye bye!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def mostrar_opcoes(self):
        print("\nOpções do jogo: ")
        print("# Cada ataque gasta 10 pontos de energia.")
        print("# Descansar recupera 20 pontos de energia (máximo 100)")
        print("# Cada inimigo derrotado vale 10 pontos.")

    def iniciar_jogo(self):
        jogador = Jogador()
        nome_dos_inimigos = ["Freeza", "Majin-Boo", "Dabura", "Baby", "Cell"]
        num_inimigos = random.randint(1, 3)
        inimigos = [Inimigo(random.choice(nome_dos_inimigos), 100) for _ in range(num_inimigos)]

        print(f"\nIniciando o jogo com {num_inimigos} inimigo(s)!")

        turnos_restantes = 10

        for inimigo in inimigos:
            print(f"\nLutando contra {inimigo.nome}")
            while inimigo.vida > 0:
                jogador.atacar(inimigo)
                turnos_restantes -= 1
                if inimigo.vida <= 0:
                    break
                if jogador.energia < 10:
                    jogador.descansar()
                    turnos_restantes -= 1
            if turnos_restantes <= 0:
                break

        print("\nFim da partida!!!")
        print(f"Pontuação final: {jogador.pontuacao.pontos}")
        if jogador.pontuacao.pontos == num_inimigos * 10:
            print("Parabéns! Você conseguiu vencer todos os inimigos!")
        else:
            print("Você sobreviveu, mas não conseguiu vencer todos os inimigos.")

#Inicia o menu

menu = Menu()
menu.exibir()

