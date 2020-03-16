#Teste de criação de interface com tkinter

#O principal elemento é chamado window, onde vão os demais elementos

#Importando a biblioteca como tk
import tkinter as tk

#criando o elemento de janela
janela = tk.Tk()

#saudacao = tk.Label(text="Hello, Tkinter")

#saudacao.pack()

#Frame A
#.Frame são molduras que organizam os demais widgets
frame_a = tk.Frame(master = janela, relief = tk.RIDGE, borderwidth = 5)
#.Label é um widget que exibe texto na interface
label_a = tk.Label(master = frame_a, text = "Frame A")
label_a.pack()

#Button cria um widget de botão que pode ser clicado
botao1 = tk.Button(master = frame_a, text = "Arquivos")
botao1.pack()

#Frame B
frame_b = tk.Frame(master = janela, relief = tk.GROOVE, borderwidth = 10)
label_b = tk.Label(master = frame_b, text = "Frame B")
label_b.pack()

botao2 = tk.Button(text = "Texto", master = frame_b)
botao2.pack()

botao3 = tk.Button(text = "Bobagens", master = frame_b)
botao3.pack()

#.Entry é um widget que recebe texto do usuário
entrada = tk.Entry(text = "Uma entrada aí:", master = frame_b)
entrada.pack()

#.pack "empacota" e exibe a funcionalidade na interface
frame_a.pack(side = tk.LEFT)
frame_b.pack(side = tk.RIGHT)

#.mainloop mantém a GUI rodando
janela.mainloop()