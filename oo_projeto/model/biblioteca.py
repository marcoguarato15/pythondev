class Biblioteca:
    bibliotecas = []

    def __init__(self, name):
        self.name = name
        self.active = False
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        # return "Nome:",self.name ,"Ativo:",self.active # retorna uma tupla
        return self.name + " | " +  str(self.active)
    
    def listLibraries():
        for l in Biblioteca.bibliotecas:
            print(f"{l.name} | {"Ativa" if l.active else "Inativa"}")
    
cityLibrary = Biblioteca("Biblioteca da Cidade")
shoppingLibrary = Biblioteca("Biblioteca do Shopping")

print(cityLibrary)
print(shoppingLibrary)

Biblioteca.listLibraries()