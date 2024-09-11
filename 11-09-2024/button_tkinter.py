import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo simples de botão")
janela.geometry("400x400")

def on_click_button():
    print("Botão clicado!")

botao = tk.Button(janela, text="Clique no Botão",
                   command= on_click_button)

botao.pack(pady=10)

janela.mainloop()