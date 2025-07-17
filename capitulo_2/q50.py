# Arquivo capitulo_2/q50.py

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


class Equipamento(Item):
    def __init__(self, nome, bonus_defesa):
        super().__init__(nome)
        self.bonus_defesa = bonus_defesa

    def usar(self, alvo):
        alvo.defesa += self.bonus_defesa
        print(f"{alvo.nome} equipou {self.nome} e ganhou {self.bonus_defesa} pontos de defesa.")


class Inventario:
    def __init__(self):
        self.itens = []  # Composição: o inventário contém os itens
                         # Os itens são objetos das classes Poção e Equipamento

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item.nome} foi adicionado ao inventário.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item.nome} foi removido do inventário.")
        else:
            print("Item não encontrado no inventário.")

    # Método a ser usado futuramente na classe personagem
    def usar_item(self, nome_item, alvo):
        for item in self.itens:
            if item.nome == nome_item:
                item.usar(alvo)
                self.itens.remove(item)  # Consome o item
                return
        print("Item não encontrado.")


inventario = Inventario()

# Criando alguns itens
pocao = Pocao("Poção de Vida", 30)
escudo = Equipamento("Escudo de Madeira", 10)

# Adicionando itens ao inventário
inventario.adicionar_item(pocao)
inventario.adicionar_item(escudo)
