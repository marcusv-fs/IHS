
Skip to content
rormoura /
app
Public

Code
Issues
Pull requests
Actions
Projects
Wiki

More
app/Aplicacao.py /
@rormoura
rormoura Add files via upload
History
1 contributor
251 lines (232 sloc) 13.8 KB
#Nossa placa � a 00

## IMPORTA��ES 
import os, sys #necess�ria para as fun��es de write e read
from fcntl import ioctl
from ioctl_cmds import *#defines para iotctl
from tkinter import * #necess�ria para 
## FIM DAS IMPORTA��ES

## FUN��ES
def botao_sair(): #fun��o para sair do jogo
    os.close(fd)
    exit(0)

def chorou_bb(num):
    #fun��o que abre a janela em caso de derrota
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
    botao = Button(janela, text="F", command=botao_sair, bg='dark blue', fg='white', font="Arial 10 bold", activebackground='red', activeforeground='white', height=2, width=4)
    botao.grid(column=0, row=10, padx=10, pady=10)

def ganhou_bb():#fun��o que abre a janela em caso de vit�ria
    print("ganhasse")

def bomba():#QUARTO E �LTIMO DESAFIO
    #Consiste em desarmar a bomba que est� amarrada no ref�m. Para isso o jogador precisa enviar dois algarismos: um pelos switches (dezena) e o outro pelos push
    #buttons (unidade). A dezena est� em bin�rio nos leds vermelhos (aceso = 1, apagado = 0) e a unidade est� em bin�rio nos leds verdes (aceso = 1, apagado = 0)
    #Ser� necess�rio enviar os dois algarismos na mesma hora, quando enviar a letra 'a' no terminal.O usu�rio s� ter� uma chance, caso contr�rio perde.
    print("opa")

def hackear():#TERCEIRO DESAFIO
    #Consiste em hackear o sistema de vigil�ncia da garagem mandando cinco algarismos pelos switches, os quais correspondem ao endere�o 
    #que � a soma dos endere�os que apare�em nos displays da esquerda (origem) e da direita (offset). Endere�o de origem, mostrado em hexa: 0456.
    #Offset, mostrado em hexa: 8392. Resultado: 04560 + 08392 = C8F2. Ent�o, pelos switches, o usu�rio deve mandar os seguintes
    #algarismos (em decimal) na seguinte ordem: 12 -> 8 -> 15 -> 2. O usu�rio s� tem uma chance, caso contr�rio perde. Para enviar cada um dos
    #algarismos, envie no terminal a letra 'a'.
    janela = Toplevel()
    janela.config(bg = "black")
    img = PhotoImage(file='hacker.png')
    janela.title("CALL GATE: O RESGATE")
    imagem = Label(janela, image=img, height=400, width=700)
    imagem.grid(column=0, row=0)
    textinho = "Seu terceiro desafio � hackear o sistema de vigil�ncia da garagem mandando cinco algarismos pelos switches, os quais correspondem ao endere�o"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    textinho = "que � a soma dos endere�os que apare�em nos displays da esquerda (origem) e da direita (offset)."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=6, padx=10, pady=10)
    textinho = "Vc s� tem uma chance!!\nMande um algarismo por vez e nessa ordem: mais significativos -> menos significativos."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=10, padx=10, pady=10)
    textinho = "Para mandar atrav�s dos switches � preciso enviar a letra 'a' no terminal.\nLembrando que os switches enviam um n�mero em bin�rio!"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=15, padx=10, pady=10)
    textinho = "Quando chegar no pr�ximo desafio, pode fechar essa janela."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=15, padx=10, pady=10)
    ioctl(fd, WR_L_DISPLAY)#origem
    data = 0x2e3f3f3a
    os.write(fd, data.to_bytes(4, 'little'))
    ioctl(fd, WR_R_DISPLAY)#destino
    os.write(fd, data.to_bytes(4, 'little'))
    janela.mainloop()

