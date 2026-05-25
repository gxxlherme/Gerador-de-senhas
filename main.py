
from tkinter import *

import random
import string



janela = Tk()

try:
    janela.iconbitmap("icone.ico")
except:
    pass

janela.title("PasswordGen")

janela.geometry("500x600")

janela.config(bg="#1e1e1e")




def gerar_senha():

    caracteres = ""

    if var_maiuscula.get():
        caracteres += string.ascii_uppercase

    if var_minuscula.get():
        caracteres += string.ascii_lowercase

    if var_numeros.get():
        caracteres += string.digits

    if var_simbolos.get():
        caracteres += string.punctuation

    if caracteres == "":
        resultado.config(
            text="Selecione pelo menos uma opção!",
            fg="red"
        )
        return

    tamanho = escala.get()

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    pontos = 0

    if any(c.isupper() for c in senha):
        pontos += 1

    if any(c.islower() for c in senha):
        pontos += 1

    if any(c.isdigit() for c in senha):
        pontos += 1

    if any(c in string.punctuation for c in senha):
        pontos += 1

    if len(senha) >= 12:
        pontos += 1

    if pontos <= 2:
        forca = "FRACA"
        cor = "red"

    elif pontos <= 4:
        forca = "MÉDIA"
        cor = "orange"

    else:
        forca = "FORTE"
        cor = "lime"

    resultado.config(state="normal")

    resultado.delete(0, END)

    resultado.insert(0, senha)

    resultado.config(state="readonly")
    texto_forca.config(
    text=f"Força: {forca}",
    fg=cor
)
    




titulo = Label(
    janela,
    text="GERADOR DE SENHAS",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=20)

texto_forca = Label(
    janela,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e"
)

texto_forca.pack()




texto_tamanho = Label(
    janela,
    text="Tamanho da senha",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

texto_tamanho.pack()

escala = Scale(
    janela,
    from_=4,
    to=30,
    orient=HORIZONTAL,
    length=300,
    bg="#1e1e1e",
    fg="white",
    troughcolor="#333333"
)

escala.set(12)

escala.pack(pady=10)




var_maiuscula = IntVar(value=1)

check_maiuscula = Checkbutton(
    janela,
    text="Letras Maiúsculas",
    variable=var_maiuscula,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    font=("Arial", 11)
)

check_maiuscula.pack()

var_minuscula = IntVar(value=1)

check_minuscula = Checkbutton(
    janela,
    text="Letras Minúsculas",
    variable=var_minuscula,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    font=("Arial", 11)
)

check_minuscula.pack()

var_numeros = IntVar(value=1)

check_numeros = Checkbutton(
    janela,
    text="Números",
    variable=var_numeros,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    font=("Arial", 11)
)

check_numeros.pack()

var_simbolos = IntVar(value=1)

check_simbolos = Checkbutton(
    janela,
    text="Símbolos",
    variable=var_simbolos,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    font=("Arial", 11)
)

check_simbolos.pack()




botao = Button(
    janela,
    text="GERAR SENHA",
    command=gerar_senha,
    font=("Arial", 13, "bold"),
    bg="#00aa00",
    fg="white",
    padx=20,
    pady=10
)

botao.pack(pady=20)



resultado = Entry(
    janela,
    font=("Arial", 14, "bold"),
    justify="center",
    width=30,
    bg="#333333",
    fg="black",
    bd=3
)

resultado.config(state="readonly")



resultado.pack(pady=20)




janela.mainloop()

