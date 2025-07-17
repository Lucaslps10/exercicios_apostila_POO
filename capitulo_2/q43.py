# Arquivo capitulo_2/q43.py

import random

# Eu tranformei a classe Jogador na classe Guerreiro;
# Usei a classe inimigo para testar o ataque da classe paladino;
# A classe Pontuação armazena os pontos do guerreiro;


# Classe Curador
class Curador:
    def __init__(self, nome, poder_cura):
        self.nome = nome
        self.poder_cura = poder_cura

    def curar(self, aliado):
        energia_anterior = aliado.energia
        if aliado.energia + self.poder_cura > 100:
            recuperado = 100 - aliado.energia
            aliado.energia = 100
        else:
            recuperado = self.poder_cura
            aliado.energia += self.poder_cura
        print(f"{self.nome} curou {aliado.nome}, restaurando {recuperado} de energia!")
        print(f"-> Energia de {aliado.nome}: {energia_anterior} → {aliado.energia}")

# Classe Jogador tranformada em Classe Guerreiro
class Guerreiro:
    def __init__(self,nome, energia):
        self.nome = nome
        self.__energia = energia
        self.pontos = Pontuacao(0)

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if self.__energia >= 0:
            self.__energia = valor
            
    def atacar(self, inimigo):
        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeiro...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontos.adicionar_pontos(10)
        
    def descansar(self):
        if self.__energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        self.__energia -= valor
        if self.__energia < 0:
            print("Sem energia suficiente!")
        else:
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
    
    @forca.setter
    def forca(self, valor):
        if valor >=5 and valor <= 20:
            self.__forca = valor
        else:
            print("A força deve ser no mínimo 5 e no máximo 20!")


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

# Classe Pontuação
class Pontuacao:
    def __init__(self, pontos = 0):
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
            raise ValueError("A pontuação não pode ser negativa.") # O raise é usado para gerar uma excessão
        self.__pontos = valor

# Classe Paladino que herda de Guerreiro e Curador
class Paladino(Guerreiro, Curador):
    def __init__(self, nome, energia, poder_cura):
        Guerreiro.__init__(self, nome, energia)
        Curador.__init__(self, nome, poder_cura)
    

# Exemplo de uso
paladino = Paladino("Sir Lancelot", 100, poder_cura=15)
inimigo = Inimigo("Troll", 100, 15)
guerreiro = Guerreiro("Dartanhan", 60)

paladino.atacar(inimigo)
paladino.curar(guerreiro)

"""
Sistema de Combate com Herança Múltipla: Guerreiro, Curador e Paladino

Classes principais:

- Pontuacao: controla e armazena os pontos ganhos pelo jogador.
- Guerreiro: representa um personagem que pode atacar inimigos, descansar e gerenciar sua energia.
- Curador: representa um personagem com habilidade de curar aliados, restaurando a energia deles.
- Paladino: herda de Guerreiro e Curador, podendo tanto atacar quanto curar. Usa herança múltipla.
- Inimigo: representa um inimigo com vida e força que pode atacar e receber dano.

Funcionalidade:
- O Paladino pode atacar um inimigo, causando dano e ganhando pontos se o inimigo for derrotado.
- O Paladino também pode curar aliados (incluindo outros guerreiros), restaurando parte da energia deles.
- A energia é limitada a 100, e o sistema evita ultrapassar esse valor.
- Os ataques gastam energia do atacante, e o personagem pode descansar para recuperá-la.

Exemplo final:
Um Paladino chamado "Sir Lancelot" ataca um Troll e cura seu aliado "Dartanhan".

"""


