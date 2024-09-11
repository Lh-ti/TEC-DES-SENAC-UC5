import tkinter as tk

def verificar():
    if opcao.get():
        print("Selecionado")
    else:
        print("Não selecionado")
janela = tk.Tk()
janela.title("exemplo de Caixa de Seleção")
opcao = tk.IntVar()
check = tk.Checkbutton(janela, text="Escolha esta opção",
                       variable=opcao, command=verificar)
check.pack(pady=10)
janela.mainloop()