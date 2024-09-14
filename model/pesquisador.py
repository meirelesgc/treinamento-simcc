class Pesquisador:
    # Atributos privados
    __pesquisador_id: int
    __nome: str
    __lattes: str
    
    def __init__(self, pesquisador_id: int = None, nome: str = None, lattes: str = None):
        # Inicializa os atributos da classe com os valores fornecidos
        self.__pesquisador_id = pesquisador_id
        self.__nome = nome
        self.__lattes = lattes
        
    def json(self) -> dict:
        """
        Converte o objeto Pesquisador em um dicionário JSON.
        
        Returns:
            dict: Um dicionário representando o pesquisador, com os atributos pesquisador_id, nome e lattes.
        """
        # Cria um dicionário com os atributos do pesquisador
        pesquisador = {
            'pesquisador_id': self.__pesquisador_id,
            'nome': self.__nome,
            'lattes': self.__lattes
        }
        
        return pesquisador
