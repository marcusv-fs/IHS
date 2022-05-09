from tkinter import *

def criar_quarto():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    def Voltar2():
        tela.destroy()

    Label(
        tela,
        text="do what ",
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    ).pack(expand=True, fill=BOTH)

    Button(
        tela, 
        text="Voltar", 
        font=f,
        command=Voltar2
        ).pack(fill=X, expand=TRUE, side=LEFT)
    tela.mainloop()



