from tkinter import *
import threading
import time

remaining = 500

tela = Tk()
tela.geometry('1920x1080')
tela.title('GATE: O RESGATE')
tela['bg']='#5d8a82'
tela.attributes('-fullscreen',True)
f = ("Times bold", 34)
bg = PhotoImage(file='../Imagens/bomb.png')

canvas = Canvas(tela)
canvas.pack(fill="both", expand=True)
canvas.create_image( (1920/2), (1080/2), image = bg, anchor = "center")

def criar_bomb():
    def Voltar():
        tela.destroy()
        import menu

    label = Label(
        canvas,
        padx=20,
        pady=20,
        bg='#ffbf00',
        font=f
    )
    label.pack(side=TOP)

    bt = Button(
        canvas, 
        text="Voltar", 
        font=f,
        command=Voltar,
    )
    bt.pack(fill=X, side=BOTTOM)

    def clock():
        global remaining
    
        while remaining>0:
            mins, secs = divmod(remaining, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            remaining -= 1
            label.config(text=timeformat)
            tela.update()
            time.sleep(1)

    threading.Thread(target=clock).start()
    button1_canvas = canvas.create_window(100, 10, anchor = "nw")

    tela.mainloop()