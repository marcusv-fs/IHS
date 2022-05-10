from tkinter import *
from tl_sala import *
from tl_bomb import *
import os, sys #necessária para as funções de write e read
from fcntl import ioctl
from ioctl_cmds import *#defines para iotctl

fd = os.open("/dev/mydev", os.O_RDWR)

def bomb():
    os.close(fd)
    criar_bomb()

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

def vigilancia():
        array_switches = [0,0,0,0]
        for i in range(4):
            input()
            ioctl(fd, RD_SWITCHES) #setando para ler os switches
            array_switches[i] = os.read(fd, 1) #lendo um byte dos switches
        if(array_switches[0] == b'\x0c' and array_switches[1] == b'\x08' and array_switches[2] == b'\x0f' and array_switches[3] == b'\x02'): #resposta: C8F2
            ioctl(fd, WR_RED_LEDS) #se acertou, os leds vermelhos são apagados e os verdes acesos
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            bomb()
        else:
            ioctl(fd, WR_RED_LEDS) #se errou, os leds vermelhos são acesos e os verdes apagados
            data = 0xFFFFFFFF
            os.write(fd, data.to_bytes(4, 'little'))
            ioctl(fd, WR_GREEN_LEDS)
            data = 0x0
            os.write(fd, data.to_bytes(4, 'little'))
            chorou_bb(2)

def criar_garagem():
    tela = Tk()
    tela.geometry('1920x1080')
    tela.title('GATE: O RESGATE')
    tela['bg']='#5d8a82'
    tela.attributes('-fullscreen',True)
    f = ("Times bold", 14)
    #falta a foto

    canvas = Canvas(tela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image( (1920/2), (1080/2), image = bg, anchor = "center")

#TERCEIRO DESAFIO
    #Consiste em hackear o sistema de vigilância da garagem mandando cinco algarismos pelos switches, os quais correspondem ao endereço 
    #que é a soma dos endereços que apareçem nos displays da esquerda (origem) e da direita (offset). Endereço de origem, mostrado em hexa: 0456.
    #Offset, mostrado em hexa: 8392. Resultado: 04560 + 08392 = C8F2. Então, pelos switches, o usuário deve mandar os seguintes
    #algarismos (em decimal) na seguinte ordem: 12 -> 8 -> 15 -> 2. O usuário só tem uma chance, caso contrário perde. Para enviar cada um dos
    #algarismos, envie no terminal a letra 'a'.
    tela.config(bg = "black")
    img = PhotoImage(file='hacker.png')
    tela.title("CALL GATE: O RESGATE")
    imagem = Label(tela, image=img, height=400, width=700)
    imagem.grid(column=0, row=0)
    textinho = "Seu terceiro desafio é hackear o sistema de vigilância da garagem mandando cinco algarismos pelos switches, os quais correspondem ao endereço"
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    textinho = "que é a soma dos endereços que apareçem nos displays da esquerda (origem) e da direita (offset)."
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=6, padx=10, pady=10)
    textinho = "Vc só tem uma chance!!\nMande um algarismo por vez e nessa ordem: mais significativos -> menos significativos."
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=10, padx=10, pady=10)
    textinho = "Para mandar através dos switches é preciso enviar a letra 'a' no terminal.\nLembrando que os switches enviam um número em binário!"
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=15, padx=10, pady=10)
    botao = Button(tela, text="Próximo", command=vigilancia, bg='dark blue', fg='white', font="Arial 10 bold", activebackground='red', activeforeground='white', height=2, width=4)
    botao.grid(column=0, row=20, padx=20, pady=20)
    textinho = "Quando chegar no próximo desafio, pode fechar essa tela."
    texto = Label(tela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=25, padx=10, pady=10)
    ioctl(fd, WR_L_DISPLAY)#origem
    data = 0xff191202 #
    os.write(fd, data.to_bytes(4, 'little'))
    ioctl(fd, WR_R_DISPLAY)#offset
    data = 0x00301024
    os.write(fd, data.to_bytes(4, 'little'))

    Button(
        canvas, 
        text="Voltar", 
        font=f,
        command=Voltar
        ).pack(fill=X, side=BOTTOM)
    
    def Voltar():
        os.close(fd)
        tela.destroy()

    tela.mainloop()