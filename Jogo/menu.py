from tkinter import *
from sobre import *
from tl_porta import *
import os, sys #necessária para as funções de write e read
from ioctl_cmds import *
#from fcntl import ioctl

def criar_menu():

    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)
    bg = PhotoImage(file='../Imagens/Gate.png')

    def Jogar():
        tela.destroy()
        criar_porta()

    def Sobre():
        tela.destroy()
        criar_sobre()
    
    def Sair():
        exit(0)

    canvas = Canvas(tela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image( (1920/2), (1080/2), image = bg, anchor = "center")

    Button(
        canvas, 
        text="Sair", 
        font=f,
        command=Sair
        ).pack(fill=X, side=BOTTOM)

    Button(
        canvas, 
        text="Sobre", 
        font=f,
        command=Sobre
        ).pack(fill=X, side=BOTTOM)

    Button(
        canvas, 
        text="Jogar", 
        font=f,
        command=Jogar
        ).pack(fill=X, side=BOTTOM)

    tela.mainloop()

criar_menu()