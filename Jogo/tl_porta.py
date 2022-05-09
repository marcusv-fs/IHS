from tkinter import *
from tl_sala import *
import os, sys #necessária para as funções de write e read
from fcntl import ioctl
from ioctl_cmds import *#defines para iotctl


def criar_porta():
    fd = os.open(r'/dev/mydev', os.O_RDWR)
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    def acertou():#mudar de tela
        tela.destroy()
        criar_sala()

    def errou():#mudar de tela
        tela.destroy()

    def validar():
        pass

    Label(
        tela,
        image=img,
        height=500, 
        width=900,
        bg='#ffbf00',
        font=f
    ).grid(column=0, row=0)


    Label(
        tela,
        text="Seu primeiro desafio eh acertar a senha da fechadura!!",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(expand=True, fill=BOTH)

    Label(tela,
         text= "Vc tera que informar quatro algarismos atraves dos push buttons\nUm de cada vez! Forneca um algarismo (segurando!) e envie a tecla 'a' no terminal.",
         fg='white',
         font="Arial 10 bold",
         bg='black'
         ).grid(column=0, row=5, padx=10, pady=10)

    Label(tela,
         text="Se vc acertar o algarismo, os leds verdes ficam ligados, caso contrario, os vermelhos.",
         fg='white',
         font="Arial 10 bold",
         bg='black'
         ).grid(column=0, row=10, padx=10, pady=10)

    Label(tela,
         text="Se vc acertar o algarismo, os leds verdes ficam ligados, caso contrario, os vermelhos.",
         fg='white',
         font="Arial 10 bold",
         bg='black'
         ).grid(column=0, row=20, padx=10, pady=10)

    Label(tela,
         text="Vc tem somente duas tentativas antes do alarme tocar!!", 
         fg='white',
         font="Arial 10 bold",
         bg='black'
         ).grid(column=0, row=25, padx=10, pady=10)

    Label(tela,
         text="Dica para a senha: Quantidade de bytes reservados para a IVT. Informe os algarismos nessa ordem: milhar->centena->dezena->unidade.",
         fg='red',
         font="Arial 5 bold",
         bg='black'
         ).grid(column=0, row=30, padx=10, pady=10)

    Button(
        tela, 
        text="Confirma", 
        font=f,
        command=Voltar
        ).pack(fill=X, expand=TRUE, side=LEFT)

    
    Button(
        tela, 
        text="Inserir digito", 
        font=f,
        command=Voltar
        ).pack(fill=X, expand=TRUE, side=LEFT)
    tela.mainloop()



