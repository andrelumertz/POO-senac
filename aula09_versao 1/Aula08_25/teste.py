# Public, Private, Protected


class Conta_Bancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular # Public
        self.__saldo = saldo # Private
        self.__senha = "123456" # Protected 

    # Método publico: acessivel de qualquer lugar
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else: 
            print("Valor inválido para depósito.")

    # Método protegido: recomendavel que seja usado apenas por subclasses ou internamente
    def _verificar_saldo(self) -> None:
        print(f"Saldo atual: {self.__saldo}")

    # Método privado: acessivel apenas dentro da classe
    def __verificar_senha(self, senha):
        return senha == self.__senha


    # Metodo público para acessar o metodo privado
    def autenticar(self, senha):
        if self.__verificar_senha(senha):
            print("Autenticação bem sucedida.")
        else:
            print("Senha inválida.")
            
    def exibir_saldo(self):
        print(f"Saldo atual: {self.__saldo}")


conta = Conta_Bancaria("João", 1000)

print(conta.titular)
# Acesso ao método público
conta.depositar(200)
conta.exibir_saldo()

# print(conta.__saldo)
conta._verificar_saldo()



# Acesso ao método protegido indiretamente
conta.autenticar("123456")
conta.autenticar("1234567")
