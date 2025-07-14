# Arquivo capitulo_2/q34.py

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
        # O raise NotImplementedError em Python é usado para indicar que um método deve 
        # ser implementado por uma subclasse.
        # Se alguém tentar usar o método sem sobrescrevê-lo, o Python lançará uma exceção clara e específica.


# Subclasse FaseFloresta
class FaseFloresta(Fase):
    def __init__(self, dificuldade):
        super().__init__("Floresta Encantada", dificuldade)
        self.criaturas = ["unicórnios", "ogros", "trolls"]
        self.clima = "úmido e chuvoso"

    def ambiente(self):
        return f"Ambiente de floresta com clima {self.clima} e criaturas como {', '.join(self.criaturas)}."
        
        #O método join() em Python é usado para juntar (ou concatenar) os elementos de uma lista 
        #(ou outro iterável de strings) em uma única string, usando um separador específico.
       
    

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
        return ["Escorpião Gigante", "Múmia do Deserto", "Serpente de Areia"]

# Exemplo de uso
fase1 = FaseFloresta("Média")
fase2 = FaseDeserto("Alta")

print(fase1.descricao())
print(fase1.ambiente())

print(fase2.descricao())
print(fase2.ambiente())
print("Inimigos:", ", ".join(fase2.gerar_inimigos()))
