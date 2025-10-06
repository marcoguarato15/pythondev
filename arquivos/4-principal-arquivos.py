from mod_agenda_4 import add_contact, list_contacts, del_all_contacts
def main():
    while True:
        print("1. Inserir contatos")
        print("2. Mostrar todos contatos")
        print("3. Excluir todos contatos")
        print("4. Sair")

        opc = input("Escolha uma opção (1-4): ")

        if opc == "1":
                add_contact()
        elif opc == "2":
                list_contacts()
        elif opc == "3":
                del_all_contacts()
        elif opc == "4":
            break
        else:
            print("Opção inválida! escolha de 1 a 4!")

main()
