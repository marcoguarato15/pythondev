from model.items.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self._isbn = isbn

    def __str__(self):
        return self._title + " " + self._author + " " + str(self._price) + " " + self._isbn
    