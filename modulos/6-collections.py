# Módulo de Collections (coleções)
from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contador de itens de uma lista/tupla (Não é case sensitive)
fruitsList = ["Banana", "Banana", "Banana", "Maçã", "Maçã", "Uva", "Uva", "uva", "Abacaxi", 
             "Abacaxi", "Laranja"]
print(fruitsList)
print(Counter(fruitsList))

# 2 - utilizando uma tupla nomeada (parece com um dicionário) e é do tipo class'__main__.game'
Game = namedtuple('game', ['name', 'price', 'grade'])
g1 = Game('Fifa 23', 90.50, 8.5)
g2 = Game('Resident Evil 4 Remake', 300, 10.0)
print(type(g1))
print(f"{g1}\n{g2}")

# 3 - Ordenando dicionários pelos itens, retorna tuplas de dois valores, mas é possível fazer um casting para dicionário neste caso
studentsAge = {"Ana": 28, "Pedro": 23, "Jõao": 25, "Beatris": 24}
print(studentsAge)
a = sorted(studentsAge.items(), key=itemgetter(0)) # necessário colocar o nome do parâmetro 'key'
b = sorted(studentsAge.items(), key=itemgetter(1))
print(dict(a))
print(b)

# 4 - Fazendo uma "Fila"(na verdade é uma lista pois é possível adicionar no final e remover no começo) com deque de collections
deq = deque([20, 40, 60, 80])
print(deq)
deq.appendleft(10)
deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)