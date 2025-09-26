import tkinter as tk
import orm_slqalchemy as orm
from tkinter import messagebox

def adicionarFilme():
    nome = entryNome.get()
    ano = entryAno.get()
    nota = entryNota.get()

    res = orm.addFilme(nome, ano, nota)
    if res == 1:
        messagebox.showinfo("Sucesso", "Sucesso ao adicionar filme.")
    elif res == -1:
        messagebox.showwarning("Falha", "Falha ao adicionar filme")
    else:
        messagebox.showinfo("Desconhecido", "Tentativa desconhecida")


def atualizarFilme():
    id = entryId.get()
    nome = entryNome.get()
    ano = entryAno.get()
    nota = entryNota.get()

    res = orm.updateFilme(id, nome, ano, nota)
    if res == 1:
        messagebox.showinfo("Sucesso", "Sucesso ao atualizar filme")
    elif res == -1:
        messagebox.showwarning("Falha", "Falha ao atualizar filme")
    else:
        messagebox.showinfo("Desconhecido", "Tentativa desconhecida")

def excluirFilme():
    id = entryId.get()
    res = orm.delFilme(id)
    if res == 1:
        messagebox.showinfo("Sucesso", "Sucesso ao excluir filme")
    elif res == -1:
        messagebox.showwarning("Falha", "Falha ao excluir filme")
    else:
        messagebox.showinfo("Desconhecido", "Tentativa desconhecida")


# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Filmes")

# Criação dos icones do CRUD
labelId = tk.Label(root, text="ID:")
labelId.grid(row=0, column=0)
entryId = tk.Entry(root, width=50)
entryId.grid(row=0, column=1, padx=10, pady=5)

labelNome = tk.Label(root, text="Nome:")
labelNome.grid(row=1, column=0)
entryNome = tk.Entry(root, width=50)
entryNome.grid(row=1, column=1, padx=10, pady=5)

labelAno = tk.Label(root, text="Ano:")
labelAno.grid(row=2, column=0)
entryAno = tk.Entry(root, width=50)
entryAno.grid(row=2, column=1, padx=10, pady=5)

labelNota = tk.Label(root, text="nota:")
labelNota.grid(row=3, column=0)
entryNota = tk.Entry(root, width=50)
entryNota.grid(row=3, column=1, padx=10, pady=5)

# Criação dos botoes
buttonAdd = tk.Button(root, text="Adicionar", command=adicionarFilme, width=30,)
buttonAdd.grid(row=4, column=0, columnspan=2, pady=5)

buttonAtualizar = tk.Button(root, text="Atualizar", command=atualizarFilme, width=30)
buttonAtualizar.grid(row=5, column=0, columnspan=2, pady=5)

buttonExcluir = tk.Button(root, text="Excluir", command=excluirFilme, width=30)
buttonExcluir.grid(row=6, column=0, columnspan=2, pady=5)

# Execução do aplicativo
root.mainloop()