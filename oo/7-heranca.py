## Classe Pai / Super Classe - Classe Generalista
class Game:

    ammountGames = 0

    def __init__(self, name="Default", releaseYear=0, multiplayer=False): 
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.note = 0
        Game.ammountGames += 1
        self.evaluators = 0         # Necessário criar o parâmetro para utilizar nas funções evaluate e average
    
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
            return round(self.note / self.evaluators, 2)
        else:
            return f"Não avaliado."

## Classe filho / Subclasse - Classe Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="Default", releaseYear=0, storyline=""):
        super().__init__(name, releaseYear, multiplayer=False)
        self.storyline = storyline
    def technicalSheet(self):
        super().technicalSheet()
        print(f"O enredo do jogo é: {self.storyline}")

## Jogo 1
g1 = Game()

## Jogo 2
g2 = Game("Fortnite", 2017, False)

## Metodo instância
g2.evaluate(10.0)
g2.evaluate(8.0)

print(g2.average())

## Informações dos jogos
g2.technicalSheet()

## Classe filho SinglePlayerGame
sinGame1 = SinglePlayerGame()
sinGame2 = SinglePlayerGame("The Last of Us 2", 2020, "Uma história emocionante de sobrevivência e vingança ocorrendo em um apocalipse zumbi")

print(sinGame2)

## Avaliações dos jogos single player
sinGame2.evaluate(10.0)
sinGame2.evaluate(9.5)
sinGame2.evaluate(9.2)

## Informações dos jogos single player
sinGame1.technicalSheet()
sinGame2.technicalSheet()


## Total de jogos criados
print(f"Total de jogos: (pela classe):{Game.ammountGames} (pelo g2):{g2.ammountGames}") # Considera os filhos como jogos pois tem o 
                                                                                        # __init__ do super(classe pai) totalizando 4 
                                                                                        # jogos mesmo com apenas 2 classe Game instanciadas
