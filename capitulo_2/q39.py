# Arquivo capitulo_2/q39.py
import random

class Pontuacao:
    def __init__(self, pontos = 0):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        print(f"Adicionando {valor} pontos...")
        
    def mostrar_pontos(self):
        return f"Pontos: {self.__pontos}"

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

class JogoMultiplayer(Jogo):
    def __init__(self, dificuldade, turno):
        super().__init__(dificuldade, turno)
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado ao jogo.")

    def iniciar(self):
         # Agora o método iniciar() imprime uma mensagem personalizada indicando o início do jogo multiplayer.
        print("\n=== Iniciando Jogo Multiplayer ===")
        # Lista os jogadores conectados.
        print(f"Número de jogadores conectados: {len(self.jogadores)}")
        for jogador in self.jogadores:
            print(f"-> {jogador.nome} está pronto para o combate!")
        # Fornece uma mensagem de “Boa sorte”.
        print("Boa sorte a todos!\n")

    def iniciar_combate_multiplayer(self, inimigo):
        self.iniciar()
        while any(j.energia > 0 for j in self.jogadores) and inimigo.vida > 0:
            print(f"\n--- Turno {self.turno} ---")

            for jogador in self.jogadores:
                if jogador.energia > 0:
                    jogador.atacar(inimigo)
                    if inimigo.vida <= 0:
                        print(f"O inimigo foi derrotado por {jogador.nome}!")
                        return

            self.turno += 1


jogador1 = Jogador("Irmão do Jorel", 100)
jogador2 = Jogador("Lara Croft", 100)
# Criando inimigo
inimigo = Inimigo("Goblin Rei", 150, 15)

# Criando instância do jogo multiplayer
jogo = JogoMultiplayer(dificuldade=2, turno=1)

# Adicionando jogadores
jogo.adicionar_jogador(jogador1)
jogo.adicionar_jogador(jogador2)

# Iniciando combate multiplayer
jogo.iniciar_combate_multiplayer(inimigo)
