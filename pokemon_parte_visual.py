import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Dados de exemplo em uma matriz
pokedex = [
    ["Pikachu", "imagens/pikachu.png", "Electric", 35, 55, 40],
    ["Bulbasaur", "imagens/bulbasaur.png", "Grass", 45, 49, 60],
    ["Charmander", "imagens/charmander.png", "Fire", 39, 52, 42]
]

#Função para atualizar a exibição do Pokémon(Imagem e dados)
def update_pokemon_display(event):
    pokemon_selecionado = listbox_pokemon.curselection()
    if pokemon_selecionado:
        #A posição 0 nos dá o índice da listbox
        index = pokemon_selecionado[0]
        pokemon = pokedex[index]

        # Atualizar nome
        lbl_name.config(text=pokemon[0])

        #Pegar a imagem e padronizar
        img_pokemon = Image.open(pokemon[1])
        img_pokemon = img_pokemon.resize((200,200), Image.ANTIALIAS)
        img_pokemon = ImageTk.PhotoImage(img_pokemon)
        lbl_image.config(image=img_pokemon)
        lbl_image.image = img_pokemon
        #Manter uma referência à imagem para evitar que seja coletada pelo garbage collector

        # Atualizar atributos
        lbl_type.config(text=f"Type: {pokemon[2]}")
        lbl_hp.config(text=f"HP: {pokemon[3]}")
        lbl_attack.config(text=f"Attack: {pokemon[4]}")
        lbl_defense.config(text=f"Defense: {pokemon[5]}")

#Inicializando a janela
janela = tk.Tk()
janela.title("Jogo Pokémon")

#Frame é uma região do layout(janela)
#grid(l,c) determina a posição que vai ficar na janela
frame_left = tk.Frame(janela)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

frame_right = tk.Frame(janela)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

#Label é um texto na tela
lbl_select = tk.Label(frame_left, text="Selecione um pokémon: ")
lbl_select.pack()

#Alimentando o listbox com Pokémons
listbox_pokemon = tk.Listbox(frame_left)
for pokemon in pokedex:
    listbox_pokemon.insert(tk.END, pokemon[0])
listbox_pokemon.pack()

listbox_pokemon.bind('<<ListBoxSelect>>', update_pokemon_display)

lbl_name = tk.Label(frame_right, text="", font=("Helvetica", 20))
lbl_name.pack()

lbl_image = tk.Label(frame_right)
lbl_image.pack()

lbl_type = tk.Label(frame_right, text="")
lbl_type.pack()
lbl_hp = tk.Label(frame_right, text="")
lbl_hp.pack()
lbl_attack = tk.Label(frame_right, text="")
lbl_attack.pack()
lbl_defense = tk.Label(frame_right, text="")
lbl_defense.pack()

btn_exit = tk.Button(janela, text="Sair", command=janela.quit)
btn_exit.pack(pady=10)

#Rodar janela
janela.mainloop()