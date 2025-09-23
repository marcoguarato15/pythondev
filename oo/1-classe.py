class Game:
    name = ""
    releaseYear = 0
    multiplayer = False
    note = 0.0
    
    def __str__(self):
        return f"Nome: {self.name} | Ano de lançamento: {self.releaseYear} | {"Multiplayer" if self.multiplayer else "Singleplayer"} | Nota: {self.note}"

g1 = Game()
print(g1.__str__())