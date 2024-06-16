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

pokebolas = 3
mochilas = []

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
 
def evento_botao_pokemon_inicial(nome, pokebolas):
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
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2, pokebolas=3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
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
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2, pokebolas=3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
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
                    btn_proximo2 = tk.Button(frame_pokebolas, command=lambda:iniciar_menu(btn_proximo2, pokebolas=3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=650, y=387)

def encontrar_pokebolas():
    num = random.randint(0,2)
    return num

def sorteio_pokemon(lista_pokemons):
    indice_sorteado = random.randint(0, len(lista_pokemons)-1)
    pokemon_sorteado = lista_pokemons[indice_sorteado]
    return pokemon_sorteado

def iniciar_menu(event, pokebolas):
    frame_pokebolas.destroy()

    btn_caverna = Button(frame_menu, text="Entrar na caverna", command=lambda:entrar_caverna(btn_caverna, pokebolas), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_caverna.place(x=290, y=200)

    btn_mato = Button(frame_menu, text="Entrar no mato", command=lambda:entrar_mato(btn_mato, pokebolas), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_mato.place(x=290, y=270)

    btn_pokedex = Button(frame_menu, text="Pokédex",command=lambda:mostrar_pokedex(btn_pokedex), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_pokedex.place(x=290, y=340)

    btn_mochila = Button(frame_menu, text="Mostrar Mochila",command=lambda:mostrar_mochila(btn_mochila), width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_mochila.place(x=290, y=410)

    btn_sair = tk.Button(frame_menu, text="Sair", command=janela.destroy, width=20, height=1, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 15"), bg="#ffdf00", fg="#6E5820")
    btn_sair.place(x=290, y=480)

def entrar_caverna(event, pokebolas):
    frame_menu.pack_forget()
    frame_entrarCaverna.pack()

    pokebolas_encontradas = encontrar_pokebolas()
    pokebolas += pokebolas_encontradas
    lbl_pokebolasCaverna.config(text=f"Você encontrou {pokebolas_encontradas} Pokébolas")
    image_textBox3 = Image.open("imagens/caixa-texto3.png")
    image_textBox3 = image_textBox3.resize((620, 80))
    image_textBox3 = ImageTk.PhotoImage(image_textBox3)
    imagem_caixaTexto3.config(image=image_textBox3)
    imagem_caixaTexto3.image_types = image_textBox3

    image_cave1 = Image.open("imagens/caverna.png")
    image_cave1 = image_cave1.resize((800, 600))
    image_cave1 = ImageTk.PhotoImage(image_cave1)
    imagem_caverna1.create_image(0,0, anchor="nw", image=image_cave1)
    imagem_caverna1.image_types = image_cave1

def menu_caverna(event, pokebolas):
    frame_entrarCaverna.destroy()

    image_cave2 = Image.open("imagens/caverna.png")
    image_cave2 = image_cave2.resize((800, 600))
    image_cave2 = ImageTk.PhotoImage(image_cave2)
    imagem_caverna2.create_image(0,0, anchor="nw", image=image_cave2)
    imagem_caverna2.image_types = image_cave2

    pokemonsCaverna = ["Weedle","Rattata","Ekans"]
    pokemon = sorteio_pokemon(pokemonsCaverna)
    lbl_pokemonCaverna.config(text=f"Um {pokemon} selvagem apareceu!\n"
                              "O que você deseja fazer?")
    image_textBox4 = Image.open("imagens/caixa-texto3.png")
    image_textBox4 = image_textBox4.resize((620, 80))
    image_textBox4 = ImageTk.PhotoImage(image_textBox4)
    imagem_caixaTexto4.config(image=image_textBox4)
    imagem_caixaTexto4.image_types = image_textBox4

    image_cave_menu = Image.open("imagens/caixa-texto3.png")
    image_cave_menu = image_cave_menu.resize((170, 150))
    image_cave_menu = ImageTk.PhotoImage(image_cave_menu)
    imagem_menuCaverna.config(image=image_cave_menu)
    imagem_menuCaverna.image_types = image_cave_menu

def entrar_mato(event):
    print("Oi")

def entrar_mato(pokemon):
    frame_menu.pack_forget
    frame_entrarCaverna.pack()

def mostrar_pokedex(event):
    frame_menu.pack_forget()
    frame_pokedex.pack()

def pokedex_to_menu(event):
    frame_pokedex.pack_forget()
    frame_menu.pack()

'''def caverna_to_menu(event):
    frame_caverna.pack_forget()
    frame_menu.pack()

def mato_to_menu(event):
    frame_mato.pack_forget()
    frame_menu.pack()'''

def mostrar_mochila(event):
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
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
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)

##Tentando fazer uma função para todos os pokemons, acredito que vai precisar, mas essa aqui em baixo ainda n funciona

'''def atualizar_informacoes_pokedex(nome):
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
                    # Atualizar imagem
                    imagePokemon = Image.open(linha)
                    imagePokemon = imagePokemon.resize((476, 373))
                    imagePokemon = ImageTk.PhotoImage(imagePokemon)
                    lbl_image.config(image=imagePokemon)
                    lbl_image.image_types(imagePokemon)
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

#Talvez isso ajude:
    elif nome == 'Squirtle':
        with open("pokemonsIniciais.csv", "r") as pokemons_data:
            dados_pokemons = csv.reader(pokemons_data, delimiter=",")
            for i, linha in enumerate(dados_pokemons):
                if i == 2:'''

###Precisa definir as variaveis no programa principal, igual ta daqui para baixo, pois quando a gente clica em um botão
### e vai para uma próxima tela, usamos o .destroy() para excluir as coisas da tela anterior
### Caso a variável não seja definida no programa principal, o .destroy() não funciona

janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("800x600")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)
janela.config(bg ="#d93035")

'''pokedex = []'''

#Tela inicial
imagem_telaInicial = tk.Canvas(janela, width=800, height=600)
imagem_telaInicial.pack()

btn_jogar = tk.Button(janela, command=lambda:exibir_fala_professor(btn_jogar), text="", width=5, height=0, relief="raised", anchor=NW, padx=10, pady=1, font=("Fixedsys 33"), bg='black', fg='white')
btn_jogar.place(x=230, y=450)

#Tela da fala do professor Carvalho
frame_falaprofessor = tk.Frame(janela, width=800, height=600, bg="#76a2b4")
frame_falaprofessor.pack()

imagem_fundoProfessor = Label(frame_falaprofessor, bg="#76a2b4")
imagem_fundoProfessor.place(x=0, y=0)

imagem_caixaTexto = Label(frame_falaprofessor, bg="#587873")
imagem_caixaTexto.place(x=55, y=350)

lbl_fala = Label(frame_falaprofessor, text="",  relief="flat", pady=5, font=("Fixedsys 17"), fg="black", bg="#d8e3e3")
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
lbl_escolhaPokemon = Label(frame_pokebolas, text="", relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolhaPokemon.place(x=72, y=78)

#Botões para escolher o pokemon inicial
btn_bulbasaurInicial = tk.Button(frame_pokebolas,command=lambda: evento_botao_pokemon_inicial(nome="Bulbasaur", pokebolas=3), text="Bulbasaur", width=10, height=0, relief="raised", anchor="center", padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_bulbasaurInicial.place(x=127, y=380)

btn_squirtleInicial = tk.Button(frame_pokebolas,command=lambda: evento_botao_pokemon_inicial(nome="Squirtle", pokebolas=3), text="Squirtle", width=10, height=0, relief="raised", anchor="center", padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_squirtleInicial.place(x=324, y=380)

btn_charmanderInicial = tk.Button(frame_pokebolas,  command=lambda: evento_botao_pokemon_inicial(nome="Charmander", pokebolas=3), text="Charmander", width=10, height=0, relief="raised", anchor="center", padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_charmanderInicial.place(x=520, y=380)

lbl_escolheuBulbasaur = Label(frame_pokebolas, text="", relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuBulbasaur.place(x=130, y=90)

lbl_escolheuSquirtle = Label(frame_pokebolas, text="", relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuSquirtle.place(x=130, y=90)

lbl_escolheuCharmander = Label(frame_pokebolas, text="", relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
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

#Frame entrar na caverna
frame_entrarCaverna = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_entrarCaverna.pack()

imagem_caverna1 = tk.Canvas(frame_entrarCaverna, width=800, height=600)
imagem_caverna1.pack()

imagem_caixaTexto3 = Label(frame_entrarCaverna, bg="#587873")
imagem_caixaTexto3.place(x=88, y=50)

lbl_pokebolasCaverna = Label(frame_entrarCaverna, text="", relief="flat", font=("Fixedsys 17"), fg="#20506E", bg="#ECECEC")
lbl_pokebolasCaverna.place(x=275, y=78)

btn_proximo3 = tk.Button(frame_entrarCaverna, command=lambda:menu_caverna(btn_proximo3, pokebolas), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo3.place(x=625, y=70)

#Frame menu caverna
frame_menuCaverna = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_menuCaverna.pack()

imagem_caverna2 = tk.Canvas(frame_menuCaverna, width=800, height=600)
imagem_caverna2.pack()

imagem_caixaTexto4 = Label(frame_menuCaverna, bg="#587873")
imagem_caixaTexto4.place(x=88, y=50)

lbl_pokemonCaverna = Label(frame_menuCaverna, text="", relief="flat", font=("Fixedsys 17"), fg="#20506E", bg="#ECECEC")
lbl_pokemonCaverna.place(x=270, y=68)

imagem_menuCaverna = Label(frame_menuCaverna, bg="#ECECEC")
imagem_menuCaverna.place(x=535, y=220)

btn_capturarCaverna = tk.Button(frame_menuCaverna, command=lambda: capturar_pokemonCaverna(nome, pokebolas), text="Capturar", width=8, height=0, relief="raised", anchor="center", padx=30, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_capturarCaverna.place(x=548, y=250)

btn_capturarCaverna = tk.Button(frame_menuCaverna, command=lambda: cave_to_menu(pokebolas), text="Fugir", width=8, height=0, relief="raised", anchor="center", padx=30, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_capturarCaverna.place(x=548, y=300)

#TELA DA POKEDEX#
frame_pokedex = Frame(janela, width=1200, height=1000, bg ="#d93035")
frame_pokedex.pack()

pokedex = [
    #Name, imagem, Primary Type,Secondary type,Attack,Defense,HP,Sp.Attack,Sp.Defense,Speed,Total
    ['Bulbasaur','imagens/bulbasaur.png', 'GRASS','POISON',49,49,45,65,65,45,318,],
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
borderImage = borderImage.resize((420, 360))
borderImage = ImageTk.PhotoImage(borderImage)
lbl_borderImage = Label(frame_pokedex, image=borderImage, bg="#d93035")
lbl_borderImage.place(x=260, y=20)

infoImage = Image.open("imagens/info.png")
infoImage = infoImage.resize((550, 200))
infoImage = ImageTk.PhotoImage(infoImage)
lbl_infoImage = Label(frame_pokedex, image=infoImage, bg="#d93035")
lbl_infoImage.place(x=200, y=390)

lbl_name = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 18 "), fg="black", bg="#e3e3e3")
lbl_name.place(x=510, y=335)

lbl_image = Label(frame_pokedex, bg="#598f60")
lbl_image.place(x=315, y=73)

image_back = Image.open("imagens/setinha-voltar.png")
image_back = image_back.resize((45, 30))
image_back = ImageTk.PhotoImage(image_back)
btn_voltar = Button(frame_pokedex, command=lambda:pokedex_to_menu(btn_voltar), image=image_back, width=45, height=30, relief="raised", anchor=NW, padx=1, pady=1, bg='#e3e3e3')
btn_voltar.place(x=15, y=30)

#Habilidade  do Pokemons
lbl_habilities = Label(frame_pokedex, text="Habilidade", relief="flat", anchor=CENTER, font=("Fixedsys 13"), fg="black", bg="#8dc73f")
lbl_habilities.place(x=522, y=420)

lbl_type = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_type.place(x=522, y=445)

lbl_secondtype = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_secondtype.place(x=522, y=470)

#Atributos de cada Pokemon
lbl_status = Label(frame_pokedex, text="Status", relief="flat", anchor=CENTER, font=("Fixedsys 13"), fg="black", bg="#8dc73f")
lbl_status.place(x=250, y=420)

lbl_hp = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_hp.place(x=250, y=445)

lbl_attack = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_attack.place(x=250, y=470)

lbl_defense = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_defense.place(x=250, y=495)

lbl_spAttack = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_spAttack.place(x=250, y=520)

lbl_spDefense = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_spDefense.place(x=250, y=545)

lbl_speed = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_speed.place(x=380, y=445)

lbl_total = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_total.place(x=380, y=470)

#Botoes para cada Pokemon
imageBulbasaurIcone = Image.open("imagens/icone-bulbasaur.png")
imageBulbasaurIcone = imageBulbasaurIcone.resize((40, 43))
imageBulbasaurIcone = ImageTk.PhotoImage(imageBulbasaurIcone)
btn_Bulbasaur = Button(frame_pokedex, command=lambda: atualizar_informacoes_bulbasaur(btn_Bulbasaur), image=imageBulbasaurIcone, text=(f"Bulbasaur "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Bulbasaur.place(x=10, y=80)

imageCharmanderIcone = Image.open("imagens/icone-charmander.png")
imageCharmanderIcone = imageCharmanderIcone.resize((40, 43))
imageCharmanderIcone = ImageTk.PhotoImage(imageCharmanderIcone)
btn_Charmander = Button(frame_pokedex,command=lambda: atualizar_informacoes_charmander(btn_Charmander), image=imageCharmanderIcone, text=(f"Charmander"), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Charmander.place(x=10, y=130)

imageSquirtleIcone = Image.open("imagens/icone-squirtle.png")
imageSquirtleIcone = imageSquirtleIcone.resize((40, 43))
imageSquirtleIcone = ImageTk.PhotoImage(imageSquirtleIcone)
btn_Squirtle= Button(frame_pokedex,command=lambda:atualizar_informacoes_squirtle(btn_Squirtle), image=imageSquirtleIcone, text=(f"Squirtle  "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Squirtle.place(x=10, y=180)

imageCaterpieIcone = Image.open("imagens/icone-caterpie.png")
imageCaterpieIcone = imageCaterpieIcone.resize((40, 43))
imageCaterpieIcone = ImageTk.PhotoImage(imageCaterpieIcone)
btn_Caterpie= Button(frame_pokedex,command=lambda:atualizar_informacoes_caterpie(btn_Caterpie), image=imageCaterpieIcone, text=(f"Caterpie  "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Caterpie.place(x=10, y=230)

imageWeedleIcone = Image.open("imagens/icone-weedle.png")
imageWeedleIcone = imageWeedleIcone.resize((40, 43))
imageWeedleIcone = ImageTk.PhotoImage(imageWeedleIcone)
btn_Weedle= Button(frame_pokedex, command=lambda:atualizar_informacoes_weedle(btn_Weedle), image=imageWeedleIcone, text=(f"Weedle    "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Weedle.place(x=10, y=280)

imagePidgeyIcone = Image.open("imagens/icone-pidgey.png")
imagePidgeyIcone = imagePidgeyIcone.resize((40, 43))
imagePidgeyIcone = ImageTk.PhotoImage(imagePidgeyIcone)
btn_Pidgey= Button(frame_pokedex, command=lambda:atualizar_informacoes_pidgey(btn_Pidgey), image=imagePidgeyIcone, text=(f"Pidgey    "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Pidgey.place(x=10, y=330)

imageSpearowIcone = Image.open("imagens/icone-spearow.png")
imageSpearowIcone = imageSpearowIcone.resize((40, 43))
imageSpearowIcone = ImageTk.PhotoImage(imageSpearowIcone)
btn_Spearow= Button(frame_pokedex, command=lambda:atualizar_informacoes_spearow(btn_Spearow), image=imageSpearowIcone, text=(f"Spearow   "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Spearow.place(x=10, y=380)

imageRattataIcone = Image.open("imagens/icone-rattata.png")
imageRattataIcone = imageRattataIcone.resize((40, 43))
imageRattataIcone = ImageTk.PhotoImage(imageRattataIcone)
btn_Rattata= Button(frame_pokedex,command=lambda:atualizar_informacoes_rattata(btn_Rattata), image=imageRattataIcone, text=(f"Rattata   "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Rattata.place(x=10, y=430)

imageEkansIcone = Image.open("imagens/icone-ekans.png")
imageEkansIcone = imageEkansIcone.resize((40, 43))
imageEkansIcone = ImageTk.PhotoImage(imageEkansIcone)
btn_Ekans = Button(frame_pokedex, command=lambda:atualizar_informacoes_ekans(btn_Ekans), image=imageEkansIcone, text=(f"Ekans     "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Ekans.place(x=10, y=480)

imagePikachuIcone = Image.open("imagens/icone-pikachu.png")
imagePikachuIcone = imagePikachuIcone.resize((40, 43))
imagePikachuIcone = ImageTk.PhotoImage(imagePikachuIcone)
btn_Pikachu = Button(frame_pokedex, command=lambda:atualizar_informacoes_pikachu(btn_Pikachu), image=imagePikachuIcone, text=(f"Pikachu   "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Pikachu.place(x=10, y=530)

iniciar_jogo()
janela.mainloop()