# Arquivo capitulo_2/q32.py

class Missao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False

    def concluir(self): 
        print("Este método deve ser implementado pelas subclasses.")

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

        

principal = MissaoPrincipal("Derrotar o Dragão", "Elimine o dragão que ameaça o reino.")
secundaria = MissaoSecundaria("Ajudar o Ferreiro", "Leve minério ao ferreiro da vila.")

print(principal.concluir())
print(secundaria.concluir())
print(principal.concluir())

