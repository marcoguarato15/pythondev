import pytest

def somar(x, y):
    return x + y

@pytest.mark.parametrize(
    "entrada_x, entrada_y, esperado",
    [
        (1, 2, 3),
        (2, 4, 6),
        (0, 0, 0),
        (5, 7, 12)
    ]
)
def test_somar(entrada_x, entrada_y, esperado):
    resultado = somar(entrada_x, entrada_y)
    assert resultado == esperado