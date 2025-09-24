class Biblioteca:
    name = ""
    active = False

cityLibrary = Biblioteca()
cityLibrary.name = "Biblioteca da cidade"
cityLibrary.active = True

shoppingLibary = Biblioteca()

libraries = [cityLibrary, shoppingLibary]

# print(vars(cityLibrary))
# print(vars(shoppingLibary))

for l in libraries:
    print(vars(l))