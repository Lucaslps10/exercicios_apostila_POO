# Arquivo capitulo_2/q53.py

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


class Loja:
    def __init__(self, nome, itens_disponiveis):
        self.nome = nome
        self.itens_disponiveis = itens_disponiveis  # Agregação: Lista de instâncias de Item

    def adicionar_item(self, item):
        self.itens_disponiveis.append(item)
        print(f"Item '{item.nome}' adicionado à loja {self.nome}.")


    def listar_itens(self):
        print(f"Itens disponíveis na loja {self.nome}:")
        for item in self.itens_disponiveis:
            print(f"- {item.nome}")

    def vender_item(self, item_nome, jogador):
        for item in self.itens_disponiveis:
            if item.nome == item_nome:
                print(f"{jogador.nome} comprou {item.nome}")
                jogador.inventario.append(item)
                return
        print(f"Item '{item_nome}' não encontrado na loja.")

class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa
        self.inventario = [] # Agragação: Aqui o jogador recebe os itens comprados;


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
        

# Criando itens
pocao_vida = Pocao("Poção de Vida", 50)
armadura = Equipamento("Armadura de Couro", 10)
espada = Equipamento("Espada Longa", 15)

# Criando loja
loja_aventura = Loja("<< Loja da Aventura >>", [pocao_vida])

# Adicionando item
loja_aventura.adicionar_item(armadura)
loja_aventura.adicionar_item(espada)

# Listando itens
loja_aventura.listar_itens()

# Criando jogador
jogador1 = Personagem("Eldon", 80, 30)

# Vendendo item
loja_aventura.vender_item("Espada Longa", jogador1)
loja_aventura.vender_item("Poção de Vida", jogador1)

# Usando item
for item in jogador1.inventario:
    item.usar(jogador1)

# Listando novamente
loja_aventura.listar_itens()

