# Verifica se a soma total == 10
# caso falhe ele mostra o resultado esperado e onde está o erro
import functions as f

def test_is_positive():
    assert f.is_positive(5) is True
    assert f.is_positive(-2) is False
    # assert is_positive(0) is True # teste dá como erro -> FAILED test_basico.py::test_is_positive - assert False is True