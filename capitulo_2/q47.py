# Arquivo capitulo_2/q47.py

class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0
        self.defesa = defesa  # Usa o setter para validar
        self.missoes = []  # Lista de Missões aceitas

    def mostrar_vida(self):
        return self.__vida

    @property
    def vida(self):
        return self.__vida
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor tem que estar entre 0 e 100.")

    def aceitar_missao(self, missao):
        if isinstance(missao, Missao):
            self.missoes.append(missao)
            print(f"{self.nome} aceitou a missão: {missao.nome}")
        else:
            print("Isso não é uma missão válida.")

    def listar_missoes(self):
        if not self.missoes:
            print(f"{self.nome} não possui missões.")
        else:
            print(f"Missões de {self.nome}:")
            for m in self.missoes:
                print(m)


class Missao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False

    def concluir(self): 
        print("Este método deve ser implementado pelas subclasses.")

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.nome} - {self.descricao} ({status})"

class MissaoPrincipal(Missao):
    def __init__(self, titulo, descricao):
        super().__init__(titulo, descricao)

    def concluir(self):
        if not self.concluida:
            self.concluida = True
            xp = 1000
            ouro = 500
            item = "Espada Lendária"
            return f"Missão concluída! Você recebeu {xp} XP, {ouro} moedas de ouro e um item: {item}."
        else:
            return "Você já concluiu esta missão."


class MissaoSecundaria(Missao):
    def __init__(self, titulo, descricao):
        super().__init__(titulo, descricao)

    def concluir(self):
        if not self.concluida:
            self.concluida = True
            xp = 300
            ouro = 100
            item = "Pocão de Vida"
            return f"Missão concluída! Você recebeu {xp} XP, {ouro} moedas de ouro e um item: {item}."
        else:
            return "Você já concluiu esta missão."



# Criando personagem e missões
p1 = Personagem("Doni", 100, 50)

principal = MissaoPrincipal("Derrotar o Dragão", "Elimine o dragão que ameaça o reino.")
secundaria = MissaoSecundaria("Ajudar o Ferreiro", "Leve minério ao ferreiro da vila.")

# Personagem aceita as missões
p1.aceitar_missao(principal)
p1.aceitar_missao(secundaria)

# Listar missões
p1.listar_missoes()

# Concluir missão
print(principal.concluir())

# Verificar novamente o status das missões
p1.listar_missoes()



