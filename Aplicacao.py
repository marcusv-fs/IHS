#Nossa placa é a 00

from tkinter import *
cont = 0

def act_iniciar():
    janela = Tk()
    janela.title("CALL GATE: O RESGATE")
    
    texto = Label(janela, text = "Aperte 'A' para ir para a garagem, 'W' para ir para a cozinha ou 'D' para ir para o quarto", fg = "Black")
    cx_texto = Tk.Entry(janela, width = 3, fg = "white", bg = "black")

    texto.pack()
    cx_texto.pack()

    bt_pg_txt = Button(janela, text= "Confirma", command = act_confirma(cx_texto.get()), fg = "white", bg = "gray")
    bt_pg_txt.pack()

def act_confirma(nome):
    print(nome)
    janela.destroy()

def act_sobre():
    print("iniciar")

def act_sair():
    exit(0)

janela = Tk() #Janela principal
janela.title("CALL GATE: O RESGATE") #Adicionando o título
tela = Label(janela)


img_capa = PhotoImage(file='Imagens/Gate.png')
texto = Label(janela, image=PhotoImage(file='Imagens/Gate.png'))
texto.grid(column=0, row=0, padx=0, pady=0)

bt_iniciar = Button(janela, text= "Jogar", command= act_iniciar, fg = "white", bg = "gray")
bt_iniciar.grid(column=0, row=5, padx=10, pady=10)

bt_sobre = Button(janela, text="Sobre", command = act_sobre, fg = "white", bg = "gray")
bt_sobre.grid(column=0, row=10, padx=10, pady=10)

bt_sair = Button(janela, text="Sair", command = act_sair, fg = "white", bg = "gray")
bt_sair.grid(column=0, row=15, padx=10, pady=10)

janela.mainloop()

