# Módulo Random
import random
r = random

## 1 - Selecionar um valor aleatório de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(r.choice(list1))

## 2 - Gerar um número aleatório entre um intervalo de valores
rand1 = r.randint(5, 15)
print(rand1)

## 3 - Selecionar um caractere aleatório de uma string
name = "Curso de Python"
print(r.choice(name))

## 4 - Selecionar mais de um valor aleatoriamente sem repetição
print(r.sample(list1, 2))
# print(r.sample(list1, 7)) # problema pois a lista(6 itens) é menor que a quantidade de samples gerando um erro
print(r.sample(name, 3)) # também pega espaços

done = False
while not done:
    print("\nBem vindo ao jogo de sorte! Escolha sua opção: ")
    print("1- Tentar a sorte.")
    print("2- Sair do jogo.")
    choice = input("> ")
    if choice == "1":
        print("\nEscolha um número de 1 a 10! Veremos se tem sorte!!")
        chosenNumber = int(input())
        result = r.randint(1, 10)
        if chosenNumber == result:
            print("Parabéns você acertou sortudo!")
        else:
            print(f"Não foi dessa vez! O número era {result}")
    elif choice == "2":
        done = True
    else:
        print("Escolha inválida tente novamente!")
