from tkinter import *

tela = Tk()
tela.geometry('1920x1080')
tela.title('GATE: O RESGATE')
tela['bg']='#5d8a82'
tela.attributes('-fullscreen',True)
f = ("Times bold", 14)

def Sala():
    tela.destroy()
    import menu

def Garagem():
    tela.destroy()
    import menu


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
    text="Sala", 
    font=f,
    command=Sala
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    tela, 
    text="Garagem", 
    font=f,
    command=garagem
    ).pack(fill=X, expand=TRUE, side=LEFT)


tela.mainloop()