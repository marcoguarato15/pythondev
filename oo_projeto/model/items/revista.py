from model.items.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, title, author, price, edicao):
        super().__init__(title, author, price)
        self._edicao = edicao

    def __str__(self):
        return self._title + " " + self._author + " " + str(self._price) + " " + self._edicao
    
    def applyDiscount(self):
        self._price -= self._price * 0.20