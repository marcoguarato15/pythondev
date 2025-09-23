class Game:
    name = ""
    releaseYear = 0
    multiplayer = False
    note = 0.0
    
    def __str__(self):
        return f"Nome: {self.name} | Ano de lançamento: {self.releaseYear} | {"Multiplayer" if self.multiplayer else "Singleplayer"} | Nota: {self.note}"

# Jogo 1
g1 = Game() # Este é um objeto
g1.name = "Zelda Breath of the Wild"
g1.releaseYear = 2017
g1.multiplayer = False
g1.note = 9.5

# Jogo 2 
g2 = Game()
g2.name = "Fortnite"
g2.releaseYear = 2017
g2.multiplayer = True
g2.note = 8.0

# Jogo 3 
g3 = Game()
g3.name = "League of Legends"
g3.releaseYear = 2010
g3.multiplayer = True
g3.note = 10.0

## Informações dos jogos
print("--- Informações dos jogos ---")
print(g1.__str__())
print(str(g2))
print(g3)
