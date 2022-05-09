from tkinter import *
from tl_cozinha import *
from tl_quarto import *
from tl_garagem import *

def criar_sala():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    def Quarto():
        tela.destroy()
        criar_quarto

    def Cozinha():
        tela.destroy()
        criar_cozinha()

    def Garagem():
        tela.destroy()
        criar_garagem()

    Label(
        tela,
        text="Procure pela bomba",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(expand=True, fill=BOTH)

    Button(
        tela, 
        text="Garagem", 
        font=f,
        command=Garagem
        ).pack(fill=X, expand=TRUE, side=LEFT)

    Button(
        tela, 
        text="Quarto", 
        font=f,
        command=Quarto
        ).pack(fill=X, expand=TRUE, side=LEFT)

    Button(
        tela, 
        text="Cozinha", 
        font=f,
        command=Cozinha
        ).pack(fill=X, expand=TRUE, side=LEFT)

    tela.mainloop()



