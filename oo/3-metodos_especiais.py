class Game:

    # Neste caso o instanciamento com parâmetros é OPCIONAL
    # SE remover os valores padrões ele  se torna obrigatório
    def __init__(self, name="Default", releaseYear=0, multiplayer=False, note=0): 
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self): # Este é um método especial, ele é retornado caso seja chamado o print do objeto
        return f"Nome: {self.name} | Ano de lançamento: {self.releaseYear} | {"Multiplayer" if self.multiplayer else "Singleplayer"} | Nota: {self.note}"

# Jogo 1
g1 = Game()

# Jogo 2
g2 = Game("Zelda", 2017, False, 9.5)

# Jogo 3 
g3 = Game("Fortnite", 2017, True, 8.0)
## Informações dos jogos
print("--- Informações dos jogos ---")
print(g1)
print(g2)
print(g3)
