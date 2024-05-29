#from tkinter import
import tkinter as tk

pokedex = [
    ["Pikachu","Electric",35,55,40],
    ["Bulbasaur","Grass",45,49,60],
    ["Charmander","Fire",39,52,42]
]

#Função 

#Inicializando a janela
janela = tk.Tk()
janela.title("Jogo Pokémon")

#Frame é uma região do layout(janela)
#grid(l,c) determina a posição que vai ficar na janela
frame_left = tk.Frame(janela)
frame_left.pack(side=tk.LEFT,padx=10,pady=10)

#Label é um texto na tela
lbl_select = tk.Label(frame_left,text="Selecione um pokémon: ")
lbl_select.pack()

#Alimentando o listbox com Pokémons
listbox_pokemon = tk.Listbox(frame_left)
for pokemon in pokedex:
    listbox_pokemon.insert(0,pokemon[0])
listbox_pokemon.pack()

btn_exit = tk.Button(frame_left,text="Sair",command=janela.quit)
btn_exit.pack()

#Rodar janela
janela.mainloop()