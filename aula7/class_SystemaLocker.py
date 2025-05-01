
from class_locker import *

class SistemaLocker:
    def __init__(self):
        self.__moradores = {}  # {apartamento: senha}
        self.__lockers = {}  # {apartamento: {"tamanho": tamanho, "senha": senha_gerada}}

    def apartamento_valido(self, apartamento):
        for morador in self.__moradores.values():
            print(111, morador.get_apartamento(), apartamento)
            if morador.get_apartamento() == apartamento:
                return True
        return False

    def locker_disponivel(self, tamanho):
        for locker in self.__lockers.values():
            if locker.esta_disponivel() and \
                locker.tamanho_certo(tamanho):
                print(f"Encontrado. Locker {locker.get_id()} disponivel.")
                return locker
        return None  # Nenhum locker disponível

    def gerar_lockers(self):
        self.cadastrar_locker(1, Locker(1, "P"))
        self.cadastrar_locker(2, Locker(2, "P"))
        self.cadastrar_locker(3, Locker(3, "M"))
        self.cadastrar_locker(4, Locker(4, "M"))
        self.cadastrar_locker(5, Locker(5, "G"))

    def cadastrar_locker(self, id, locker):
        self.__lockers[id] = locker
        print(f"Locker {locker.id} cadastrado com sucesso!")

    def cadastrar_morador(self, id, novo_morador):
        self.__moradores[id] = novo_morador
        print(f"Apartamento {novo_morador.apartamento} cadastrado com sucesso!")
    # def cadastrar_morador(self, apto, senha):
    #     """Cadastra um morador e sua senha."""
    #     if apto in self.moradores:
    #         print("Apartamento já cadastrado!")
    #     else:
    #         self.moradores[apto] = senha
    #         print(f"Apartamento {apto} cadastrado com sucesso!")

    def entregar_pacote(self, apto, tamanho):
        """Registra uma entrega e gera senha aleatória."""
        if apto not in self.__moradores:
            print("Apartamento não cadastrado! Cadastre antes de entregar.")
            return

        senha_gerada = str(random.randint(1000, 9999))  # Senha aleatória
        self.__lockers[apto] = {"tamanho": tamanho, "senha": senha_gerada}

        print(f"Produto entregue no locker! Senha gerada: {senha_gerada}")
        print(f"Morador do apto {apto} foi notificado.")

    def retirar_pacote(self, senha_informada):
        for locker in self.__lockers.values():
            if locker.senha_random == senha_informada:
                print("Locker Aberto. Retire sua Encomenda.")
                locker.disponibilizar()
                print("Locker Liberado.")
                return
        input("OPS. Encomenda não encontrada.")


sistema = SistemaLocker()
sistema.gerar_lockers()
