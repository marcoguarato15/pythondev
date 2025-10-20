from datetime import date

class Curso():
    def __init__(self, nome, descricao, formacao_id):
        self.__nome = nome
        self.__descricao = descricao
        self.__data_criacao = date.today()
        self.__formacao_id = formacao_id

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
    
    @property
    def formacao_id(self):
        return self.__formacao_id
    
    @formacao_id.setter
    def formacao_id(self, formacao_id):
        self.__formacao_id = formacao_id
    