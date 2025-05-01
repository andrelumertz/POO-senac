import random


class Locker:
    def __init__(self, id, tamanho):
        self.id = id
        # Pequeno, Médio, Grande
        self.tamanho = tamanho
        # True-Disponível False-Indisponível
        self.disponivel = True
        self.senha_random = None
        self.apartamento = None

    def get_id(self):
        return self.id

    def esta_disponivel(self):
        print(f"Locker {self.get_id()} Destravado. Pode Abrir.")
        return self.disponivel

    def tamanho_certo(self, tamanho):
        if self.tamanho == tamanho:
            return True
        return False

    def indisponibilizar(self, apartamento):
        self.disponivel = False
        self.apartamento = apartamento
        self.senha_random = str(random.randint(1000, 9999))

    def disponibilizar(self):
        self.disponivel = True
        self.apartamento = None
        self.senha_random = None


    def get_senha(self):
        return self.senha_random

    def get_apartamento(self):
        return self.apartamento
