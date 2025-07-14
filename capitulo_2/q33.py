# Arquivo capitulo_2/q33.py


class Item:
    def __init__(self, nome):
        self.nome = nome

    def efeito(self, alvo):
         raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    

class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome)
        self.cura = cura

    def usar(self, alvo):
        alvo.vida += self.cura
        print(f"{alvo.nome} usou {self.nome} e recuperou {self.cura} pontos de vida.")

# Subclasse Equipamento
class Equipamento(Item):
    def __init__(self, nome, bonus_defesa):
        super().__init__(nome)
        self.bonus_defesa = bonus_defesa

    def usar(self, alvo):
        alvo.defesa += self.bonus_defesa
        print(f"{alvo.nome} equipou {self.nome} e ganhou {self.bonus_defesa} pontos de defesa.")

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

p1 = Personagem("Perseu", 40)
pocao_cura = Pocao("Poção de Vida", 50)
escudo = Equipamento("Escudo", 20)


# Usando os itens
pocao_cura.usar(p1)
escudo.usar(p1)

print(p1.nome)
print(p1.vida)
print(p1.defesa)