from model.biblioteca import Biblioteca
from model.items.livro import Livro
from model.items.revista import Revista

## Definindo/Cirando livrarias
cityLibrary = Biblioteca("Biblioteca da Cidade")
shoppingLibrary = Biblioteca("Biblioteca do Shopping")

## Definindo valores as livrarias
# cityLibrary.__active = True   # devido a convenção '_' não devemos utilizar mais esse meio para acessar a variável
shoppingLibrary.setActive()     # Fazer desta forma pois é uma variável privada

shoppingLibrary.avaliar('Fulano',2)
shoppingLibrary.avaliar('Ciclano',1)
shoppingLibrary.avaliar('Deltrano',3)
shoppingLibrary.avaliar('Acrano',5)

## Criando items Livro e Revista de ItemsBiblioteca
livro1 = Livro("1984", "Geoge Orwell", 30.0, "9786147643236")
livro2 = Livro("Brave New World", "Aldous Huxley", 25.0, "9781541235129")
revista1 = Revista("National Geographic", "Jhon Doe", 15.0, "Quinta")
revista2 = Revista("Pixé", "Eduardo Mahon", 20.0, "Trigésima Quinta")

## Adicionando items às bibliotecas
cityLibrary.add_item(livro1)
cityLibrary.add_item(revista1)
cityLibrary.add_item(livro2)
cityLibrary.add_item(revista2)

def main():
    Biblioteca.listLibraries()
                                      # será sempre correto pois é a partir de onde o arquivo é executado
                                      # SE eu tentar executar algo deste arquivo por fora, o __name__ será o caminho do import
    # print(cityLibrary.get__name__)  # como neste caso é model.biblioteca
    print(__name__)                 # e aqui como método executado no arquivo citado no código cmd será __main__
    # print(type(main))

    ## Mostrando os itens
    print(vars(livro1), vars(revista1))     # Com o método vars
    print(livro1, " | ", revista1)          # Com o método __str__ de cada item

    ## Mostrando os itens através de um método
    cityLibrary.getItems()
    shoppingLibrary.getItems()

if __name__ == "__main__":          
    main()