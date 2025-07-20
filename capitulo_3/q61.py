# Arquivo capitulo_3/q61.py

# Classe base
class Fase:
    tempo_maximo = 300  # em segundos, por exemplo

    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

    def descricao(self):
        return f"Fase: {self.nome}, Dificuldade: {self.dificuldade}, Tempo Máximo: {Fase.tempo_maximo} segundos"

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


# Exemplo de uso
fase1 = FaseFloresta("Média")
fase2 = FaseDeserto("Alta")

print(fase1.descricao())
print(fase1.ambiente())
print("Inimigos:", ", ".join(fase1.gerar_inimigos()))

print(fase2.descricao())
print(fase2.ambiente())
print("Inimigos:", ", ".join(fase2.gerar_inimigos()))

# Se quiser alterar o tempo para todas as fases:
# Fase.tempo_maximo = 400, isso afeta todas as instâncias.


# Explicação:
# tempo_maximo = 300 é um atributo de classe, ou seja, é comum a todas as fases.

# Você pode acessar esse atributo usando Fase.tempo_maximo.


