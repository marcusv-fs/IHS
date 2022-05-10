from tkinter import *

def criar_cozinha():
    tela = Toplevel()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)
    bg = PhotoImage(file='../Imagens/cozinha.png')

    canvas = Canvas(tela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image( (1920/2), (1080/2), image = bg, anchor = "center")

    def Voltar():
        tela.destroy()
        import tl_sala

    Label(
        canvas,
        text="Parece que o refém não está nesse lugar",
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


    tela.mainloop()