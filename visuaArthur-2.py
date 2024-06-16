import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv

def iniciar_jogo():
    # Definindo tela inicial com imagem do Pokémon Fire Red
    imagem_telaInicial.delete("all")
    image_homeScreen = Image.open("imagens/tela-inicial.png")
    image_homeScreen = image_homeScreen.resize((800, 600))
    image_homeScreen = ImageTk.PhotoImage(image_homeScreen)
    imagem_telaInicial.create_image(0,0, anchor="nw", image=image_homeScreen)
    imagem_telaInicial.image_types = image_homeScreen
    # Adicionando botão "Jogar"
    btn_jogar.config(text="Jogar")
    

def exibir_fala_professor(event):
    btn_jogar.destroy()
    imagem_telaInicial.destroy()

    lbl_fala.config(text="Olá! Eu sou o Professor Carvalho, um pesquisador Pokémon.\n" 
                                "Esse mundo é habitado por várias criaturas chamadas\n" 
                                "de Pokémon. Algumas pessoas os tratam como\n" 
                                "mascotes, outras usam em batalhas.")

    image_textBox = Image.open("imagens/caixa-texto.png")
    image_textBox = image_textBox.resize((700, 200))
    image_textBox = ImageTk.PhotoImage(image_textBox)
    imagem_caixaTexto.config(image=image_textBox)
    imagem_caixaTexto.image_types = image_textBox

    image_teacher = Image.open("imagens/professor-carvalho.png")
    image_teacher = image_teacher.resize((230, 260))
    image_teacher = ImageTk.PhotoImage(image_teacher)
    imagem_professor.config(image=image_teacher)
    imagem_professor.image_types = image_teacher

    image_backgroundTeacher = Image.open("imagens/imagem-fundo-professor.jpg")
    image_backgroundTeacher = image_backgroundTeacher.resize((800, 600))
    image_backgroundTeacher = ImageTk.PhotoImage(image_backgroundTeacher)
    imagem_fundoProfessor.config(image=image_backgroundTeacher)
    imagem_fundoProfessor.image_types = image_backgroundTeacher  


def escolher_pokemon_inicial(event):
    frame_falaprofessor.destroy()

    # Criar tela para escolha do Pokémon inicial
    image_tablePokeball = Image.open("imagens/mesa-pokebola.png")
    image_tablePokeball = image_tablePokeball.resize((700, 450))
    image_tablePokeball = ImageTk.PhotoImage(image_tablePokeball)
    imagem_mesaPokebola.config(image=image_tablePokeball)
    imagem_mesaPokebola.image_types = image_tablePokeball

    image_pokeball1 = Image.open("imagens/pokebola1.png")
    image_pokeball1 = image_pokeball1.resize((140, 140))
    image_pokeball1 = ImageTk.PhotoImage(image_pokeball1)
    imagem_pokebola1.config(image=image_pokeball1)
    imagem_pokebola1.image_types = image_pokeball1

    image_pokeball2 = Image.open("imagens/pokebola2.png")
    image_pokeball2 = image_pokeball2.resize((140, 140))
    image_pokeball2 = ImageTk.PhotoImage(image_pokeball2)
    imagem_pokebola2.config(image=image_pokeball2)
    imagem_pokebola2.image_types = image_pokeball2

    image_pokeball3 = Image.open("imagens/pokebola3.png")
    image_pokeball3 = image_pokeball3.resize((140, 140))
    image_pokeball3 = ImageTk.PhotoImage(image_pokeball3)
    imagem_pokebola3.config(image=image_pokeball3)
    imagem_pokebola3.image_types = image_pokeball3

    image_textBox2 = Image.open("imagens/caixa-texto2.png")
    image_textBox2 = image_textBox2.resize((750, 100))
    image_textBox2 = ImageTk.PhotoImage(image_textBox2)
    imagem_caixaTexto2.config(image=image_textBox2)
    imagem_caixaTexto2.image_types = image_textBox2

    lbl_escolhaPokemon.config(text="Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")
 
