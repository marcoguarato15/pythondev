import math_operations
from math_operations import divide, multiply

import string_utils

# Possível atribuir uma variável para ficar mais fácil chamar o módulo importado
mo = math_operations

# Utilização indireta, necessário chamar o módulo
print(math_operations.sum(5, 3))
print(mo.subtract(5, 3))

# Utilização direta da função importada com o 'from * import *'
print(multiply(5,3))
print(divide(5,3))

su = string_utils
print(su.capitalizeString("hello World"))
print(su.reverseString("Reversed"))
print(su.count("Apple"))