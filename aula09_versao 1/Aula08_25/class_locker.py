import random

class Locker:
    """
    Classe que representa um locker para armazenar pacotes.

    Atributos:
        id (int): Identificador único do locker.
        tamanho (str): Tamanho do locker ('P' - Pequeno, 'M' - Médio, 'G' - Grande).
        disponivel (bool): Indica se o locker está disponível.
        senha_random (str): Senha gerada para retirada do pacote.
        apartamento (str): Número do apartamento associado à entrega.
    """

    def __init__(self, id:int, tamanho:str) -> None:
        """
        Inicializa um locker com seu identificador e tamanho.

        Args:
            id (int): Identificador único do locker.
            tamanho (str): Tamanho do locker ('P', 'M', 'G').
        """
        
        #Aqui esta o encapsulamento, que é o principio de que os atributos devem ser privados e acessados através de métodos públicos.
        #Python não tem palavras-chave como private ou public, mas usa convenções: 
        #atributos privados, começam com __ (dois underline)
        #atributos protegidos, começam com _ (um underline)
        #atributos públicos, não começam com nada
        #Os atributos privados, podemos acessar com o @property, mas não podemos acessar diretamente, como self.__id, self.__tamanho, etc. 
        self.__id = id #privado
        self.__tamanho = tamanho #privado
        self.__disponivel = True #privado   
        self.__senha_random = None #privado
        self.__apartamento = None #privado

    #@property é um decorador que permite acessar o atributo como se fosse um atributo público.
    @property
    def id(self):
        """Retorna o identificador do locker."""
        return self.__id

    def esta_disponivel(self):
        """Verifica se o locker está disponível."""
        return self.__disponivel

    def tamanho_certo(self, tamanho:str) -> bool:
        """
        Verifica se o locker é do tamanho desejado.

        Args:
            tamanho (str): Tamanho desejado ('P', 'M', 'G').

        Returns:
            bool: True se o tamanho corresponder, False caso contrário.
        """
        return self.__tamanho == tamanho

    def indisponibilizar(self, apartamento:str) -> None:
        """
        Torna o locker indisponível e associa a um apartamento.

        Args:
            apartamento (str): Número do apartamento.
        """
        self.__disponivel = False #tornando o locker indisponível
        self.__apartamento = apartamento #associando o locker ao apartamento
        self.__senha_random = str(random.randint(1000, 9999)) #gerando uma senha aleatória de 4 digitos
        print("\nEnviando mensagem...") #printando a mensagem de que a entrega está disponível
        print(f"Nova entrega disponível! Apt: {apartamento} - Senha: {self.__senha_random}") #printando a senha gerada

    def disponibilizar(self):
        """
        Torna o locker disponível novamente após a retirada do pacote.
        """
        self.__disponivel = True #tornando o locker disponível
        self.__apartamento = None #removendo o apartamento associado ao locker
        self.__senha_random = None #removendo a senha gerada
        print("Locker Aberto. Retire sua encomenda.") #printando a mensagem de que o locker está aberto para retirada do pacote 
        input("Feche a porta e pressione Enter.") #aguardando o usuário fechar a porta
        print("Locker liberado.") #printando a mensagem de que o locker está liberado

    @property
    def senha_random(self):
        """Retorna a senha gerada para retirada do pacote."""
        return self.__senha_random

    @property
    def apartamento(self):
        """Retorna o número do apartamento associado ao locker."""
        return self.__apartamento

    @property
    def tamanho(self):
        """Retorna o tamanho do locker."""
        return self.__tamanho
