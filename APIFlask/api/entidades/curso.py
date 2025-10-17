class Curso():
    def __init__(self, nome, descricao, data_criacao):
        self.__nome = nome
        self.__descricao = descricao
        self.__data_criacao = data_criacao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data_criacao(self):
        return self.__data_criacao
    
    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self.__data_criacao = data_criacao