def varrendo():#SEGUNDO DESAFIO
    #Consiste em encontrar o lugar onde est� o ref�m. Existem tr�s lugares poss�veis: a - cozinha, w - garagem, d - quarto, mas o ref�m est� na garagem.
    #O usu�rio manda pelo terminal uma das tr�s letras. Ele tem duas chances, caso contr�rio perde.
    janela = Toplevel()
    janela.config(bg = "black")
    img = PhotoImage(file='interior.png')
    janela.title("CALL GATE: O RESGATE")
    imagem = Label(janela, image=img, height=400, width=700)
    imagem.grid(column=0, row=0)
    textinho = "Seu segundo desafio � encontrar o local onde o ref�m est�!!"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    textinho = "Vc ter� que informar uma das tr�s seguintes op��es no terminal: a - cozinha, w - garagem, d - quarto"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=10, padx=10, pady=10)
    textinho = "Escolha logo! O tempo est� passando!!!\nVc s� tem duas chances antes que os capangas ou�am seus passos!!!"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=20, padx=10, pady=10)
    textinho = "Quando passar para o pr�ximo desafio pode fechar esta janela."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=25, padx=10, pady=10)
    letra = input()
    if(letra == 'a'):#se a primeira escolha foi cozinha
        print("O REF�M N�O EST� NA COZINHA!!\nTente mais uma vez!!!")
        letra = input()
        if(letra == 'w'):#a segunda escolha foi garagem
            print("ISSO! O REF�M EST� NA GARAGEM!!!")
            hackear()
        else:
            print("CHOROU BB!")
            chorou_bb(1)
    elif(letra == 'w'):#o ref�m est� na garagem
        print("ISSO! O REF�M EST� NA GARAGEM!!!")
        hackear()
    else:#se a primeira escolha foi quarto
        print("O REF�M N�O EST� NO QUARTO!!\nTente mais uma vez!!!")
        letra = input()
        if(letra == 'w'):#a segunda escolha foi garagem
            print("ISSO! O REF�M EST� NA GARAGEM!!!")
            hackear()
        else:
            print("CHOROU BB!")
            chorou_bb(1)
    janela.mainloop()

def senha():#AINDA O PRIMEIRO DESAFIO
    #Essa fun��o s�os os loops que leem os push buttons
    valor = [0,0,0,0]
    for i in range(4):
        input()
        ioctl(fd, RD_PBUTTONS) #setando para ler os push buttons
        valor[i] = os.read(fd, 1) #lendo um byte dos push buttons
    if(valor[0] == 1 and valor[1] == 0 and valor[2] == 2 and valor[3] == 4): #resposta: 1024 bytes
        ioctl(fd, WR_RED_LEDS) #se acertou, os leds vermelhos s�o apagados e os verdes acesos
        data = 0x0
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_GREEN_LEDS)
        data = 0xFFFFFFFF
        os.write(fd, data.to_bytes(4, 'little'))
        varrendo()
    else:
        ioctl(fd, WR_RED_LEDS) #se errou, os leds vermelhos s�o acesos e os verdes apagados
        data = 0xFFFFFFFF
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_GREEN_LEDS)
        data = 0x0
        os.write(fd, data.to_bytes(4, 'little'))
        print("S� MAIS UMA CHANCE!")
    for i in range(4):
        input()
        ioctl(fd, RD_PBUTTONS) #setando para ler os push buttons
        valor[i] = os.read(fd, 1) #lendo um byte dos push buttons
    if(valor[0] == 1 and valor[1] == 0 and valor[2] == 2 and valor[3] == 4): #resposta: 1024 bytes
        ioctl(fd, WR_RED_LEDS) #se acertou, os leds vermelhos s�o apagados e os verdes acesos
        data = 0x0
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_GREEN_LEDS)
        data = 0xFFFFFFFF
        os.write(fd, data.to_bytes(4, 'little'))
        varrendo()
    else:
        ioctl(fd, WR_RED_LEDS) #se errou, os leds vermelhos s�o acesos e os verdes apagados
        data = 0xFFFFFFFF
        os.write(fd, data.to_bytes(4, 'little'))
        ioctl(fd, WR_GREEN_LEDS)
        data = 0x0
        os.write(fd, data.to_bytes(4, 'little'))
        print("CHOROU BB!")
        chorou_bb(0)

