
from class_SystemaLocker import *
from class_retornar import *
from class_morador import *

menu = """
    +----+-----------------------------------+
    |----+   Sistema de Lockers do Tio Ivo   |
    +----+-----------------------------------+
    |  1 | Entrega                           |
    |  2 | Retirada                          |
    |  3 | Configuração                      |
    |  S | Saída                             |
    +----+-----------------------------------+
    Escolha: """

menu_configuracao = """
    +----+-----------------------------------+
    |----+   Configuração                    |
    +----+-----------------------------------+
    |  1 | Cadastrar Novo Morador            |
    |  2 | Alterar Dados Morador             |
    |  3 | Excluir Morador                   |
    |  R | Retornar                          |
    +----+-----------------------------------+
    Escolha: """


##########################################
# submenu configuração
def novo_morador():
    sistema.cadastrar_morador(1, Morador("Ana", "101", "1111"))
    sistema.cadastrar_morador(2, Morador("Clara", "201", "2222"))
    sistema.cadastrar_morador(3, Morador("Pedro", "301", "3333"))
    pass

def alterar_morador():
    pass

def excluir_morador():
    pass

# def retornar_menu_geral():
#     raise ValueError

def retornar_menu_geral():
    raise RetornarMenu

dict_configuracao = {
        "1": novo_morador,
        "2": alterar_morador,
        "3": excluir_morador,
        "R": retornar_menu_geral}

def submenu_configuracao():
    while True:
        try:
            opcao = input(menu_configuracao).upper()
            dict_configuracao[opcao]()
        except KeyError:
            print("Ops! Escolha incorreta! Tente novamente.")
        # except ValueError:
        #     break
        except RetornarMenu:
            break

# submenu configuração
##########################################


##########################################
# menugeral
def entrega():
    def ler_dados_pacote():
        while True:
            print("Escolha o tamanho do Pacote:")
            print("P - Pequeno")
            print("M - Médio")
            print("G - Grande")
            tam_pacote = input("Qual o tamanho do Pacote? ").upper()
            if tam_pacote in ['P', 'M', 'G']:
                return tam_pacote

            input("OPS. Escolha uma das opções. ")

    def ler_dados_apartamento():
        while True:
            num_apartamento = input("Qual o Apartamento? ").upper()
            if sistema.apartamento_valido(num_apartamento):
                return num_apartamento
            input("OPS. Apartamento não encontrado. Enter")

    def ler_dados_entrega():
        tam_pacote = ler_dados_pacote()
        num_apartamento = ler_dados_apartamento()
        return tam_pacote, num_apartamento

    def confirmar_entrega():
        while True:
            confirmar = input("Finalizar Entrega? s/n: ").upper()
            if confirmar in ['S', 'N']:
                input("Feche a porta do Locker.")
                if confirmar == 'S':
                    return True
                return False

    tamanho_pacote, numero_apartamento = ler_dados_entrega()

    locker = sistema.locker_disponivel(tamanho_pacote)

    if locker:
        if confirmar_entrega():
            locker.indisponibilizar(numero_apartamento)
            print(f"Nova Entrega Disponivel Apt: {locker.get_apartamento()}- Senha Abertura: {locker.get_senha()}")


def retirada():
    senha_recebida = input("Qual a senha enviada? ").upper()
    sistema.retirar_pacote(senha_recebida)

def configuracao():
    submenu_configuracao()

def finaliza():
    print("Sistema Encerrado!")
    exit(0)

dict_escolha = {
        "1": entrega,
        "2": retirada,
        "3": configuracao,
        "S": finaliza}

def menu_geral():
    while True:
        try:
            opcao = input(menu).upper()
            dict_escolha[opcao]()
        except KeyError:
            print("Ops! Escolha incorreta! Tente novamente.")
# menugeral
##########################################


if __name__ == "__main__":
    menu_geral()
