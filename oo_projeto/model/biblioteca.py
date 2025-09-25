from model.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = [] # isto é ruim pois é uma variável estática, se eu quiser uma biblioteca fora do país e contá-la
                     # de forma diferente ele irá adicionar automaticamente nesta variável(lista)

    def __init__(self, name):
        self.name = name
        self._active = False # '__' antes da variável significa que ela é privada não sendo mais possível alterá-la diretamente
                              # Apenas um '_' significa que é protegida, não deve ser alterada diretamente mas ainda é possível
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        # return "Nome:",self.name ,"Ativo:",self.active # retorna uma tupla
        return self.name + " | " +  self.getActive
    
    def listLibraries():
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | Status")
        for l in Biblioteca.bibliotecas:
            print(f"{l.name.ljust(25)} | {str(l.getMediaAvaliacao).ljust(25)} | {l.getActive}")

    def setActive(self): # Método SET
        self._active = not self._active

    @property # Método GET
    def getActive(self):
        return "Ativa" if self._active else "Inativa"
    
    @property
    def get__name__(self):
        return __name__
    
    # SE não colocar @property ele retorna a instância do objeto
    # Pois é necessário colocar as chaves sem o @property
    @property
    def getMediaAvaliacao(self):
        if not self._avaliacao:
            return '-'
        else:
            soma = sum(avaliacao._note for avaliacao in self._avaliacao)
            media = round(soma / len(self._avaliacao), 1)
            return media

    def avaliar(self, client, note):
        avaliacao = Avaliacao(client, note)
        self._avaliacao.append(avaliacao)
    
print(__name__)

    
