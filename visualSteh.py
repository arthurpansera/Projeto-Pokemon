import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def atualizar_informacoes_pokemon(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        pokemon = pokemons[index]
        # Atualizar nome
        lbl_name.config(text=pokemon[0])
        lbl_type.config(text=f"Tipo: {pokemon[2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemon[3]}")
        lbl_attack.config(text=f"Ataque: {pokemon[4]}")
        lbl_defense.config(text=f"Defensa: {pokemon[5]}")
        lbl_hp.config(text=f"HP: {pokemon[6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemon[7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemon[8]}")
        lbl_speed.config(text=f"Velocidade: {pokemon[9]}")
        lbl_total.config(text=f"Total: {pokemon[10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemon[1])
        imagePokemon = imagePokemon.resize((586, 483))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


#Configurações da Janela
janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("1200x1000")
janela.config(bg="white")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)

pokemons = [
    #Name, imagem, Primary Type,Secondary type,Attack,Defense,HP,Sp.Attack,Sp.Defense,Speed,Total, imagem do icone
    ['Bulbasaur','imagens/bulbasaur.png', 'GRASS,POISON','',49,49,45,65,65,45,318,],
    ['Charmander','imagens/charmander.png','FIRE','',52,43,39,60,50,65,309,],
    ['Squirtle','imagens/squirtle.png','WATER','',48,65,44,50,64,43,314,],
    ['Caterpie','imagens/caterpie.png','BUG','',30,35,45,20,20,45,195, ],
    ['Weedle','imagens/weedle.png','BUG','POISON',35,30,40,20,20,50,195, ],
    ['Pidgey','imagens/pidgey.png','NORMAL','FLYING',45,40,40,35,35,56,251,],
    ['Spearow', 'imagens/spearow.png','NORMAL','FLYING',60,30,40,31,31,70,262,],
    ['Rattata','imagens/rattata.png', 'NORMAL','',56,35,30,25,35,72,253,],
    ['Ekans','imagens/ekans.png','POISON','',60,44,35,40,54,55,288,],
    ['Pikachu','imagens/pikachu.png','ELECTRIC','',55,40,35,50,50,90,320,]
]

lbl_select = tk.Label(janela, text="Select a Pokemon:")
lbl_select.place(x=900, y=700)

listbox = tk.Listbox(janela)
for pokemon in pokemons:
    listbox.insert(tk.END, pokemon[0])

listbox.place(x=1000, y=600)

listbox.bind('<<ListboxSelect>>', atualizar_informacoes_pokemon)


lbl_name = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 30 bold"), fg="black")
lbl_name.place(x=300, y=15)

lbl_image = Label(janela)
lbl_image.place(x=375, y=70)

#Habilidade do Pokemons
lbl_habilities = Label(janela, text="Habilidade", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black")
lbl_habilities.place(x=700, y=570)

lbl_type = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black")
lbl_type.place(x=700, y=610)

lbl_secondtype = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black")
lbl_secondtype.place(x=700, y=640)



#Informações do Pokemon
lbl_status = Label(janela, text="Status", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black")
lbl_status.place(x=300, y=570)

lbl_hp = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_hp.place(x=300, y=610)

lbl_attack = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_attack.place(x=300, y=640)

lbl_defense = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_defense.place(x=300, y=670)

lbl_spAttack = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_spAttack.place(x=300, y=700)

lbl_spDefense = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_spDefense.place(x=300, y=730)

lbl_speed = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_speed.place(x=300, y=760)

lbl_total = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black")
lbl_total.place(x=300, y=790)


#Botoes para Cada Pokemon

imageBulbasaurIcone = Image.open("imagens/icone-bulbasaur.png")
imageBulbasaurIcone = imageBulbasaurIcone.resize((60, 63))
imageBulbasaurIcone = ImageTk.PhotoImage(imageBulbasaurIcone)
btn_imageIcone = Button(janela, command=atualizar_informacoes_pokemon, image=imageBulbasaurIcone, text=(f"Bulbasaur "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_imageIcone.place(x=10, y=100)

imageCharmanderIcone = Image.open("imagens/icone-charmander.png")
imageCharmanderIcone = imageCharmanderIcone.resize((60, 63))
imageCharmanderIcone = ImageTk.PhotoImage(imageCharmanderIcone)
btn_Charmander = Button(janela, image=imageCharmanderIcone, text=(f"Charmander"), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Charmander.place(x=10, y=160)

imageSquirtleIcone = Image.open("imagens/icone-squirtle.png")
imageSquirtleIcone = imageSquirtleIcone.resize((60, 63))
imageSquirtleIcone = ImageTk.PhotoImage(imageSquirtleIcone)
btn_Squirtle= Button(janela, image=imageSquirtleIcone, text=(f"Squirtle  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Squirtle.place(x=10, y=220)

imageCaterpieIcone = Image.open("imagens/icone-caterpie.png")
imageCaterpieIcone = imageCaterpieIcone.resize((60, 63))
imageCaterpieIcone = ImageTk.PhotoImage(imageCaterpieIcone)
btn_Caterpie= Button(janela, image=imageCaterpieIcone, text=(f"Caterpie  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Caterpie.place(x=10, y=280)

imageWeedleIcone = Image.open("imagens/icone-weedle.png")
imageWeedleIcone = imageWeedleIcone.resize((60, 63))
imageWeedleIcone = ImageTk.PhotoImage(imageWeedleIcone)
btn_Weedle= Button(janela, image=imageWeedleIcone, text=(f"Weedle    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Weedle.place(x=10, y=340)

imagePidgeyIcone = Image.open("imagens/icone-pidgey.png")
imagePidgeyIcone = imagePidgeyIcone.resize((60, 63))
imagePidgeyIcone = ImageTk.PhotoImage(imagePidgeyIcone)
btn_Pidgey= Button(janela, image=imagePidgeyIcone, text=(f"Pidgey    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pidgey.place(x=10, y=400)

imageSpearowIcone = Image.open("imagens/icone-spearow.png")
imageSpearowIcone = imageSpearowIcone.resize((60, 63))
imageSpearowIcone = ImageTk.PhotoImage(imageSpearowIcone)
btn_Spearow= Button(janela, image=imageSpearowIcone, text=(f"Spearow   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Spearow.place(x=10, y=460)

imageRattataIcone = Image.open("imagens/icone-rattata.png")
imageRattataIcone = imageRattataIcone.resize((60, 63))
imageRattataIcone = ImageTk.PhotoImage(imageRattataIcone)
btn_Rattata= Button(janela, image=imageRattataIcone, text=(f"Rattata   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Rattata.place(x=10, y=520)

imageEkansIcone = Image.open("imagens/icone-ekans.png")
imageEkansIcone = imageEkansIcone.resize((60, 63))
imageEkansIcone = ImageTk.PhotoImage(imageEkansIcone)
btn_Ekans = Button(janela, image=imageEkansIcone, text=(f"Ekans     "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Ekans.place(x=10, y=580)

imagePikachuIcone = Image.open("imagens/icone-pikachu.png")
imagePikachuIcone = imagePikachuIcone.resize((60, 63))
imagePikachuIcone = ImageTk.PhotoImage(imagePikachuIcone)
btn_Pikachu = Button(janela, image=imagePikachuIcone, text=(f"Pikachu   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pikachu.place(x=10, y=640)


janela.mainloop()