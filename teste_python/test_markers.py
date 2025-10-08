import pytest

def funcao_unidade(x):
    """Função de exemplo para testes unitários"""
    return x * 2

def funcao_integracao(x):
    """Função de exemplo para testes de integração"""
    return x + 10

## Comando para execução de marcadores criados
# pytest -m unity,integration,slow....
# pytest -m "not slow"
# pytest -m "not unity and not slow"

@pytest.mark.unit
def teste_unitario():
    assert funcao_unidade(10) == 20
    assert funcao_unidade(3) == 6
    assert funcao_unidade(2) == 4
    
@pytest.mark.integration
def test_integration():
    assert funcao_integracao(10) == 20
    assert funcao_integracao(3) == 13
    assert funcao_integracao(0) == 10
    assert funcao_integracao(-5) == 5

@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(2)
    assert True

@pytest.mark.unit
@pytest.mark.integration
def test_funcao_combinada():
    assert funcao_unidade(1) == 2
    assert funcao_integracao(2) == 12