import tkinter as tk

# 1 - Criando a Janela
window = tk.Tk()
window.geometry("600x300") # Proporção da janela
window.title("Gerencia Frases")

# 2 - Adiciona um Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# 3 - Adicionando um label
label = tk.Label(frame, text="Olá mundo!")
label.pack(fill="x", expand=True)

textLabel = tk.Label(frame, text="Frase")
textLabel.pack(fill="x", expand=True)

# 4 - Adiciona o input text
textInput = tk.Entry(frame)
textInput.pack(fill="x", expand=True)

# 5 - Criando a função para alterar o texto do primeiro frame
def click():
    label.config(text=textInput.get())
    # a = ""
    # textInput.config(textvariable=a) # não achei a maneira de resetar o texto, não funciona como o label

# 6 - Adicionando o botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop() # Executa a aplicação
