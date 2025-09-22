# Módulo de Hashing
import hashlib
hl = hashlib

## 1 - Verificar os algoritimos disponíveis
print(hl.algorithms_available)

## 2 - Verificar algoritimos de acordo com o SO
print(hl.algorithms_guaranteed)

## 3 - Utilizando o algoritimo sha256
algorithm = hl.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo"
encMessage = message.encode() # necessário dar um encode() para funcionar o update()
print(f"Mensagem: {message}, com encode(): ",encMessage)
print("Algorithm pré update:",algorithm)
algorithm.update(encMessage) # Atribui a mensagem para o algorítimo selecionado tornando-a um objeto
print("Algorithm pós update:",algorithm)
print(algorithm.hexdigest()) # Retorna o valor do objeto de criptografia em um valor hashed hexadecimal

## 4 - Utilizando o MD5 (mais utilizado para verificar a integridade dos arquivos)
md5 = hl.md5()
md5.update(encMessage)
print(f"Mensagem com encode: {encMessage}; codificada a md5: {md5.hexdigest()}")