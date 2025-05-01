class Porta:
    def __init__(self):
        self.aberta = False
        self.trancada = False
        self.cor = "Branca"

    def abrir(self):
        if self.trancada:
            print("A porta está trancada! Não pode ser aberta.")
        elif self.aberta:
            print("A porta já está aberta.")
        else:
            self.aberta = True
            print("Você abriu a porta.")

    def fechar(self):
        if not self.aberta:
            print("A porta já está fechada.")
        else:
            self.aberta = False
            print("Você fechou a porta.")

    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"Você pintou a porta de {self.cor}.")

    def trancar(self):
        if self.aberta:
            print("Feche a porta antes de trancá-la!")
        elif self.trancada:
            print("A porta já está trancada.")
        else:
            self.trancada = True
            print("Você trancou a porta.")

    def destrancar(self):
        if not self.trancada:
            print("A porta já está destrancada.")
        else:
            self.trancada = False
            print("Você destrancou a porta.")

    def status(self):
        estado = "aberta" if self.aberta else "fechada"
        trancado = "trancada" if self.trancada else "destrancada"
        print(f"A porta está {estado}, {trancado} e pintada de {self.cor}.")

# Criando um objeto Porta
porta = Porta()

# Loop principal
while True:
    print("\n" * 5)
    print("===== Brincando com uma Porta ======")
    escolha = input("""
    O que fazer com a porta?
    1- Abrir a Porta
    2- Fechar a Porta
    3- Pintar a Porta
    4- Trancar a Porta
    5- Destrancar a Porta
    6- Mostrar status da Porta
    7- Sair
    ::: """)

    if escolha == "1":
        porta.abrir()
    elif escolha == "2":
        porta.fechar()
    elif escolha == "3":
        nova_cor = input("Qual cor deseja pintar a porta? ")
        porta.pintar(nova_cor)
    elif escolha == "4":
        porta.trancar()
    elif escolha == "5":
        porta.destrancar()
    elif escolha == "6":
        porta.status()
    elif escolha == "7":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")

    input("\nPressione Enter para continuar...")


