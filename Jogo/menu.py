from tkinter import *
from sobre import *
from tl_porta import *
import os, sys #necessária para as funções de write e read
from ioctl_cmds import *
from fcntl import ioctl

def criar_cozinha():
    tela = Tk()
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
        criar_sala()

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

def criar_sala():
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

def criar_porta():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    fd = os.open("/dev/mydev", os.O_RDWR)

    def Voltar():
        os.close(fd)
        tela.destroy()

    def sala():
        os.close(fd)
        tela.destroy()
        criar_sala()

    def Sair():
        exit(0)

    def chorou_bb(num):
        #função que abre a janela em caso de derrota
        ioctl(fd, WR_L_DISPLAY)#carinha de choro nos displays da esquerda
        data = 0x2e3f3f3a
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_R_DISPLAY)#carinha de choro nos displays da direita
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_RED_LEDS)#ligando os leds vermelhos
        data = 0xFFFFFFFF
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_GREEN_LEDS)#apagando os leds verdes
        data = 0x00000000
        os.write(fd, data.to_bytes(4, 'little'))
        os.close(fd)
        janela = Toplevel()
        janela.config(bg = "red")
        if(num == 0):
            textinho = "O alarme tocou e os bandidos encurralarram vc e sua equipe :(\nF to respect"
        elif(num == 1):
            textinho = "Seus passos fizeram muito barulho e os bandidos encurralarram vc e sua equipe :(\nF to respect"
        elif(num == 2):
            textinho = "Foi identificado que o sistema estava sendo invadido e os bandidos encurralarram vc e sua equipe :(\nF to respect"
        else:
            textinho = "KABOOM? Yes Rico, KABOOM!\nF to respect"
        texto = Label(janela, text=textinho, fg='black',font="Arial 20 bold", bg="red")
        texto.grid(column=0, row=5, padx=10, pady=10)
        botao = Button(janela, text="F", command=Sair, bg='dark blue', fg='white', font="Arial 10 bold", activebackground='red', activeforeground='white', height=2, width=4)
        botao.grid(column=0, row=10, padx=10, pady=10)

    def senha():#O PRIMEIRO DESAFIO
        #Essa função sãos os loops que leem os push buttons
        valor = [0,0,0,0]
        for i in range(4):
            input()
            ioctl(fd, RD_PBUTTONS) #setando para ler os push buttons
            valor[i] = os.read(fd, 1) #lendo um byte dos push buttons
        if(valor[0] == b'\x01' and valor[1] == b'\x00' and valor[2] == b'\x02' and valor[3] == b'\x04'): #resposta: 1024 bytes
            ioctl(fd, WR_RED_LEDS) #se acertou, os leds vermelhos são apagados e os verdes acesos
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            sala()
        else:
            ioctl(fd, WR_RED_LEDS) #se errou, os leds vermelhos são acesos e os verdes apagados
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            print("SÓ MAIS UMA CHANCE!")
        for i in range(4):
            input()
            ioctl(fd, RD_PBUTTONS) #setando para ler os push buttons
            valor[i] = os.read(fd, 1) #lendo um byte dos push buttons
        if(valor[0] == b'\x01' and valor[1] == b'\x00' and valor[2] == b'\x02' and valor[3] == b'\x04'): #resposta: 1024 bytes
            ioctl(fd, WR_RED_LEDS) #se acertou, os leds vermelhos são apagados e os verdes acesos
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            sala()
        else:
            ioctl(fd, WR_RED_LEDS) #se errou, os leds vermelhos são acesos e os verdes apagados
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            print("CHOROU BB!")
            chorou_bb(0)


    tela.config(bg = "black")
    img = PhotoImage(file='../Imagens/porta.png')
    imagem = Label(tela, image=img, height=500, width=900)
    imagem.grid(column=0, row=0)
    textinho = "Seu primeiro desafio é acertar a senha da fechadura!!"
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    textinho = "Vc terá que informar quatro algarismos através dos push buttons\nUm de cada vez! Forneca um algarismo (segurando!) e envie a tecla 'a' no terminal."
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=10, padx=10, pady=10)
    textinho = "Se vc acertar o algarismo, os leds verdes ficam ligados, caso contrário, os vermelhos."
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=15, padx=10, pady=10)
    textinho = "Vc tem somente duas tentativas antes do alarme tocar!!"
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=20, padx=10, pady=10)
    textinho = "Dica para a senha: Quantidade de bytes reservados para a IVT. Informe os algarismos nessa ordem: milhar->centena->dezena->unidade."
    texto = Label(tela, text=textinho, fg='red',font="Arial 5 bold", bg='black')
    texto.grid(column=0, row=25, padx=10, pady=10)
    botao = Button(tela, text="Próximo", command=senha, bg='dark blue', fg='white', font="Arial 10 bold", activebackground='red', activeforeground='white', height=2, width=4)
    botao.grid(column=0, row=30, padx=10, pady=10)
    textinho = "Após apertar o ""Próximo"", pode fechar essa tela"
    texto = Label(tela, text=textinho, fg='red',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=35, padx=10, pady=10)

    Button(
        tela, 
        text="Abrir", 
        font=f,
        command=Voltar
        ).pack(fill=X, expand=TRUE, side=BOTTOM)

    

    tela.mainloop()

def criar_sobre():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)

    def Voltar2():
        tela.destroy()
        criar_menu()

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
        command=Voltar2
        ).pack(fill=X, expand=TRUE, side=LEFT)
    tela.mainloop()

def criar_menu():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)
    bg = PhotoImage(file='Imagens/Gate.png')

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