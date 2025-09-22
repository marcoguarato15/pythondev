import os

## 1 - Consultar os métodos do módulo OS
# no terminal com o interpretador python aberto digite $help('os')

## 2 - Retornar a pasta atual
print(os.getcwd())

## 3 - Retornar arquivos e pastas do diretório atual
print(os.listdir()) # Retorna em uma lista de strings

## 4 - Retornar a versão do OS/SO (Sistema Operacional)
os.system('ver')

## 5 - Configurações da máquina
os.system('systeminfo')

## 6 - Limpar a tela do Terminal
# os.system('cls')

## 7 - Desligar o computador
# os.system('shutdown /s')
# os.system('shutdown /s /t 0') # Desliga o computador na hora
## 8 - Cancela o desligamento do computador
# os.system('shutdown /a')

def shutdownOneHour():
    os.system('shutdown /s /t 3600')
    print("O computador irá desligar em uma hora!")

def shutdownHalfHour():
    os.system('shutdown /s /t 1800')
    print("O computador irá desligar em meia hora!")

def cancelShutdown():
    os.system('shutdown /a')
    print("Desligamento automático do computador desativado")

# shutdownOneHour()
# cancelShutdown()