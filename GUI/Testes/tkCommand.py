import tkinter as tk

#Janela principal
janela = tk.Tk()

#Label
label = tk.Label(text = "Hello")

#Pega o valor texto do label
texto = label["text"]
print(texto)

#Muda o valor do label
label["text"] = "Good Bye"

label.pack()

janela.mainloop()