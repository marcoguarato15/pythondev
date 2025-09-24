class Game:
    def __init__(self, name="Default", releaseYear=0, multiplayer=False): 
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.note = 0
        self.evaluators = 0         # contador de avaliadores da nota dos jogos
    
    def __str__(self): # Este é um método especial, ele é retornado caso seja chamado o print do objeto
        return f"Nome: {self.name} | Ano de lançamento: {self.releaseYear} | " +\
            f"{"Multiplayer" if self.multiplayer else "Singleplayer"} | Nota: {self.average()}"
    
    def technicalSheet(self):
        print("--- Informações do jogo ---")
        print(str(self))

    def evaluate(self, note):
        self.note += note
        self.evaluators += 1

    def average(self):
        if self.evaluators != 0:
            return self.note / self.evaluators
        else:
            return f"Não avaliado."

class GameCategory():
    def __init__(self, name):
        self.name = name
        self.games = []

    def addGame(self, game):
        self.games.append(game)

    def showactionGameCategory(self):
        if len(self.games) != 0:
            for g in self.games:
                # se utilizado dentro de um print ele usa o valor de retorno e como a função
                # não retorna nada o valor que é imprimido é 'None' não fazendo o desejado 
                # mas executando a função corretamente
                # Este é o problema de utilizar print para imprimir dentro de uma função em vez de usar return com uma string formatada
                g.technicalSheet() 
                print( f"Categoria: ",self.name)
                print(25 * "-")
        else:
            print("Ainda não há jogos com categoria cadastrados")


# Jogo 1
g1 = Game()

# Jogo 2
g2 = Game("Zelda", 2017, False)

# Jogo 3 
g3 = Game("Fortnite", 2017, True)

# Metodo instância
g1.evaluate(9.5)
g1.evaluate(7.5)

g2.evaluate(10.0)
g2.evaluate(8.0)

## Informações dos jogos
# g1.technicalSheet()
# g2.technicalSheet()
# g3.technicalSheet()

actionGameCategory = GameCategory("Ação")

actionGameCategory.addGame(g2)
actionGameCategory.addGame(g3)

actionGameCategory.showactionGameCategory()