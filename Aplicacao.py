#Nossa placa é a 00

def botao():
    print("oi")

from tkinter import *

janela = Tk()
img = PhotoImage(file='Imagens/Gate.png')

janela.title("CALL GATE: O RESGATE")
texto = Label(janela, image=img)
texto.grid(column=0, row=0, padx=10, pady=10)

bt_iniciar = Button(janela, text="Jogar", command=botao)
bt_iniciar.grid(column=0, row=5, padx=10, pady=10)

bt_sobre = Button(janela, text="Sobre", command=botao)
bt_sobre.grid(column=0, row=10, padx=10, pady=10)

bt_sair = Button(janela, text="Sair", command=botao)
bt_sair.grid(column=0, row=15, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()