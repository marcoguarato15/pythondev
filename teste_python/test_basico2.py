import functions as f
import pytest

def test_subtract_list_length():
    assert f.subtract(5, 3) == 2
    assert f.list_length(["a", "b", "c", "d"]) == 4

def test_validate_email():
    assert f.validate_email("teste@email.com") is True

def test_soma_lista():
    lista = [1, 4, 5, 10]
    assert f.soma_lista(lista) == 20

    
    # Testando casos de erro
    with pytest.raises(ValueError):
        # Se não der erro ele gera esse relatório, então ele espera que o erro ocorra neste caso
        # FAILED test_basico2.py::test_soma_lista - Failed: DID NOT RAISE <class 'ValueError'>
        f.soma_lista([1, 2, 'a'])

def test_encontrar_valor_dicionario():
    dicionario = {"id": "1", "nome": "Marco", "idade": 24, "cidade": "Uberaba"}
    assert f.encontrar_valor(dicionario, "nome") == "Marco"

    with pytest.raises(ValueError):
        assert f.encontrar_valor(["Marco", 24], 24)