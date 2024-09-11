import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo simples de label")

label = tk.Label(janela, text="Apenas um teste de label")
label.pack(pady=10)

janela.mainloop()