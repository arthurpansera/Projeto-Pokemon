import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

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

        lbl_type.config(text=f"Tipo: {pokemon[2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemon[3]}")
        lbl_attack.config(text=f"Ataque: {pokemon[4]}")
        lbl_defense.config(text=f"Defensa: {pokemon[5]}")
        lbl_hp.config(text=f"HP: {pokemon[6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemon[7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemon[8]}")
        lbl_speed.config(text=f"Velocidade: {pokemon[9]}")
        lbl_total.config(text=f"Total: {pokemon[10]}")

#Configurações da Janela
janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("1000x800")
janela.config(bg="white")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)

pokemons = [
    #Name,Primary Type,Secondary type,Attack,Defense,HP,Sp.Attack,Sp.Defense,Speed,Total
    ['Bulbasaur','imagens/bulbasaur.png', 'GRASS,POISON','',49,49,45,65,65,45,318],
    ['Charmander','imagens/charmander.png','FIRE','',52,43,39,60,50,65,309],
    ['Squirtle','imagens/squirtle.png','WATER','',48,65,44,50,64,43,314],
    ['Caterpie','imagens/caterpie.png','BUG','',30,35,45,20,20,45,195],
    ['Weedle','imagens/weedle.png','BUG','POISON',35,30,40,20,20,50,195],
    ['Pidgey','imagens/pidgey.png','NORMAL','FLYING',45,40,40,35,35,56,251],
    ['Rattata','imagens/rattata.pgn', 'NORMAL','',56,35,30,25,35,72,253],
    ['Spearow', 'imagens/spearow.png','NORMAL','FLYING',60,30,40,31,31,70,262],
    ['Ekans','imagens/ekans.png','POISON','',60,44,35,40,54,55,288],
    ['Pikachu','imagens/pikachu.png','ELECTRIC','',55,40,35,50,50,90,320]
]

frame_pokemon = Frame(janela, width=670, height=510, relief="flat", bg='lightgray')
frame_pokemon.grid(row=1, column=0, padx=330, pady=0)

lbl_name = Label(frame_pokemon, text="", relief="flat", anchor=CENTER, font=("Fixedsys 25 bold"), fg="black")
lbl_name.place(x=12, y=15)

lbl_type = Label(frame_pokemon, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black")
lbl_type.place(x=12, y=50)

lbl_secondtype = Label(frame_pokemon, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black")
lbl_secondtype.place(x=150, y=50)

lbl_image = tk.Label(frame_pokemon)
lbl_image.pack()

janela.mainloop()