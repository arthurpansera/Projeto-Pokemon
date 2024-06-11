
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Dados de exemplo em uma matriz
pokemons = [
    ["Pikachu", "imagens/pikachu.png", "Electric", 35, 55, 40],
    ["Bulbasaur", "imagens/bulbasaur.png", "Grass/Poison", 45, 49, 49],
    ["Charmander", "imagens/charmander.png", "Fire", 39, 52, 43]
]
# Função para atualizar a exibição do Pokémon
def update_pokemon_display(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        pokemon = pokemons[index]
        # Atualizar nome
        lbl_name.config(text=pokemon[0])
        # Atualizar imagem
        img = Image.open(pokemon[1])
        img = ImageTk.PhotoImage(img)
        lbl_image.config(image=img)
        lbl_image.image_types(img)
        img.resize(200,200)


        # Manter uma referência à imagem para evitar que
        #seja coletada pelo garbage collector

        # Atualizar atributos
        lbl_type.config(text=f"Type: {pokemon[2]}")
        lbl_hp.config(text=f"HP: {pokemon[3]}")
        lbl_attack.config(text=f"Attack: {pokemon[4]}")
        lbl_defense.config(text=f"Defense: {pokemon[5]}")

# Interface principal
root = tk.Tk()
root.title("Pokemon Selector")

# Layout principal
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=0, pady=0)

lbl_select = tk.Label(frame_left, text="Select a Pokemon:")
lbl_select.pack()

listbox = tk.Listbox(frame_left)
for pokemon in pokemons:
    listbox.insert(tk.END, pokemon[0])
listbox.pack()

listbox.bind('<<ListboxSelect>>', update_pokemon_display)

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

btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=10)
root.mainloop()
