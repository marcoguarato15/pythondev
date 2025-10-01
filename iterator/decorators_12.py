def my_decorator(function):
    def wrapper():
        print("Antes da função!")
        function()
        print("Depois da função")
    return wrapper


def to_upper_decorator(function):
    def wrapper():
        strs = function()
        return strs.upper()

    return wrapper


def split_string_decorator(function):
    def wrapper():
        strs = function()
        return strs.split()
    return wrapper