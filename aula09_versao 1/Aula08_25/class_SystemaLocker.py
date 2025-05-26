
from Aula08_25.class_locker import *
from Aula08_25.class_morador import *


#SistemaLocker é a classe principal do sistema de lockers, gerenciando moradores e lockers.
class SistemaLocker:
    """
    Classe principal do sistema de lockers, gerenciando moradores e lockers.

    Atributos:
        moradores (dict): Dicionário que mapeia IDs para objetos `Morador`.
        lockers (dict): Dicionário que mapeia IDs para objetos `Locker`.
    """

    def __init__(self) -> None:
        """Inicializa o sistema com dicionários de moradores e lockers."""
        #Inicializando os dicionários de moradores e lockers
        #Esses atributos estão com __, ou seja, são privados. Só essa classe pode acessá-los diretamente.
        self.__moradores = {}
        self.__lockers = {}

    def apartamento_valido(self, apartamento: str) -> bool:
        """
        Verifica se o apartamento está registrado no sistema.

        Args:
            apartamento (str): Número do apartamento.

        Returns:
            bool: True se o apartamento for válido, False caso contrário.
        """
        #Verificando se o apartamento está registrado no sistema
        #any() é uma função que retorna True se algum elemento do iterável for True
        return any(morador.apt == apartamento for morador in self.__moradores.values())

    #Verificando se há lockers livres
    def existe_algum_locker_disponivel(self) -> bool:
        """
        Verifica se há lockers disponíveis.

        Returns:
            bool: True se existir ao menos um locker disponível, False caso contrário.
        """
        if any(locker.esta_disponivel() for locker in self.__lockers.values()):
            return True
        input("OPS. Não há lockers disponíveis. Pressione Enter.")
        return False

    def todos_lockers_disponiveis(self) -> None:
        """Exibe todos os lockers disponíveis no sistema."""
        print("\nLockers Disponíveis: ")
        for locker in self.__lockers.values():
            if locker.esta_disponivel():
                print(f"[{locker.id}] - {locker.tamanho}")

    def locker_disponivel(self, tamanho: str) -> Locker | None:
        """
        Retorna um locker disponível com o tamanho desejado.

        Args:
            tamanho (str): Tamanho do locker desejado ('P', 'M', 'G').

        Returns:
            Locker: Um locker disponível para uso.
            None: Se não houver lockers disponíveis.
        """
        for locker in self.__lockers.values():
            if locker.esta_disponivel() and locker.tamanho_certo(tamanho):
                print(f"Locker {locker.id} disponível.")
                print("Porta Liberada. Abra a Porta!")
                return locker
        input(f"OPS. Não há Lockers disponíveis com tamanho: {tamanho}. Pressione Enter.")
        return None

    #Método Temporário para gerar lockers para teste
    def gerar_lockers(self) -> None: # Método Temporário
        self.cadastrar_locker(1, Locker(1, "P"))
        self.cadastrar_locker(2, Locker(2, "P"))
        self.cadastrar_locker(3, Locker(3, "M"))
        self.cadastrar_locker(4, Locker(4, "M"))
        self.cadastrar_locker(5, Locker(5, "G"))

    #Método para cadastrar um locker no sistema
    def cadastrar_locker(self, id_: int, locker: Locker) -> None:
        """
        Registra um locker no sistema.

        Args:
            id_ (int): ID do locker.
            locker (Locker): Objeto locker a ser registrado.
        """
        self.__lockers[id_] = locker
        print(f"Locker {locker.id} cadastrado com sucesso!")

    #Método Temporário para gerar moradores para teste
    def gerar_moradores(self) -> None: # Método Temporário
        self.cadastrar_morador(1, Morador("Ana", "101", "1111"))
        self.cadastrar_morador(2, Morador("Clara", "201", "2222"))
        self.cadastrar_morador(3, Morador("Pedro", "301", "3333"))

    #Método para cadastrar um morador no sistema
    def cadastrar_morador(self, id_: int, novo_morador: Morador) -> None:
        """
        Registra um morador no sistema.

        Args:
            id_ (int): ID do morador.
            novo_morador (Morador): Objeto morador a ser registrado.
        """
        self.__moradores[id_] = novo_morador
        print(f"Apartamento {novo_morador.apt} cadastrado com sucesso!")

    #Método para retirar um pacote do locker
    def retirar_pacote(self, senha_informada: str) -> None:
        """
        Permite a retirada do pacote se a senha informada for correta.

        Args:
            senha_informada (str): Senha fornecida pelo morador para abrir o locker.

        Returns:
            None
        """
        for locker in self.__lockers.values():
            if locker.senha_random == senha_informada:
                locker.disponibilizar() #Método para disponibilizar o locker
                return

        input("OPS. Encomenda não encontrada.") #Msg de erro caso a senha não seja encontrada


