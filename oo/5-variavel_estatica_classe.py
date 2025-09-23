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
            return self.note / self.evaluators
        else:
            return f"Não avaliado."

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

print(g1.average())
print(g2.average())
print(g3.average())

# Informações dos jogos
g1.technicalSheet()
g2.technicalSheet()
g3.technicalSheet()

# Total de jogos criados
print(f"Total de jogos: (pela classe):{Game.ammountGames} (pelo g3):{g3.ammountGames}")
