# Arquivo capitulo_2/q44.py

# Classe base Mago
class Mago:
    def __init__(self, nome, mana):
        self.nome = nome
        self.mana = mana

    def conjurar(self):
        print(f"{self.nome} está canalizando energia mágica...")

# Classe MagiaElemental
class MagiaElemental:
    def lancar_magia(self, elemento):
        if elemento.lower() == "fogo":
            print("Uma bola de fogo incendeia o inimigo!")

        elif elemento.lower() == "água" or elemento.lower() == "agua":
            print("Um jato de água atinge com força!")

        elif elemento.lower() == "terra":
            print("Rochas se erguem do chão em um ataque poderoso!")

        elif elemento.lower() == "ar":
            print("Uma rajada de vento empurra tudo à frente!")
        else:
            print("Esse elemento não é conhecido...")

# Classe MagoElemental que herda de Mago e MagiaElemental
class MagoElemental(Mago, MagiaElemental):
    def __init__(self, nome, mana):
        super().__init__(nome, mana)

    def usar_magia_elemental(self, elemento):
        if self.mana >= 10:
            print(f"{self.nome} lança uma magia elemental de {elemento}!")
            self.lancar_magia(elemento)
            self.mana -= 10
        else:
            print(f"{self.nome} não tem mana suficiente para lançar magia!")

# Exemplo de uso
mago = MagoElemental("\nMerlim", 50)
mago.conjurar()
mago.usar_magia_elemental("fogo")
mago.usar_magia_elemental("água")
mago.usar_magia_elemental("terra")
mago.usar_magia_elemental("ar")
mago.usar_magia_elemental("vento")  # Elemento não reconhecido