def botao_iniciar():#PRIMEIRO DESAFIO
    #O desafio consiste em passar atrav�s dos push buttons o n�mero 1024. Desse modo, passam-se um algarismo de cada vez: primeiro o 1, depois o 0,
    #depois o 2 e por fim o 4. Para enviar cada um desses algarismo � preciso: segurar a combina��o referente nos push buttons e depois enviar no terminal
    # a letra 'a'. No momento em que o jogador aperta ENTER, os push buttons s�o lidos. Cada jogador tem duas tentativas para acertar, caso contr�rio perde.
    janela = Toplevel()
    janela.config(bg = "black")
    img = PhotoImage(file='porta.png')
    janela.title("CALL GATE: O RESGATE")
    imagem = Label(janela, image=img, height=500, width=900)
    imagem.grid(column=0, row=0)
    textinho = "Seu primeiro desafio � acertar a senha da fechadura!!"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    textinho = "Vc ter� que informar quatro algarismos atrav�s dos push buttons\nUm de cada vez! Forneca um algarismo (segurando!) e envie a tecla 'a' no terminal."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=10, padx=10, pady=10)
    textinho = "Se vc acertar o algarismo, os leds verdes ficam ligados, caso contr�rio, os vermelhos."
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=15, padx=10, pady=10)
    textinho = "Vc tem somente duas tentativas antes do alarme tocar!!"
    texto = Label(janela, text=textinho, fg='white',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=20, padx=10, pady=10)
    textinho = "Dica para a senha: Quantidade de bytes reservados para a IVT. Informe os algarismos nessa ordem: milhar->centena->dezena->unidade."
    texto = Label(janela, text=textinho, fg='red',font="Arial 5 bold", bg='black')
    texto.grid(column=0, row=25, padx=10, pady=10)
    botao = Button(janela, text="Pr�ximo", command=senha, bg='dark blue', fg='white', font="Arial 10 bold", activebackground='red', activeforeground='white', height=2, width=4)
    botao.grid(column=0, row=30, padx=10, pady=10)
    textinho = "Ap�s apertar o ""Pr�ximo"", pode fechar essa janela"
    texto = Label(janela, text=textinho, fg='red',font="Arial 10 bold", bg='black')
    texto.grid(column=0, row=35, padx=10, pady=10)
    janela.mainloop()

def botao_sobre(): #fun��o que apresenta algumas curiosidades sobre o jogo
    janela = Toplevel()
    janela.config(bg = "black")
    janela.title("CALL GATE: O RESGATE")
    textao = "Projeto de Interface Hardware-Software (2021.2)\nVoc� e sua equipe precisam resgatar um ref�m!!!\nPara isso ter�o que passar por quatro puzzles, cada um utilizando um dos perif�ricos da placa DE2I-150.\nBOM JOGO!"
    texto = Label(janela, text=textao, fg = 'white', bg='black')
    texto.grid(column=0, row=0, padx=10, pady=10)
    textao = "\n\nEquipe: Victor Gabriel de Carvalho (vgc3), Lucas Nascimento Brandao (lnb), Arthur Thierre dos Santos Silva (atss), Marcus Vinicius de Faria Santos (mvfs), Rodrigo Rocha Moura (rrm2)."
    texto = Label(janela, text=textao, fg = 'white', bg='black')
    texto.grid(column=0, row=5, padx=10, pady=10)
    janela.mainloop()
## FIM DAS FUN��ES

## C�DIGOS
if len(sys.argv) < 1: #n�o sei oq � isso
    print("Error: expected more command line arguments")
    print("Syntax: %s </dev/device_file>"%sys.argv[0])
    exit(0)

fd = os.open(sys.argv[0], os.O_RDWR)#se der erro foi o arg q era pra ser 1 ao inv�s de 0 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000

janela = Tk() #abrindo a janela inicial
janela.config(bg = "black")
img = PhotoImage(file='gate.png')
textinho = "N�o feche essa janela pfv :)"
janela.title("CALL GATE: O RESGATE")
imagem = Label(janela, image=img, bg= 'black')
imagem.grid(column=0, row=0, padx=10, pady=10)

bt_iniciar = Button(janela, text="Jogar", command=botao_iniciar, bg='dark blue', fg='white', font="Arial 20 bold", activebackground='red', activeforeground='white', height=2, width=4)
bt_iniciar.grid(column=0, row=5, padx=10, pady=10)

bt_sobre = Button(janela, text="Sobre", command=botao_sobre, bg='dark blue', font="Arial 20 bold", fg= 'white', activebackground='red', activeforeground='white',height=2, width=4)
bt_sobre.grid(column=0, row=10, padx=10, pady=10)

bt_sair = Button(janela, text="Sair", command=botao_sair, bg='dark blue',font="Arial 20 bold", fg='white', activebackground='red', activeforeground='white',height=2, width=4)
bt_sair.grid(column=0, row=15, padx=10, pady=10)

texto = Label(janela, text=textinho, fg='white',font="Arial 20 bold", bg='black')
texto.grid(column=0, row=30, padx=10, pady=10)

janela.mainloop()
##FIM DOS C�DIGOS

    � 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Loading complete