def evento_botao_pokemon_inicial(nome):
    imagem_pokebola1.destroy()
    imagem_pokebola2.destroy()
    imagem_pokebola3.destroy()
    btn_bulbasaurInicial.destroy()
    btn_squirtleInicial.destroy()
    btn_charmanderInicial.destroy()
    lbl_escolhaPokemon.destroy()

    if nome == 'Bulbasaur':
        with open("pokemonsIniciais.csv", "r") as pokemons_data:
            dados_pokemons = csv.reader(pokemons_data, delimiter=",")
            for i, linha in enumerate(dados_pokemons):
                if i == 1:
                    pokedex.append(linha)
                    lbl_escolheuBulbasaur.config(text="Ótima escolha! Bulbasaur foi adicionado a sua Pokédex\n")
                    image_bulbasaur = Image.open("imagens/bulbasaur.png")
                    image_bulbasaur = image_bulbasaur.resize((150, 150))
                    image_bulbasaur = ImageTk.PhotoImage(image_bulbasaur)
                    imagem_bulbasauro.config(image=image_bulbasaur)
                    imagem_bulbasauro.image_types = image_bulbasaur
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=650, y=387)

    elif nome == 'Squirtle':
        with open("pokemonsIniciais.csv", "r") as pokemons_data:
            dados_pokemons = csv.reader(pokemons_data, delimiter=",")
            for i, linha in enumerate(dados_pokemons):
                if i == 2:
                    pokedex.append(linha)
                    lbl_escolheuSquirtle.config(text="Ótima escolha! Squirtle foi adicionado a sua Pokédex\n")
                    image_squirtle = Image.open("imagens/squirtle.png")
                    image_squirtle = image_squirtle.resize((150, 150))
                    image_squirtle = ImageTk.PhotoImage(image_squirtle)
                    imagem_squirtle.config(image=image_squirtle)
                    imagem_squirtle.image_types = image_squirtle
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=650, y=387)

    elif nome == 'Charmander':
        with open("pokemonsIniciais.csv", "r") as pokemons_data:
            dados_pokemons = csv.reader(pokemons_data, delimiter=",")
            for i, linha in enumerate(dados_pokemons):
                if i == 3:
                    pokedex.append(linha)
                    lbl_escolheuCharmander.config(text="Ótima escolha! Charmander foi adicionado a sua Pokédex\n")
                    image_charmander = Image.open("imagens/charmander.png")
                    image_charmander = image_charmander.resize((150, 150))
                    image_charmander = ImageTk.PhotoImage(image_charmander)
                    imagem_charmander.config(image=image_charmander)
                    imagem_charmander.image_types = image_charmander
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=650, y=387)

