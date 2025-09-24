class Biblioteca:
    bibliotecas = [] # isto é ruim pois é uma variável estática, se eu quiser uma biblioteca fora do país e contá-la
                     # de forma diferente ele irá adicionar automaticamente nesta variável(lista)

    def __init__(self, name):
        self.name = name
        self.__active = False # '__' antes da variável significa que ela é privada não sendo mais possível alterá-la diretamente
                              # Apenas um '_' significa que é protegida, não deve ser alterada diretamente mas ainda é possível
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        # return "Nome:",self.name ,"Ativo:",self.active # retorna uma tupla
        return self.name + " | " +  self.getActive
    
    def listLibraries():
        print(f"{'Nome da biblioteca'.ljust(25)} | Status")
        for l in Biblioteca.bibliotecas:
            print(f"{l.name.ljust(25)} | {l.getActive}")

    def setActive(self): # Método SET
        self.__active = not self.__active

    @property # Método GET
    def getActive(self):
        return "Ativa" if self.__active else "Inativa"
    
    @property
    def get__name__(self):
        return __name__
    
print(__name__)

    
