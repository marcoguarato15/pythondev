import pytest as p
import functions as f

# Cria esta lista para ser usada como teste para outras funções de teste que utilizam listas
# como um valor fixo para não ter que criar listas em cada caso
# possível fazer qualquer tipo como tuplas, dicionarios, sets, etc...
@p.fixture
def list_sample():
    return [10, 9, 8, 7, 6]

def test_list_length(list_sample):
    assert f.list_length(list_sample) == 5

def test_soma_valores(list_sample):
    assert f.soma_lista(list_sample) == 40