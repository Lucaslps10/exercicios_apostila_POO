# Arquivo capitulo_2/q52.py

# Classe base
class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

    def descricao(self):
        return f"Fase: {self.nome}, Dificuldade: {self.dificuldade}"

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

    def ambiente(self):
        return f"Ambiente de floresta com clima {self.clima} e criaturas como {', '.join(self.criaturas)}."

    def gerar_inimigos(self):
        return ["Goblin da Névoa", "Lobo Fantasma", "Espírito da Árvore\n"]

# Subclasse FaseDeserto
class FaseDeserto(Fase):
    def __init__(self, dificuldade):
        super().__init__("Deserto Escaldante", dificuldade)
        self.perigos = ["tempestade de areia", "calor extremo"]
        self.oasis = True

    def ambiente(self):
        oasis_info = "com oásis disponível" if self.oasis else "sem oásis"
        return f"Ambiente de deserto com perigos como {', '.join(self.perigos)}, {oasis_info}."

    def gerar_inimigos(self):
        return ["Escorpião Gigante", "Múmia do Deserto", "Serpente de Areia\n"]


# Classe com Agregação
class Mapa:
    def __init__(self, nome):
        self.nome = nome
        self.fases = []  # Lista de objetos Fase (ou subclasses)

    def adicionar_fase(self, fase):
        if isinstance(fase, Fase):
            self.fases.append(fase)
        else:
            raise TypeError("Somente instâncias de Fase podem ser adicionadas ao Mapa.")
        # A função isinstance() em Python serve para verificar se um objeto é uma instância de uma
        # determinada classe (ou de uma tupla de classes).
        # Isso garante que apenas objetos da classe Fase ou de suas subclasses 
        # (como FaseFloresta, FaseDeserto) possam ser adicionados ao mapa — protegendo seu código 
        # contra erros de tipo e uso incorreto.


    def exibir_fases(self):
        print(f"Mapa: {self.nome}")
        for fase in self.fases:
            print(f"- {fase.descricao()}")
            print(f"  Ambiente: {fase.ambiente()}")
            print(f"  Inimigos: {', '.join(fase.gerar_inimigos())}")
            # O método join funciona como um concatenador que junta as strings numa única linha
            # e usa um separador específico.

# Exemplo de uso
fase1 = FaseFloresta("Média")
fase2 = FaseDeserto("Alta")

meu_mapa = Mapa("Região Mística")
meu_mapa.adicionar_fase(fase1)
meu_mapa.adicionar_fase(fase2)

meu_mapa.exibir_fases()
