# Arquivo capitulo_2/q54.py

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
        self.aliado = None  # Associação com um aliado
        # Isso é uma associação porque o Aliado é criado fora da classe Jogador, e o jogador apenas 
        # recebe a referência.
        # A instância de Aliado não depende da vida do Jogador.
        
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

    def definir_aliado(self, aliado):
        self.aliado = aliado
        print(f"{aliado.nome} agora está acompanhando {self.nome} na aventura!")

    def exibir_aliado(self):
        if self.aliado:
            print(f"Aliado: {self.aliado.apresentar()}")
        else:
            print("Nenhum aliado está acompanhando este jogador.")

    def usar_habilidade_aliado(self):
        if self.aliado:
            print(self.aliado.habilidade_especial())
        else:
            print("Este jogador não possui um aliado para usar habilidades.")


class Aliado:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def apresentar(self):
        return f"{self.nome} - Tipo: {self.tipo}"
    
    def habilidade_especial(self):
        raise NotImplementedError("Subclasses devem implementar este método.")

class Mago(Aliado):
    def __init__(self, nome, tipo, mana):
        super().__init__(nome, tipo)
        self.mana = mana

    def habilidade_especial(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.nome} lançou uma bola de fogo! (Mana restante: {self.mana})"
        else:
            return f"{self.nome} está sem mana suficiente para lançar magia."

class Guerreiro(Aliado):
    def __init__(self, nome, tipo, energia):
        super().__init__(nome, tipo)
        self.energia = energia

    def habilidade_especial(self):
        if self.energia >= 5:
            self.energia -= 5
            return f"{self.nome} executa um Golpe Poderoso com a espada justiceira! (Energia restante: {self.energia})"
        else:
            return f"{self.nome} está cansado e não consegue usar o golpe especial."
        
j1 = Jogador("Arthur", 80)
m1 = Mago("Merlin", "Mago", 50)

j1.definir_aliado(m1)
j1.exibir_aliado()
j1.usar_habilidade_aliado()
j1.usar_habilidade_aliado()

