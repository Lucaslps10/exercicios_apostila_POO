# Arquivo capitulo_3/q60.py

# Etapas para a solução:

# Adicionar o atributo preco à classe Item e às suas subclasses.

# Modificar os métodos de listagem e venda para considerar esse preço.

# Criar o método de classe ajustar_preco_itens na classe Loja.

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco  # Novo atributo

    def efeito(self, alvo):
         raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    

class Pocao(Item):
    def __init__(self, nome, cura, preco):
        super().__init__(nome, preco)
        self.cura = cura

    def usar(self, alvo):
        alvo.vida += self.cura
        print(f"{alvo.nome} usou {self.nome} e recuperou {self.cura} pontos de vida.")


class Equipamento(Item):
    def __init__(self, nome, bonus_defesa, preco):
        super().__init__(nome, preco)
        self.bonus_defesa = bonus_defesa

    def usar(self, alvo):
        alvo.defesa += self.bonus_defesa
        print(f"{alvo.nome} equipou {self.nome} e ganhou {self.bonus_defesa} pontos de defesa.")


class Loja:
    def __init__(self, nome, itens_disponiveis):
        self.nome = nome
        self.itens_disponiveis = itens_disponiveis

    def adicionar_item(self, item):
        self.itens_disponiveis.append(item)
        print(f"Item '{item.nome}' adicionado à loja {self.nome}.")

    def listar_itens(self):
        print(f"Itens disponíveis na loja {self.nome}:")
        for item in self.itens_disponiveis:
            print(f"- {item.nome} | Preço: {item.preco:.2f}")

    def vender_item(self, item_nome, jogador):
        for item in self.itens_disponiveis:
            if item.nome == item_nome:
                print(f"{jogador.nome} comprou {item.nome} por {item.preco:.2f}")
                jogador.inventario.append(item)
                return
        print(f"Item '{item_nome}' não encontrado na loja.")

    @classmethod
    def ajustar_preco_itens(cls, lojas, fator):
        for loja in lojas:
            for item in loja.itens_disponiveis:
                item.preco *= fator
        print(f"Preços ajustados em todas as lojas com fator {fator:.2f}.")
    """
    O que ele faz exatamente:
    1. Recebe uma lista de lojas (lojas) e um fator de ajuste (fator).

    2. Para cada loja na lista:

        Ele percorre todos os itens disponíveis nessa loja.

        Multiplica o preço atual de cada item pelo fator.

    3. Exibe uma mensagem informando que os preços foram ajustados.
    """

class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa
        self.inventario = []

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
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor tem que estar entre 0 e 100.")

# Criando itens
pocao_vida = Pocao("Poção de Vida", 50, 20.0)
armadura = Equipamento("Armadura de Couro", 10, 100.0)
espada = Equipamento("Espada Longa", 15, 150.0)

# Criando loja
loja_aventura = Loja("<< Loja da Aventura >>", [pocao_vida])
loja_aventura.adicionar_item(armadura)
loja_aventura.adicionar_item(espada)

# Criando jogador
jogador1 = Personagem("Eldon", 80, 30)

# Listar itens antes do ajuste
loja_aventura.listar_itens()

# Ajustar preços de todas as lojas (nesse caso, uma só)
Loja.ajustar_preco_itens([loja_aventura], 1.10)

# Listar itens após o ajuste
loja_aventura.listar_itens()

