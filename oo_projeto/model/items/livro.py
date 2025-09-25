from model.items.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self._isbn = isbn       # Padrao ISBN (entre parênteses é o número de caracteres)
                                # Padrão no mínimo 13 caracteres (prefixo(3)(978/979), Grupo de registro(1-5), 
                                # Elemento Registrante(-7), Número de publicação(-6), Dígito de controle(1))

    def __str__(self):
        return self._title + " " + self._author + " " + str(self._price) + " " + self._isbn
    
    def applyDiscount(self):
        self._price -= self._price * 0.10