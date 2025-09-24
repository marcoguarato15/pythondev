from model.biblioteca import Biblioteca

cityLibrary = Biblioteca("Biblioteca da Cidade")
shoppingLibrary = Biblioteca("Biblioteca do Shopping")

# cityLibrary.__active = True # não funciona mais pois tem dois '_' ditando que é um atributo privado
shoppingLibrary.setActive() # Fazer desta forma pois é privada e possui o metodo justamente para não acessar a variável diretamente

def main1():
    Biblioteca.listLibraries()

if __name__ == "__main__":          # será sempre correto pois é a partir de onde o arquivo é executado
                                    # SE eu tentar executar algo deste arquivo por fora, o __name__ será o caminho do import
    print(cityLibrary.get__name__)  # como neste caso é model.biblioteca
    print(__name__)
    print(type(main1))
    main1()