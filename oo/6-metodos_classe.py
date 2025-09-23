class Game:
    testers = 0
    ammountGames = 0

    def __init__(self, name, releaseYear, multiplayer): 
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.note = 0
        Game.ammountGames += 1
        self.evaluators = 0         # Necessário criar o parâmetro para utilizar nas funções evaluate e average
    
    @classmethod
    def create_with_default_values(cls):
        return cls("default", 0, False)
    
    @classmethod
    def increment_testers(cls, ammount):
        cls.testers += ammount

    def get_ammount_testers(self):
        return self.testers


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

## Jogo 1
# g1 = Game() # problema agora pois não é mais possível criar o objeto vazio

## Jogo 2
g2 = Game("Zelda", 2017, False)

## Jogo 3 
g3 = Game("Fortnite", 2017, True)

## Jogo 4 - Metodo de classe - @classmethod
g4 = Game.create_with_default_values() ## instância da classe sem ser pelo innit

## Metodo instância
g2.evaluate(10.0)
g2.evaluate(8.0)

print(g2.average())
print(g3.average())

# Informações dos jogos
g2.technicalSheet()
g3.technicalSheet()

## Objeto default definido pelo classmethod create...values
print(str(g4) + "\n" + str(type(g4)))

## Método de classe 
g4.increment_testers(1)
g4.increment_testers(3)

## Avaliação do g4(game default) para testes
g4.evaluate(5)
g4.evaluate(6)
g4.evaluate(10)


print(f"Quantidade de testadores: {g4.get_ammount_testers()}")
g4.technicalSheet()

## Total de jogos criados
print(f"Total de jogos: (pela classe):{Game.ammountGames} (pelo g3):{g3.ammountGames}")
