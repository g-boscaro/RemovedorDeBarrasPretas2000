#Criar Interface para o removedor de barras
#import tkinter as tk

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import mainloop
from tkinter import filedialog as fd

def pegaCaminho():
    caminho = fd.askopenfilenames()
    print(caminho)
    return caminho

#-----Janela Principal
#Cria o elemente principal da janela onde serao acomodados os demais botoes
janela_principal = Tk()

#Cria um título para a janela principal
janela_principal.title("Removedor de Barras Pretas 2000")

#Definindo comportamento da janela principal
#janela_principal.rowconfigure()
#janela_principal.columnconfigure()

#-----Botoes
#Selecao de arquivo/arquivos
botao_arq = Button(janela_principal, text = "Arquivo", command = pegaCaminho)

#Executa a funcao de remocao de barras
botao_exec = Button(janela_principal, text = "Remover Barras")

#-----Label
arquivos_caminho = Label(text = botao_arq["pegaCaminho"])

#-----Definindo as posicoes dos botoes no grid
botao_arq.grid(row = 0, column = 1, padx = 10, pady = 10)
arquivos_caminho.grid(row = 1, column = 1, padx = 10, pady = 10)
botao_exec.grid(row = 2, column = 1, padx = 10, pady = 10)

#-----Loop principal que mantem a janela executando
janela_principal.mainloop()