from tkinter import *
from tl_cozinha import *
from tl_quarto import *
from tl_garagem import *
from menu import *
import os, sys #necessária para as funções de write e read
#from fcntl import ioctl
from ioctl_cmds import *#defines para iotctl

def criar_sala():
    import menu
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)
    bg = PhotoImage(file='../Imagens/sala.png')

    canvas = Canvas(tela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image( (1920/2), (1080/2), image = bg, anchor = "center")

    def Voltar():
        tela.destroy()
        criar_menu()

    def quarto():
        tela.destroy()
        criar_quarto()

    def cozinha():
        tela.destroy()
        criar_cozinha()

    def garagem():
        tela.destroy()
        criar_garagem()

    Label(
        canvas,
        text="Seu segundo desafio é encontrar o local onde o refém está!!Escolha logo! O tempo está passando!!!\nVc só tem duas chances antes que os capangas ouçam seus passos!!!",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(side=TOP, fill=X)

    Button(
        canvas, 
        text="Voltar", 
        font=f,
        command=Voltar
        ).pack(fill=X, side=BOTTOM)

    Button(
        canvas, 
        text="Garagem", 
        font=f,
        command=garagem
        ).pack(fill=X, side=BOTTOM)

    Button(
        canvas, 
        text="Quarto", 
        font=f,
        command=quarto
        ).pack(fill=X, side=BOTTOM)

    Button(
        canvas, 
        text="Cozinha", 
        font=f,
        command=cozinha
        ).pack(fill=X, side=BOTTOM)

    tela.mainloop()