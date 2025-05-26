
class Usuario_Master:
    """
    Classe base para representar usuários do sistema.

    Atributos:
        nome (str): Nome do usuário.
        apartamento (str): Número do apartamento do usuário.
        senha_universal (str): Senha exclusiva do síndico.
    """

    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        """
        Inicializa um usuário mestre no sistema.

        Args:
            nome (str): Nome do usuário.
            apartamento (str): Número do apartamento do usuário.
            senha (str, opcional): Senha universal, usada apenas pelo síndico.
        """
        self.__nome = nome #atributo privado
        self._apartamento = apartamento #atributo protegido
        if isinstance(self, Sindico): #verificando se o usuário é um síndico
            self.__senha_universal = senha #atribuindo a senha universal ao síndico e deixando a senha privada
        # if type(self) is Sindico:
        #     self.__senha_universal = senha


#Herança: é um conceito que permite criar uma nova classe a partir de uma classe existente, o seu pai aqui é a classe Usuario_Master.
class Sindico(Usuario_Master):
    """
    Classe que representa o síndico do condomínio, herdando de `Usuario_Master`.
    """

    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        """
        Inicializa um síndico do sistema.

        Args:
            nome (str): Nome do síndico.
            apartamento (str): Número do apartamento do síndico.
            senha (str, opcional): Senha universal do síndico.
        """
        super().__init__(nome, apartamento) #O super() é usado para chamar o construtor da classe pai (Usuario_Master), sera verificado se o usuario é um síndico e atribuido a senha universal


# A classe Morador herda de Usuario_Master, e tem um atributo senha_geral, que é exclusivo do morador.
class Morador(Usuario_Master):
    """
    Classe que representa um morador do condomínio, herdando de `Usuario_Master`.

    Atributos:
        senha_geral (str): Senha exclusiva do morador.
    """

    def __init__(self, nome: str, apartamento: str, senha_geral: str) -> None:
        """
        Inicializa um morador do sistema.

        Args:
            nome (str): Nome do morador.
            apartamento (str): Número do apartamento do morador.
            senha_geral (str): Senha exclusiva do morador.
        """
        super().__init__(nome, apartamento) #O super() é usado para chamar o construtor da classe pai (Usuario_Master)
        self.__senha_geral = senha_geral #atribuindo a senha exclusiva do morador

    @property #@property é um decorador que permite acessar o atributo como se fosse um atributo público.
    def apt(self) -> str:
        """Retorna o apartamento associado ao morador."""
        return self._apartamento

    
    @apt.setter #@apt.setter é um decorador que permite definir o apartamento do morador.
    def apt(self, apt: str) -> None:
        """Define o apartamento do morador."""
        self._apartamento = apt #atribuindo o apartamento ao morador
