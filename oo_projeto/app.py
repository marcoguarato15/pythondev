from model.biblioteca import Biblioteca

cityLibrary = Biblioteca("Biblioteca da Cidade")
shoppingLibrary = Biblioteca("Biblioteca do Shopping")

# cityLibrary.__active = True   # devido a convenção '_' não devemos utilizar mais esse meio para acessar a variável
shoppingLibrary.setActive()     # Fazer desta forma pois é uma variável privada

shoppingLibrary.avaliar('Fulano',2)
shoppingLibrary.avaliar('Ciclano',1)
shoppingLibrary.avaliar('Deltrano',3)
shoppingLibrary.avaliar('Acrano',5)

def main1():
    Biblioteca.listLibraries()

if __name__ == "__main__":          # será sempre correto pois é a partir de onde o arquivo é executado
                                    # SE eu tentar executar algo deste arquivo por fora, o __name__ será o caminho do import
    print(cityLibrary.get__name__)  # como neste caso é model.biblioteca
    print(__name__)
    print(type(main1))
    main1()