from abc import ABC, abstractmethod

# Necessário herdar de ABC para aplicar o metodo abstrato as subclasses
class ItemBiblioteca(ABC):
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    # Método abstrato (implementação obrigatória de subclasses)
    @abstractmethod
    def applyDiscount(self):
        pass