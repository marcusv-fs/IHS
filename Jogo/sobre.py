from tkinter import *

def criar_sobre():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    def Voltar():
        tela.destroy()

    Label(
        tela,
        text="Life is short do what you want",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(expand=True, fill=BOTH)

    Button(
        tela, 
        text="Voltar", 
        font=f,
        command=Voltar
        ).pack(fill=X, expand=TRUE, side=LEFT)
    tela.mainloop()
