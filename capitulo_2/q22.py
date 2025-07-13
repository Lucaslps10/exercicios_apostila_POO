# Arquivo capitulo_2/q21.py

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
        


p = Personagem("Sky", 100)
print(p.nome)
print(p.vida)
print(p.defesa)



