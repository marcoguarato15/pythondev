def is_positive(number):
    return number > 0

def subtract(a, b):
    return a - b

def list_length(list):
    return len(list)

def validate_email(email):
    return '@' in email and '.' in email

def soma_lista(valores: list) -> bool:
    if not all(isinstance(i, (int, float)) for i in valores):
        raise ValueError("Todos os valores da lista devem ser numeros")
    return sum(valores)

def encontrar_valor(dicionario, chave):
    if not isinstance(dicionario, dict):
        raise ValueError("O primeiro argumento deve ser um dicionário")
    # dict.get(chave, None) significa que irá pegar o valor da chave passada como parâmetro
    return dicionario.get(chave, None)

