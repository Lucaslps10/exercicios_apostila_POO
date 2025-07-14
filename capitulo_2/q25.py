# Arquivo capitulo_2/q25.py
import random

class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, valor):
        if valor < 0:
            raise ValueError("A pontuação não pode ser negativa.") # O raise é usado para gerar uma excessão
        self.__pontos = valor
        
class Jogador:
    def __init__(self, nome, energia, pontuacao=None):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = pontuacao if pontuacao else Pontuacao()
        # Dentro do método, é feita uma verificação:
        # Se o usuário passar uma pontuação, ela será usada.
        # Caso contrário (pontuacao == None), será criada uma nova instância de Pontuacao().
        # Agora se for criado mais de um objeto jogador, a pontoação é diferente.


    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if valor < 0:
            self.__energia = 0
        else:
            self.__energia = valor

            
    def atacar(self, inimigo):
        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeiro...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {inimigo.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.__energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        if self.__energia < valor:
            print("Sem energia suficiente!")
        else:
            self.__energia -= valor
            print(f"Energia usada: {valor} Restante: {self.energia}")
        
    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = valor

        self.__energia += recuperado
        print(f"Jogador recuperou {recuperado} de energia. Energia atual: {self.__energia}")

    

    

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
    
    # Mostrando a força do ataque sem acesso direto a força
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com {self.forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
        print(f"Energia do Jogador: {alvo.energia}")

      


class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir(self):
        while True:
            print(self.titulo)
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
        print("Cada ataque gasta 10 pontos de energia.")
        print("Descansar recupera 20 pontos de energia (máximo 100)")
        print("Cada inimigo derrotado vale 10 pontos.")

    def iniciar_jogo(self):
        jogador1 = Jogador("Super Mário", 100)
        nome_dos_inimigos = ["Freeza", "Majin-Boo", "Dabura", "Baby", "Cell"]
        num_inimigos = random.randint(1, 3)
        inimigos = [Inimigo(random.choice(nome_dos_inimigos), 100, 10) for _ in range(num_inimigos)]

        print(f"\nIniciando o jogo com {num_inimigos} inimigo(s)!")

        turnos_restantes = 10

        for i in inimigos:
            print(f"\nLutando contra {i.nome}")
            while i.vida > 0:
                jogador1.atacar(i)
                i.atacar(jogador1)

                turnos_restantes -= 1
                if i.vida <= 0:
                    break
                if jogador1.energia < 10:
                    jogador1.descansar()
                    turnos_restantes -= 1
            if turnos_restantes <= 0:
                break

        print("\nFim da partida!!!")
        print(f"Pontuação final: {jogador1.pontuacao.pontos}")
        if jogador1.pontuacao.pontos == num_inimigos * 10:
            print("Parabéns! Você conseguiu vencer todos os inimigos!")
        else:
            print("Você sobreviveu, mas não conseguiu vencer todos os inimigos.")

#Inicia o menu

menu = Menu("\n########## ---Menu--- ############")
menu.exibir()