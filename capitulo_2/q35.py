# Arquivo capitulo_2/q35.py

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
        
aliado1 = Mago("Gandalf", "Épico", 30)
aliado2 = Guerreiro("Lion", "Raro", 20)

print(aliado1.apresentar())
print(aliado1.habilidade_especial())
print(aliado1.habilidade_especial())

print(aliado2.apresentar())
print(aliado2.habilidade_especial())



        