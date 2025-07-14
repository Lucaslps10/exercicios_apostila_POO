# Arquivo capitulo_2/q30.py
from q25 import Menu

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.vencedores = []

    def exibir(self):
        while True:
            print(self.titulo)
            print("1. Iniciar Jogo")
            print("2. Mostrar Opções")
            print("3. Mostrar vencedores")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome, turnos, venceu = super().iniciar_jogo()
                if venceu:
                    self.salvar_vencedor(nome, turnos)
            elif opcao == "2":
                self.mostrar_opcoes()
            elif opcao == "3":
                self.mostrar_vencedores()
            elif opcao == "4":
                print("Saindo do jogo. Bye bye!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def salvar_vencedor(self, nome, turnos):
        self.vencedores.append((nome, turnos))
        print(f"✅ Vencedor salvo: {nome} - {turnos} turnos.")

    def mostrar_vencedores(self):
        print("\n--- Vencedores Registrados ---")
        if not self.vencedores:
            print("Nenhum vencedor registrado ainda.")
        else:
            for nome, turnos in self.vencedores:
                print(f"🏆 {nome} - {turnos} turnos")
"""
Adiciona emojis usando o atalho Windows + . (tecla Windows + ponto).
"""



menu = MenuAvancado("\n########## Menu Avançado ##########")
menu.exibir()