def iniciar_menu(event):
    frame_pokebolas.destroy()

    btn_caverna = Button(frame_menu, text="Entrar na caverna", command=lambda:entrar_caverna(pokemon), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_caverna.place(x=290, y=200)

    btn_mato = Button(frame_menu, text="Entrar no mato", command=lambda:entrar_mato(), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_mato.place(x=290, y=270)

    btn_pokedex = Button(frame_menu, text="Pokédex",command=lambda:mostrar_pokedex(btn_pokedex), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_pokedex.place(x=290, y=340)

    btn_mochila = Button(frame_menu, text="Mostrar Mochila",command=lambda:mostrar_mochila(btn_mochila), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_mochila.place(x=290, y=410)

    btn_sair = tk.Button(frame_menu, text="Sair", command=janela.destroy, width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_sair.place(x=290, y=480)

def entrar_caverna(pokemon):
    frame_menu.destroy()

    image_cave = Image.open("imagens/caverna.png")
    image_cave = image_cave.resize((700, 200))
    image_cave = ImageTk.PhotoImage(image_cave)
    imagem_caverna.config(image=image_cave)
    imagem_caverna.image_types = image_cave

    print(f"Você entrou na caverna e encontrou um {pokemon}")

def entrar_mato(pokemon):
    print(f"Você entrou no mato e encontrou um {pokemon}")

def mostrar_pokedex():
    print("Pokémons na sua Pokédex:")

def mostrar_mochila():
    print("Itens na sua mochila:")

def atualizar_informacoes_bulbasaur(event):
    lbl_name.config(text=pokedex[0][0])
    lbl_type.config(text=f"Tipo: {pokedex[0][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[0][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[0][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[0][5]}")
    lbl_hp.config(text=f"HP: {pokedex[0][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[0][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[0][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[0][9]}")
    lbl_total.config(text=f"Total: {pokedex[0][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[0][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_charmander(event):
    lbl_name.config(text=pokedex[1][0])
    lbl_type.config(text=f"Tipo: {pokedex[1][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[1][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[1][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[1][5]}")
    lbl_hp.config(text=f"HP: {pokedex[1][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[1][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[1][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[1][9]}")
    lbl_total.config(text=f"Total: {pokedex[1][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[1][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_squirtle(event):
    lbl_name.config(text=pokedex[2][0])
    lbl_type.config(text=f"Tipo: {pokedex[2][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[2][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[2][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[2][5]}")
    lbl_hp.config(text=f"HP: {pokedex[2][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[2][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[2][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[2][9]}")
    lbl_total.config(text=f"Total: {pokedex[2][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[2][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_caterpie(event):
    lbl_name.config(text=pokedex[3][0])
    lbl_type.config(text=f"Tipo: {pokedex[3][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[3][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[3][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[3][5]}")
    lbl_hp.config(text=f"HP: {pokedex[3][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[3][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[3][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[3][9]}")
    lbl_total.config(text=f"Total: {pokedex[3][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[3][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_weedle(event):
    lbl_name.config(text=pokedex[4][0])
    lbl_type.config(text=f"Tipo: {pokedex[4][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[4][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[4][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[4][5]}")
    lbl_hp.config(text=f"HP: {pokedex[4][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[4][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[4][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[4][9]}")
    lbl_total.config(text=f"Total: {pokedex[4][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[4][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_pidgey(event):
    lbl_name.config(text=pokedex[5][0])
    lbl_type.config(text=f"Tipo: {pokedex[5][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[5][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[5][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[5][5]}")
    lbl_hp.config(text=f"HP: {pokedex[5][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[5][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[5][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[5][9]}")
    lbl_total.config(text=f"Total: {pokedex[5][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[5][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_spearow(event):
    lbl_name.config(text=pokedex[6][0])
    lbl_type.config(text=f"Tipo: {pokedex[6][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[6][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[6][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[6][5]}")
    lbl_hp.config(text=f"HP: {pokedex[6][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[6][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[6][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[6][9]}")
    lbl_total.config(text=f"Total: {pokedex[6][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[6][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_rattata(event):
    lbl_name.config(text=pokedex[7][0])
    lbl_type.config(text=f"Tipo: {pokedex[7][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[7][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[7][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[7][5]}")
    lbl_hp.config(text=f"HP: {pokedex[7][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[7][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[7][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[7][9]}")
    lbl_total.config(text=f"Total: {pokedex[7][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[7][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

def atualizar_informacoes_ekans(event):
    lbl_name.config(text=pokedex[8][0])
    lbl_type.config(text=f"Tipo: {pokedex[8][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[8][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[8][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[8][5]}")
    lbl_hp.config(text=f"HP: {pokedex[8][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[8][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[8][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[8][9]}")
    lbl_total.config(text=f"Total: {pokedex[8][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[8][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)        

def atualizar_informacoes_pikachu(event):
    lbl_name.config(text=pokedex[9][0])
    lbl_type.config(text=f"Tipo: {pokedex[9][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokedex[9][3]}")
    lbl_attack.config(text=f"Ataque: {pokedex[9][4]}")
    lbl_defense.config(text=f"Defensa: {pokedex[9][5]}")
    lbl_hp.config(text=f"HP: {pokedex[9][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokedex[9][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokedex[9][8]}")
    lbl_speed.config(text=f"Velocidade: {pokedex[9][9]}")
    lbl_total.config(text=f"Total: {pokedex[9][10]}")
    # Atualizar imagem
    imagePokemon = Image.open(pokedex[9][1])
    imagePokemon = imagePokemon.resize((476, 373))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

##Tentando fazer uma função para todos os pokemons, acredito que vai precisar, mas essa aqui em baixo ainda n funciona

def atualizar_informacoes_pokedex(nome):
    if nome == 'Bulbasaur':
        for i, linha in enumerate(pokedex):
            if i == nome:
                lbl_name.config(text=linha[0])
                lbl_type.config(text=f"Tipo: {linha[2]}")
                lbl_secondtype.config(text=f"Tipo secundário: {linha[3]}")
                lbl_attack.config(text=f"Ataque: {linha[4]}")
                lbl_defense.config(text=f"Defensa: {linha[5]}")
                lbl_hp.config(text=f"HP: {linha[6]}")
                lbl_spAttack.config(text=f"Velocidade de Ataque: {linha[7]}")
                lbl_spDefense.config(text=f"Velocidade de Defesa: {linha[8]}")
                lbl_speed.config(text=f"Velocidade: {linha[9]}")
                lbl_total.config(text=f"Total: {linha[10]}")
                #Atualizar imagem
                imagePokemon = Image.open(linha)
                imagePokemon = imagePokemon.resize((476, 373))
                imagePokemon = ImageTk.PhotoImage(imagePokemon)
                lbl_image.config(image=imagePokemon)
                lbl_image.image_types(imagePokemon)

###Precisa definir as variaveis no programa principal, igual ta daqui para baixo, pois quando a gente clica em um botão
### e vai para uma próxima tela, usamos o .destroy() para excluir as coisas da tela anterior
### Caso a variável não seja definida no programa principal, o .destroy() não funciona

janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("800x600")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)
janela.config(bg ="#d93035")

pokedex = []

#Tela inicial
imagem_telaInicial = tk.Canvas(janela, width=800, height=600)
imagem_telaInicial.pack()

btn_jogar = tk.Button(janela, command=lambda: exibir_fala_professor(btn_jogar), text="", width=5, height=0, relief="raised", anchor=NW, padx=10, pady=1, font=("Fixedsys 33"), bg='black', fg='white')
btn_jogar.place(x=230, y=450)

#Tela da fala do professor Carvalho
frame_falaprofessor = tk.Frame(janela, width=800, height=600, bg="#76a2b4")
frame_falaprofessor.pack()

imagem_fundoProfessor = Label(frame_falaprofessor, bg="#76a2b4")
imagem_fundoProfessor.place(x=0, y=0)

imagem_caixaTexto = Label(frame_falaprofessor, bg="#587873")
imagem_caixaTexto.place(x=55, y=350)

lbl_fala = Label(frame_falaprofessor, text="",  relief="flat", font=("Fixedsys 17"), fg="black", bg="#d8e3e3")
lbl_fala.place(x=115, y=400)

imagem_professor = Label(frame_falaprofessor, bg="#b9d4cd")
imagem_professor.place(x=450, y=40)

image_proximo = Image.open("imagens/proximo.png")
image_proximo = image_proximo.resize((45, 40))
image_proximo = ImageTk.PhotoImage(image_proximo)
btn_proximo = tk.Button(frame_falaprofessor, command=lambda:escolher_pokemon_inicial(btn_proximo), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo.place(x=670, y=480)

#Tela de escolher o pokemon inicial
frame_pokebolas = tk.Frame(janela, width=800, height=600, bg="#3A8C73")
frame_pokebolas.pack()

imagem_caixaTexto2 = Label(frame_pokebolas, bg="#3A8C73")
imagem_caixaTexto2.place(x=30, y=50)

imagem_mesaPokebola = Label(frame_pokebolas, bg="#3A8C73")
imagem_mesaPokebola.place(x=60, y=150)

imagem_pokebola1 = Label(frame_pokebolas, bg="#88c088")
imagem_pokebola1.place(x=150, y=220)

imagem_pokebola2 = Label(frame_pokebolas, bg="#88c088")
imagem_pokebola2.place(x=345, y=220)

imagem_pokebola3 = Label(frame_pokebolas, bg="#88c088")
imagem_pokebola3.place(x=540, y=220)

#Mensagem da caixa de texto
lbl_escolhaPokemon = Label(frame_pokebolas, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolhaPokemon.place(x=72, y=78)

#Botões para escolher o pokemon inicial
btn_bulbasaurInicial = tk.Button(frame_pokebolas,command=lambda: evento_botao_pokemon_inicial(nome="Bulbasaur"), text="Bulbasaur", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_bulbasaurInicial.place(x=220, y=400,anchor="center")

btn_squirtleInicial = tk.Button(frame_pokebolas,command=lambda: evento_botao_pokemon_inicial(nome="Squirtle"), text="Squirtle", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_squirtleInicial.place(x=415, y=400, anchor="center")

btn_charmanderInicial = tk.Button(frame_pokebolas,  command=lambda: evento_botao_pokemon_inicial(nome="Charmander"), text="Charmander", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_charmanderInicial.place(x=608, y=400, anchor="center")

lbl_escolheuBulbasaur = Label(frame_pokebolas, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuBulbasaur.place(x=130, y=90)

lbl_escolheuSquirtle = Label(frame_pokebolas, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuSquirtle.place(x=130, y=90)

lbl_escolheuCharmander = Label(frame_pokebolas, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuCharmander.place(x=130, y=90)

imagem_bulbasauro = Label(frame_pokebolas, bg="#88c088")
imagem_bulbasauro.place(x=150, y=220)

imagem_squirtle = Label(frame_pokebolas, bg="#88c088")
imagem_squirtle.place(x=345, y=230)

imagem_charmander = Label(frame_pokebolas, bg="#88c088")
imagem_charmander.place(x=540, y=230)

#Frame menu
frame_menu = Frame(janela, width=800, height=600, bg="#474c86")
frame_menu.pack()

image_border_main_menu = Image.open("imagens/borda-menu-principal.png")
image_border_main_menu = image_border_main_menu.resize((650, 150))
image_border_main_menu = ImageTk.PhotoImage(image_border_main_menu)
imagem_borda_menu_principal = Label(frame_menu, image=image_border_main_menu, bg="#474c86")
imagem_borda_menu_principal.place(x=80, y=30)

lbl_menu_principal = Label(frame_menu, text="Menu Principal", relief="flat", width=18, height=1, font=("Fixedsys 34"), fg="#20506E", bg="#d8e3e3")
lbl_menu_principal.place(x=120, y=80)

#Frame caverna
frame_caverna = tk.Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_caverna.pack()

imagem_caverna = tk.Canvas(janela, width=800, height=600)
imagem_caverna.pack()

#Frame pokedex
frame_pokedex = Frame(janela, width=800, height=600, bg ="#d93035")
frame_pokedex.pack()

#Teça da pokedex
frame_pokedex = Frame(janela, width=800, height=600, bg ="#d93035")
frame_pokedex.pack()

pokedex = [
    #Name, imagem, Primary Type,Secondary type,Attack,Defense,HP,Sp.Attack,Sp.Defense,Speed,Total
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
lbl_borderImage = Label(frame_pokedex, image=borderImage, bg="#d93035")
lbl_borderImage.place(x=400, y=20)

infoImage = Image.open("imagens/info.png")
infoImage = infoImage.resize((750, 250))
infoImage = ImageTk.PhotoImage(infoImage)
lbl_infoImage = Label(frame_pokedex, image=infoImage, bg="#d93035")
lbl_infoImage.place(x=330, y=580)

lbl_name = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 30 bold"), fg="black", bg="#e3e3e3")
lbl_name.place(x=780, y=485)

lbl_image = Label(frame_pokedex, bg="#598f60")
lbl_image.place(x=473, y=90)

#Habilidade do Pokemons
lbl_habilities = Label(frame_pokedex, text="Habilidade", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black", bg="#8dc73f")
lbl_habilities.place(x=790, y=610)

lbl_type = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black", bg="#8dc73f")
lbl_type.place(x=790, y=650)

lbl_secondtype = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 17"), fg="black", bg="#8dc73f")
lbl_secondtype.place(x=790, y=680)

#Informações do Pokemon
lbl_status = Label(frame_pokedex, text="Status", relief="flat", anchor=CENTER, font=("Fixedsys 23"), fg="black", bg="#8dc73f")
lbl_status.place(x=400, y=610)

lbl_hp = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_hp.place(x=400, y=650)

lbl_attack = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_attack.place(x=400, y=680)

lbl_defense = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_defense.place(x=400, y=710)

lbl_spAttack = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_spAttack.place(x=400, y=740)

lbl_spDefense = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_spDefense.place(x=400, y=770)

lbl_speed = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_speed.place(x=540, y=650)

lbl_total = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 15"), fg="black", bg="#8dc73f")
lbl_total.place(x=540, y=680)

#Botoes para Cada Pokemon
imageBulbasaurIcone = Image.open("imagens/icone-bulbasaur.png")
imageBulbasaurIcone = imageBulbasaurIcone.resize((60, 63))
imageBulbasaurIcone = ImageTk.PhotoImage(imageBulbasaurIcone)
btn_Bulbasaur = Button(frame_pokedex, command=lambda: atualizar_informacoes_pokedex(nome="Bulbasaur"), image=imageBulbasaurIcone, text=(f"Bulbasaur "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Bulbasaur.place(x=10, y=100)

imageCharmanderIcone = Image.open("imagens/icone-charmander.png")
imageCharmanderIcone = imageCharmanderIcone.resize((60, 63))
imageCharmanderIcone = ImageTk.PhotoImage(imageCharmanderIcone)
btn_Charmander = Button(frame_pokedex,command=lambda: atualizar_informacoes_charmander(btn_Charmander), image=imageCharmanderIcone, text=(f"Charmander"), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Charmander.place(x=10, y=160)

imageSquirtleIcone = Image.open("imagens/icone-squirtle.png")
imageSquirtleIcone = imageSquirtleIcone.resize((60, 63))
imageSquirtleIcone = ImageTk.PhotoImage(imageSquirtleIcone)
btn_Squirtle= Button(frame_pokedex,command=lambda: atualizar_informacoes_squirtle(btn_Squirtle), image=imageSquirtleIcone, text=(f"Squirtle  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Squirtle.place(x=10, y=220)

imageCaterpieIcone = Image.open("imagens/icone-caterpie.png")
imageCaterpieIcone = imageCaterpieIcone.resize((60, 63))
imageCaterpieIcone = ImageTk.PhotoImage(imageCaterpieIcone)
btn_Caterpie= Button(frame_pokedex,command=lambda: atualizar_informacoes_caterpie(btn_Caterpie), image=imageCaterpieIcone, text=(f"Caterpie  "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Caterpie.place(x=10, y=280)

imageWeedleIcone = Image.open("imagens/icone-weedle.png")
imageWeedleIcone = imageWeedleIcone.resize((60, 63))
imageWeedleIcone = ImageTk.PhotoImage(imageWeedleIcone)
btn_Weedle= Button(frame_pokedex, command=lambda: atualizar_informacoes_weedle(btn_Weedle), image=imageWeedleIcone, text=(f"Weedle    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Weedle.place(x=10, y=340)

imagePidgeyIcone = Image.open("imagens/icone-pidgey.png")
imagePidgeyIcone = imagePidgeyIcone.resize((60, 63))
imagePidgeyIcone = ImageTk.PhotoImage(imagePidgeyIcone)
btn_Pidgey= Button(frame_pokedex, command=lambda: atualizar_informacoes_pidgey(btn_Pidgey), image=imagePidgeyIcone, text=(f"Pidgey    "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pidgey.place(x=10, y=400)

imageSpearowIcone = Image.open("imagens/icone-spearow.png")
imageSpearowIcone = imageSpearowIcone.resize((60, 63))
imageSpearowIcone = ImageTk.PhotoImage(imageSpearowIcone)
btn_Spearow= Button(frame_pokedex, command=lambda: atualizar_informacoes_spearow(btn_Spearow), image=imageSpearowIcone, text=(f"Spearow   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Spearow.place(x=10, y=460)

imageRattataIcone = Image.open("imagens/icone-rattata.png")
imageRattataIcone = imageRattataIcone.resize((60, 63))
imageRattataIcone = ImageTk.PhotoImage(imageRattataIcone)
btn_Rattata= Button(frame_pokedex,command=lambda: atualizar_informacoes_rattata(btn_Rattata), image=imageRattataIcone, text=(f"Rattata   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Rattata.place(x=10, y=520)

imageEkansIcone = Image.open("imagens/icone-ekans.png")
imageEkansIcone = imageEkansIcone.resize((60, 63))
imageEkansIcone = ImageTk.PhotoImage(imageEkansIcone)
btn_Ekans = Button(frame_pokedex, command=lambda: atualizar_informacoes_ekans(btn_Ekans), image=imageEkansIcone, text=(f"Ekans     "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Ekans.place(x=10, y=580)

imagePikachuIcone = Image.open("imagens/icone-pikachu.png")
imagePikachuIcone = imagePikachuIcone.resize((60, 63))
imagePikachuIcone = ImageTk.PhotoImage(imagePikachuIcone)
btn_Pikachu = Button(frame_pokedex, command=lambda: atualizar_informacoes_pikachu(btn_Pikachu), image=imagePikachuIcone, text=(f"Pikachu   "), width=160, height=55, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 15"), bg='white', fg='black')
btn_Pikachu.place(x=10, y=640)

iniciar_jogo()
janela.mainloop()