# Verifica se a soma total == 10
# caso falhe ele mostra o resultado esperado e onde está o erro
def test_soma():
    assert sum([1, 4, 5]) == 10

def is_positive(number):
    return number > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-2) is False
    # assert is_positive(0) is True # teste dá como erro -> FAILED test_basico.py::test_is_positive - assert False is True