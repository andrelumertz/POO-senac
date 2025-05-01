class Morador(object):
    def __init__(self, nome, apartamento, senha_geral):
        self.nome = nome
        self.apartamento = apartamento
        self.senha_geral = senha_geral

    def get_apartamento(self):
        return self.apartamento

