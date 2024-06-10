import tkinter as tk
from tkinter import *

janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("1200x1000")
janela.config(bg="white")

janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)


janela.mainloop()