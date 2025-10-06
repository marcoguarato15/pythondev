import os

def add_contact ():
    name = input("Informe o nome: ")
    address = input("Informe o endereço: ")
    phone = input("Informe o telefone: ")

    contact = f"Nome: {name}\nEndereço: {address}\nContato: {phone}\n"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def list_contacts():
        if not os.path.exists("dados/contatos.txt"):
            print("Lista de Contatos vazia!")
            return -1
        with open("dados/contatos.txt", "r", encoding="utf-8") as file:
            contacts = file.read()
            print(f"{5*'-'}Contatos{5*'-'}")
            print(contacts)

def del_all_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de Contatos vazia!")
        return -1
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("Todos contatos excluídos com sucesso!")

