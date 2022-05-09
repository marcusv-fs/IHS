from tkinter import *

tela = Tk()
tela.geometry('1920x1080')
tela.title('GATE: O RESGATE')
tela['bg']='#5d8a82'
tela.attributes('-fullscreen',True)
f = ("Times bold", 14)

def Jogar():
    tela.destroy()
    import tl_sala


def Sobre():
    tela.destroy()
    import sobre
    
def Sair():
    exit(0)

img = PhotoImage(file='Imagens/Gate.png')
Label(tela, image= img).pack(expand=True, fill=BOTH)

Button(
    tela,  
    text="Jogar", 
    font=f,
    command=Jogar
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    tela, 
    text="Sobre", 
    font=f,
    command=Sobre
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    tela, 
    text="Sair", 
    font=f,
    command=Sair
    ).pack(fill=X, expand=TRUE, side=LEFT)


tela.mainloop()