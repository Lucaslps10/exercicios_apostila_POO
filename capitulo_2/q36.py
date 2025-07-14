# Arquivo capitulo_2/q36.py

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0


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
        if valor >= 0 and valor <= 100:
            self.__defesa = valor
           
        else:
            print("Valor tem que estar entre 0 e 100.")
        


class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, alvo):
        print(f"{self.nome} não pode atacar {alvo.nome}!")

    def falar(self):
        print(f"Meu nome é {self.nome} e eu não posso atacar!")

npc = NPC("Cell", 100)
p = Personagem("Jales", 100)
npc.falar()
npc.atacar(p)
print(npc.vida)