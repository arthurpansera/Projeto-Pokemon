import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def atualizar_informacoes_bulbasaur(event):
        lbl_name.config(text=pokemons[0][0])
        lbl_type.config(text=f"Tipo: {pokemons[0][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[0][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[0][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[0][5]}")
        lbl_hp.config(text=f"HP: {pokemons[0][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[0][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[0][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[0][9]}")
        lbl_total.config(text=f"Total: {pokemons[0][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[0][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_charmander(event):
        lbl_name.config(text=pokemons[1][0])
        lbl_type.config(text=f"Tipo: {pokemons[1][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[1][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[1][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[1][5]}")
        lbl_hp.config(text=f"HP: {pokemons[1][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[1][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[1][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[1][9]}")
        lbl_total.config(text=f"Total: {pokemons[1][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[1][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_squirtle(event):
        lbl_name.config(text=pokemons[2][0])
        lbl_type.config(text=f"Tipo: {pokemons[2][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[2][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[2][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[2][5]}")
        lbl_hp.config(text=f"HP: {pokemons[2][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[2][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[2][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[2][9]}")
        lbl_total.config(text=f"Total: {pokemons[2][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[2][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_caterpie(event):
        lbl_name.config(text=pokemons[3][0])
        lbl_type.config(text=f"Tipo: {pokemons[3][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[3][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[3][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[3][5]}")
        lbl_hp.config(text=f"HP: {pokemons[3][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[3][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[3][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[3][9]}")
        lbl_total.config(text=f"Total: {pokemons[3][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[3][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_weedle(event):
        lbl_name.config(text=pokemons[4][0])
        lbl_type.config(text=f"Tipo: {pokemons[4][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[4][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[4][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[4][5]}")
        lbl_hp.config(text=f"HP: {pokemons[4][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[4][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[4][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[4][9]}")
        lbl_total.config(text=f"Total: {pokemons[4][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[4][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_pidgey(event):
        lbl_name.config(text=pokemons[5][0])
        lbl_type.config(text=f"Tipo: {pokemons[5][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[5][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[5][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[5][5]}")
        lbl_hp.config(text=f"HP: {pokemons[5][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[5][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[5][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[5][9]}")
        lbl_total.config(text=f"Total: {pokemons[5][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[5][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_spearow(event):
        lbl_name.config(text=pokemons[6][0])
        lbl_type.config(text=f"Tipo: {pokemons[6][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[6][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[6][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[6][5]}")
        lbl_hp.config(text=f"HP: {pokemons[6][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[6][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[6][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[6][9]}")
        lbl_total.config(text=f"Total: {pokemons[6][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[6][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)


def atualizar_informacoes_rattata(event):
        lbl_name.config(text=pokemons[7][0])
        lbl_type.config(text=f"Tipo: {pokemons[7][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[7][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[7][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[7][5]}")
        lbl_hp.config(text=f"HP: {pokemons[7][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[7][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[7][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[7][9]}")
        lbl_total.config(text=f"Total: {pokemons[7][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[7][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)

def atualizar_informacoes_ekans(event):
        lbl_name.config(text=pokemons[8][0])
        lbl_type.config(text=f"Tipo: {pokemons[8][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[8][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[8][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[8][5]}")
        lbl_hp.config(text=f"HP: {pokemons[8][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[8][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[8][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[8][9]}")
        lbl_total.config(text=f"Total: {pokemons[8][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[8][1])
        imagePokemon = imagePokemon.resize((476, 373))
        imagePokemon = ImageTk.PhotoImage(imagePokemon)
        lbl_image.config(image=imagePokemon)
        lbl_image.image_types(imagePokemon)        


def atualizar_informacoes_pikachu(event):
        lbl_name.config(text=pokemons[9][0])
        lbl_type.config(text=f"Tipo: {pokemons[9][2]}")
        lbl_secondtype.config(text=f"Tipo secundário: {pokemons[9][3]}")
        lbl_attack.config(text=f"Ataque: {pokemons[9][4]}")
        lbl_defense.config(text=f"Defensa: {pokemons[9][5]}")
        lbl_hp.config(text=f"HP: {pokemons[9][6]}")
        lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons[9][7]}")
        lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons[9][8]}")
        lbl_speed.config(text=f"Velocidade: {pokemons[9][9]}")
        lbl_total.config(text=f"Total: {pokemons[9][10]}")
        # Atualizar imagem
        imagePokemon = Image.open(pokemons[9][1])
        imagePokemon = imagePokemon.resize((476, 373))
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
janela.config(bg = "#d93035")

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


borderImage = Image.open("imagens/border.png")
borderImage = borderImage.resize((600, 530))
borderImage = ImageTk.PhotoImage(borderImage)
lbl_borderImage = Label(janela, image=borderImage, bg="#d93035")
lbl_borderImage.place(x=400, y=20)


infoImage = Image.open("imagens/info.png")
infoImage = infoImage.resize((750, 250))
infoImage = ImageTk.PhotoImage(infoImage)
lbl_infoImage = Label(janela, image=infoImage, bg="#d93035")
lbl_infoImage.place(x=325, y=580)

lbl_name = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 30 bold"), fg="black", bg="#e3e3e3")
lbl_name.place(x=780, y=485)

lbl_image = Label(janela, bg="#598f60")
lbl_image.place(x=473, y=90)


#Habilidade do Pokemons
lbl_habilities = Label(janela, text="Habilidade", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black", bg="#8dc73f")
lbl_habilities.place(x=780, y=610)

lbl_type = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black", bg="#8dc73f")
lbl_type.place(x=780, y=650)

lbl_secondtype = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black", bg="#8dc73f")
lbl_secondtype.place(x=780, y=680)


#Informações do Pokemon
lbl_status = Label(janela, text="Status", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black", bg="#8dc73f")
lbl_status.place(x=380, y=610)

lbl_hp = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_hp.place(x=380, y=650)

lbl_attack = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_attack.place(x=380, y=680)

lbl_defense = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_defense.place(x=380, y=710)

lbl_spAttack = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_spAttack.place(x=380, y=740)

lbl_spDefense = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_spDefense.place(x=380, y=770)

lbl_speed = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_speed.place(x=520, y=650)

lbl_total = Label(janela, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_total.place(x=520, y=680)


#Botoes para Cada Pokemon

imageBulbasaurIcone = Image.open("imagens/icone-bulbasaur.png")
imageBulbasaurIcone = imageBulbasaurIcone.resize((60, 63))
imageBulbasaurIcone = ImageTk.PhotoImage(imageBulbasaurIcone)
btn_Bulbasaur = Button(janela, command=lambda: atualizar_informacoes_bulbasaur(btn_Bulbasaur), image=imageBulbasaurIcone, text=(f"Bulbasaur "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Bulbasaur.place(x=10, y=100)

imageCharmanderIcone = Image.open("imagens/icone-charmander.png")
imageCharmanderIcone = imageCharmanderIcone.resize((60, 63))
imageCharmanderIcone = ImageTk.PhotoImage(imageCharmanderIcone)
btn_Charmander = Button(janela,command=lambda: atualizar_informacoes_charmander(btn_Charmander), image=imageCharmanderIcone, text=(f"Charmander"), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Charmander.place(x=10, y=160)

imageSquirtleIcone = Image.open("imagens/icone-squirtle.png")
imageSquirtleIcone = imageSquirtleIcone.resize((60, 63))
imageSquirtleIcone = ImageTk.PhotoImage(imageSquirtleIcone)
btn_Squirtle= Button(janela,command=lambda: atualizar_informacoes_squirtle(btn_Squirtle), image=imageSquirtleIcone, text=(f"Squirtle  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Squirtle.place(x=10, y=220)

imageCaterpieIcone = Image.open("imagens/icone-caterpie.png")
imageCaterpieIcone = imageCaterpieIcone.resize((60, 63))
imageCaterpieIcone = ImageTk.PhotoImage(imageCaterpieIcone)
btn_Caterpie= Button(janela,command=lambda: atualizar_informacoes_caterpie(btn_Caterpie), image=imageCaterpieIcone, text=(f"Caterpie  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Caterpie.place(x=10, y=280)

imageWeedleIcone = Image.open("imagens/icone-weedle.png")
imageWeedleIcone = imageWeedleIcone.resize((60, 63))
imageWeedleIcone = ImageTk.PhotoImage(imageWeedleIcone)
btn_Weedle= Button(janela, command=lambda: atualizar_informacoes_weedle(btn_Weedle), image=imageWeedleIcone, text=(f"Weedle    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Weedle.place(x=10, y=340)

imagePidgeyIcone = Image.open("imagens/icone-pidgey.png")
imagePidgeyIcone = imagePidgeyIcone.resize((60, 63))
imagePidgeyIcone = ImageTk.PhotoImage(imagePidgeyIcone)
btn_Pidgey= Button(janela, command=lambda: atualizar_informacoes_pidgey(btn_Pidgey), image=imagePidgeyIcone, text=(f"Pidgey    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pidgey.place(x=10, y=400)

imageSpearowIcone = Image.open("imagens/icone-spearow.png")
imageSpearowIcone = imageSpearowIcone.resize((60, 63))
imageSpearowIcone = ImageTk.PhotoImage(imageSpearowIcone)
btn_Spearow= Button(janela, command=lambda: atualizar_informacoes_spearow(btn_Spearow), image=imageSpearowIcone, text=(f"Spearow   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Spearow.place(x=10, y=460)

imageRattataIcone = Image.open("imagens/icone-rattata.png")
imageRattataIcone = imageRattataIcone.resize((60, 63))
imageRattataIcone = ImageTk.PhotoImage(imageRattataIcone)
btn_Rattata= Button(janela,command=lambda: atualizar_informacoes_rattata(btn_Rattata), image=imageRattataIcone, text=(f"Rattata   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Rattata.place(x=10, y=520)

imageEkansIcone = Image.open("imagens/icone-ekans.png")
imageEkansIcone = imageEkansIcone.resize((60, 63))
imageEkansIcone = ImageTk.PhotoImage(imageEkansIcone)
btn_Ekans = Button(janela, command=lambda: atualizar_informacoes_ekans(btn_Ekans), image=imageEkansIcone, text=(f"Ekans     "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Ekans.place(x=10, y=580)

imagePikachuIcone = Image.open("imagens/icone-pikachu.png")
imagePikachuIcone = imagePikachuIcone.resize((60, 63))
imagePikachuIcone = ImageTk.PhotoImage(imagePikachuIcone)
btn_Pikachu = Button(janela, command=lambda: atualizar_informacoes_pikachu(btn_Pikachu), image=imagePikachuIcone, text=(f"Pikachu   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pikachu.place(x=10, y=640)

janela.mainloop()