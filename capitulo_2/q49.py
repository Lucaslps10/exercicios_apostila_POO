# Arquivo capitulo_2/q49.py

# Classe base

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.__forca = 15

    def __str__(self):
        return f"{self.nome} (Força: {self.forca}, Vida: {self.vida})"

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
   


class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
        self.inimigos = []  # Composição: a fase tem um conjunto de inimigos
        # Aqui, a Fase possui um conjunto de inimigos (self.inimigos), 
        # que são objetos da classe Inimigo.

    def descricao(self):
        return f"\nFase: {self.nome}, Dificuldade: {self.dificuldade}\n"

    def ambiente(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def gerar_inimigos(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


# Subclasse FaseFloresta
class FaseFloresta(Fase):
    def __init__(self, dificuldade):
        super().__init__("Floresta Encantada", dificuldade)
        self.criaturas = ["unicórnios", "ogros", "trolls"]
        self.clima = "úmido e chuvoso"
        self.gerar_inimigos()  # Cria os inimigos ao instanciar a fase

        # A linha self.gerar_inimigos() chama o método que cria os inimigos logo na criação da fase,
        #  por isso os inimigos já existem assim que você instancia os objetos.

    def ambiente(self):
        return f"Ambiente de floresta com clima {self.clima} e criaturas como {', '.join(self.criaturas)}."

    def gerar_inimigos(self):
        nomes = ["Goblin da Névoa", "Lobo Fantasma", "Espírito da Árvore"]
        self.inimigos = [Inimigo(nome) for nome in nomes]
        # Isso cria objetos da classe Inimigo e os coloca na lista self.inimigos.


# Subclasse FaseDeserto
class FaseDeserto(Fase):
    def __init__(self, dificuldade):
        super().__init__("Deserto Escaldante", dificuldade)
        self.perigos = ["tempestade de areia", "calor extremo"]
        self.oasis = True
        self.gerar_inimigos()

    def ambiente(self):
        oasis_info = "com oásis disponível" if self.oasis else "sem oásis"
        return f"Ambiente de deserto com perigos como {', '.join(self.perigos)}, {oasis_info}."

    def gerar_inimigos(self):
        nomes = ["Escorpião Gigante", "Múmia do Deserto", "Serpente de Areia"]
        self.inimigos = [Inimigo(nome) for nome in nomes]


# Exemplo de uso
fase1 = FaseFloresta("Média")
fase2 = FaseDeserto("Alta")

print(fase1.descricao())
print(fase1.ambiente())
print("\nInimigos da fase 1:\n")
for inimigo in fase1.inimigos:
    print("-", inimigo)

print(fase2.descricao())
print(fase2.ambiente())
print("\nInimigos da fase 2:\n")
for inimigo in fase2.inimigos:
    print("-", inimigo)
