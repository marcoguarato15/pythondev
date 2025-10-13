import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    """
    Fixture que retorna um objeto de resposta mockado com status code 200 e um
    corpo JSON específico
    """

    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}

    return mock

def test_api_response(mock_response):
    """
    Testa se a resposta mockada tem o status_code correto
    e o JSON esperado
    """
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}

    print(response.json())
