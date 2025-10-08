import pytest

def calcular_area(x, y):
    return x * y

"""
Fixture que fornece diferentes conjuntos de dados para testar a função de calculo
"""
@pytest.fixture
def dados_utilizados():
    return [
        {"base": 2, "altura": 10, "esperado": 20},
        {"base": 3, "altura": 5, "esperado": 15},
        {"base": 1, "altura": 3, "esperado": 3},
        {"base": 4, "altura": 5, "esperado": 20},
        {"base": 7, "altura": 2, "esperado": 14}
    ]

# Não utiliza os dados da fixture, ele apenas refez os dados como parâmetros
# Não é possível usar uma fixture em um parametrize pois ele é gerado em tempo de execução e  
# considerado um objeto da classe fixture que não é iterável (que é necessário para ser utilizado no parametrize)
@pytest.mark.parametrize(
    "dados",[
        {"base": 2, "altura": 10, "esperado": 20},
        {"base": 3, "altura": 5, "esperado": 15},
        {"base": 1, "altura": 3, "esperado": 3},
        {"base": 4, "altura": 5, "esperado": 20},
        {"base": 7, "altura": 2, "esperado": 14}
    ]
)
def test_calcular_area(dados):
    base = dados["base"]
    altura = dados["altura"]
    esperado = dados["esperado"]
    resultado = calcular_area(base, altura)
    assert resultado == esperado