#from tkinter import
import tkinter as tk
from PIL import Image, ImageTk

pokedex = [
    ["Pikachu","imagens/pikachu.png","Electric",35,55,40],
    ["Bulbasaur","imagens/bulbasaur.png","Grass",45,49,60],
    ["Charmander","imagens/charmander.png","Fire",39,52,42]
]

#Função para atualizar a exibição do Pokémon(Imagem e dados)
def update_pokemon(event):
    pokemon_selecionado = listbox_pokemon.curselection()
    if pokemon_selecionado:
        #A posição 0 nos dá o índice da listbox
        index = pokemon_selecionado[0]
        pokemon = pokedex[index]
        #Pegar a imagem e padronizar
        img_pokemon = Image.open(pokemon[1])
        img_pokemon = img_pokemon.resize([200,200], Image.ANTIALIAS)
        img_pokemon = ImageTk.PhotoImage(img_pokemon)

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

listbox_pokemon.bind('<<ListBoxSelect>>', update_pokemon)

btn_exit = tk.Button(frame_left,text="Sair",command=janela.quit)
btn_exit.pack()

#Rodar janela
janela.mainloop()