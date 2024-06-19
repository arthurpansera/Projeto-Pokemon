import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
from pygame import mixer

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
    mixer.init()
    mixer.music.load("tela-inicial-music.mp3")
    mixer.music.play()
    input()
    

def exibir_fala_professor(event):
    mixer.music.stop()
    mixer.quit()
    btn_jogar.destroy()
    imagem_telaInicial.destroy()

    lbl_fala.config(text="Olá! Eu sou o Professor Carvalho, um pesquisador Pokémon.\n"
                                "Esse mundo é habitado por várias criaturas chamadas de Pokémon.\n"
                                "Algumas pessoas os tratam como mascotes, outras usam em batalhas.")

    image_textBox = Image.open("imagens/caixa-texto.png")
    image_textBox = image_textBox.resize((700, 130))
    image_textBox = ImageTk.PhotoImage(image_textBox)
    imagem_caixaTexto.config(image=image_textBox)
    imagem_caixaTexto.image_types = image_textBox

    image_teacher = Image.open("imagens/professor-carvalho.png")
    image_teacher = image_teacher.resize((250, 300))
    image_teacher = ImageTk.PhotoImage(image_teacher)
    imagem_professor.config(image=image_teacher)
    imagem_professor.image_types = image_teacher

    image_backgroundTeacher = Image.open("imagens/imagem-fundo-professor.jpg")
    image_backgroundTeacher = image_backgroundTeacher.resize((800, 670))
    image_backgroundTeacher = ImageTk.PhotoImage(image_backgroundTeacher)
    imagem_fundoProfessor.config(image=image_backgroundTeacher)
    imagem_fundoProfessor.image_types = image_backgroundTeacher  


def escolher_pokemon_inicial(event):
    frame_falaprofessor.destroy()
    # Criar tela para escolha do Pokémon inicial
    
    image_tablePokeball = Image.open("imagens/mesa-pokebola.png")
    image_tablePokeball = image_tablePokeball.resize((670, 365))
    image_tablePokeball = ImageTk.PhotoImage(image_tablePokeball)
    imagem_mesaPokebola.config(image=image_tablePokeball)
    imagem_mesaPokebola.image_types = image_tablePokeball

    image_pokeball1 = Image.open("imagens/pokebola1.png")
    image_pokeball1 = image_pokeball1.resize((110, 110))
    image_pokeball1 = ImageTk.PhotoImage(image_pokeball1)
    imagem_pokebola1.config(image=image_pokeball1)
    imagem_pokebola1.image_types = image_pokeball1

    image_pokeball2 = Image.open("imagens/pokebola2.png")
    image_pokeball2 = image_pokeball2.resize((110, 110))
    image_pokeball2 = ImageTk.PhotoImage(image_pokeball2)
    imagem_pokebola2.config(image=image_pokeball2)
    imagem_pokebola2.image_types = image_pokeball2

    image_pokeball3 = Image.open("imagens/pokebola3.png")
    image_pokeball3 = image_pokeball3.resize((110, 110))
    image_pokeball3 = ImageTk.PhotoImage(image_pokeball3)
    imagem_pokebola3.config(image=image_pokeball3)
    imagem_pokebola3.image_types = image_pokeball3

    image_textBox2 = Image.open("imagens/caixa-texto2.png")
    image_textBox2 = image_textBox2.resize((700, 90))
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

                    image_proximo2 = Image.open("imagens/proximo.png")
                    image_proximo2 = image_proximo2.resize((25, 20))
                    image_proximo2 = ImageTk.PhotoImage(image_proximo2)
                    btn_proximo2 = tk.Button(frame_pokemonInicial, command=lambda:iniciar_menu(btn_proximo2, pokebolas = 3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=680, y=68)

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

                    image_proximo2 = Image.open("imagens/proximo.png")
                    image_proximo2 = image_proximo2.resize((25, 20))
                    image_proximo2 = ImageTk.PhotoImage(image_proximo2)
                    btn_proximo2 = tk.Button(frame_pokemonInicial, command=lambda:iniciar_menu(btn_proximo2, pokebolas = 3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=680, y=68)

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

                    image_proximo2 = Image.open("imagens/proximo.png")
                    image_proximo2 = image_proximo2.resize((25, 20))
                    image_proximo2 = ImageTk.PhotoImage(image_proximo2)
                    btn_proximo2 = tk.Button(frame_pokemonInicial, command=lambda:iniciar_menu(btn_proximo2, pokebolas = 3), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
                    btn_proximo2.place(x=680, y=68)


pokebolas = 3
probCaverna = 0.35
probMato = 0.5
probPikachu = 0.02

def encontrar_pokebolas():
    num = random.randint(0,2)
    return num


def sorteio_pokemon_caverna(lista_pokemons):
    indice_sorteado = random.randint(0, len(lista_pokemons) - 1)
    pokemon_sorteado = lista_pokemons[indice_sorteado]
    return pokemon_sorteado


def sorteio_pokemon_mato(lista_pokemons, probPikachu):
    indice_sorteado = random.randint(0, len(lista_pokemons) - 1)
    if indice_sorteado < probPikachu:
        return "Pikachu"
    else:
        pokemon_sorteado = lista_pokemons[indice_sorteado]
        return pokemon_sorteado
    
pokemonsMato = ["Pikachu","Pidgey","Spearow", "Caterpie"]
pokemonMato = sorteio_pokemon_mato(pokemonsMato,probPikachu)

pokemonsCaverna = ["Weedle","Rattata","Ekans"]
pokemonCave = sorteio_pokemon_caverna(pokemonsCaverna)

def entrar_caverna(event):
    global pokebolas
    frame_menu.pack_forget()
    frame_entrarCaverna.pack()

    pokebolas_encontradas = encontrar_pokebolas()
    if pokebolas_encontradas == 1:
        pokebolas += 1
        lbl_pokebolasCaverna.config(text=f"Você encontrou 1 Pokébola")
    elif pokebolas_encontradas == 2:
        pokebolas += 2
        lbl_pokebolasCaverna.config(text=f"Você encontrou 2 Pokébolas")
    else:
        lbl_pokebolasCaverna.config(text=f"Você não encontrou Pokébolas")

    image_cave1 = Image.open("imagens/caverna.png")
    image_cave1 = image_cave1.resize((800, 600))
    image_cave1 = ImageTk.PhotoImage(image_cave1)
    imagem_caverna1.create_image(0,0, anchor="nw", image=image_cave1)
    imagem_caverna1.image_types = image_cave1

    image_textBox3 = Image.open("imagens/caixa-texto3.png")
    image_textBox3 = image_textBox3.resize((620, 80))
    image_textBox3 = ImageTk.PhotoImage(image_textBox3)
    imagem_caixaTexto3.config(image=image_textBox3)
    imagem_caixaTexto3.image_types = image_textBox3


def menu_caverna(event, pokebolas):
    frame_entrarCaverna.pack_forget()
    frame_menuCaverna.pack()

    image_cave2 = Image.open("imagens/captura-caverna.jpg")
    image_cave2 = image_cave2.resize((800, 600))
    image_cave2 = ImageTk.PhotoImage(image_cave2)
    imagem_caverna2.create_image(0,0, anchor="nw", image=image_cave2)
    imagem_caverna2.image_types = image_cave2

    lbl_pokemonCaverna2.config(text=f"Um {pokemonCave} selvagem apareceu!\n"
                              "O que você deseja fazer?")

    if pokemonCave == "Weedle":
        image_capWeedle = Image.open("imagens/weedle-captura.png")
        image_capWeedle = image_capWeedle.resize((130, 130))
        image_capWeedle = ImageTk.PhotoImage(image_capWeedle)
        imagem_CapWeedle.config(image=image_capWeedle)
        imagem_CapWeedle.image_types = image_capWeedle

    elif pokemonCave == "Rattata":
        image_capEkans = Image.open("imagens/rattata-captura.png")
        image_capEkans = image_capEkans.resize((130, 130))
        image_capEkans = ImageTk.PhotoImage(image_capEkans)
        imagem_CapEkans.config(image=image_capEkans)
        imagem_CapEkans.image_types = image_capEkans
    elif pokemonCave == "Ekans":
        image_capEkans = Image.open("imagens/ekans-captura.png")
        image_capEkans = image_capEkans.resize((130, 130))
        image_capEkans = ImageTk.PhotoImage(image_capEkans)
        imagem_CapEkans.config(image=image_capEkans)
        imagem_CapEkans.image_types = image_capEkans

def capturar_pokemon_caverna(nome):
        global pokebolas
        frame_pokedex.pack_forget()
        frame_menuCaverna.pack_forget()
        frame_entrarCaverna.pack_forget()
        frame_entrarMato.pack_forget()
        frame_menuMato.pack_forget()
        frame_mochila.pack_forget()
        frame_capturaMato.pack_forget()
        frame_capturaCaverna.pack()

        image_caverna3= Image.open("imagens/captura-caverna.jpg")
        image_caverna3 = image_caverna3.resize((800, 600))
        image_caverna3 = ImageTk.PhotoImage(image_caverna3)
        imagem_caverna3.create_image(0,0, anchor="nw", image=image_caverna3)
        imagem_caverna3.image_types = image_caverna3

        if  nome == "Capturar":
            if pokebolas != 0:
                if pokemonCave not in pokedex:
                    pokebolas -= 1
                    if random.random() < probCaverna:
                        lbl_capturaCaverna.config(text=f"Você capturou o {pokemonCave}!\n*{pokemonCave} foi adicionado a sua Pokédex")
                        image_pokeball5 = Image.open("imagens/pokebola1.png")
                        image_pokeball5 = image_pokeball5.resize((75, 75))
                        image_pokeball5 = ImageTk.PhotoImage(image_pokeball5)
                        imagem_pokebola5.config(image=image_pokeball5)
                        imagem_pokebola5.image_types = image_pokeball5
                        pokedex.append(pokemonCave)
                    else:
                        lbl_capturaCaverna.config(text="*O Pokémon escapou")
                        if pokebolas == 0:
                            lbl_capturaCaverna.config(text="Você não tem mais Pokébolas.\n"
                                                    "*O Pokémon fugiu")


def entrar_mato(event):
    global pokebolas
    frame_menu.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarMato.pack()

    pokebolas_encontradas = encontrar_pokebolas()
    if pokebolas_encontradas == 1:
        pokebolas += 1
        lbl_pokebolasMato.config(text=f"Você encontrou 1 Pokébola")
    elif pokebolas_encontradas == 2:
        pokebolas += 2
        lbl_pokebolasMato.config(text=f"Você encontrou 2 Pokébolas")
    else:
        lbl_pokebolasMato.config(text=f"Você não encontrou Pokébolas")

    image_textBox4 = Image.open("imagens/caixa-texto3.png")
    image_textBox4 = image_textBox4.resize((620, 80))
    image_textBox4 = ImageTk.PhotoImage(image_textBox4)
    imagem_caixaTexto4.config(image=image_textBox4)
    imagem_caixaTexto4.image_types = image_textBox4

    image_mato = Image.open("imagens/mato.jpg")
    image_mato = image_mato.resize((800, 600))
    image_mato = ImageTk.PhotoImage(image_mato)
    imagem_Mato.create_image(0,0, anchor="nw", image=image_mato)
    imagem_Mato.image_types = image_mato


def menu_Mato(event):
    global pokebolas
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaMato.pack_forget()
    frame_menuMato.pack()

    image_mato2= Image.open("imagens/captura-mato.png")
    image_mato2 = image_mato2.resize((800, 600))
    image_mato2 = ImageTk.PhotoImage(image_mato2)
    imagem_Mato2.create_image(0,0, anchor="nw", image=image_mato2)
    imagem_Mato2.image_types = image_mato2

    lbl_pokemonMato2.config(text=f"Um {pokemonMato} selvagem apareceu!\n"
                              "O que você deseja fazer?")

    if pokemonMato == "Pikachu":
        image_capPikachu = Image.open("imagens/pikachu-captura.png")
        image_capPikachu = image_capPikachu.resize((130, 130))
        image_capPikachu = ImageTk.PhotoImage(image_capPikachu)
        imagem_CapPikachu.config(image=image_capPikachu)
        imagem_CapPikachu.image_types = image_capPikachu
    if pokemonMato == "Caterpie":
        image_capCaterpie = Image.open("imagens/caterpie-captura.png")
        image_capCaterpie = image_capCaterpie.resize((130, 130))
        image_capCaterpie = ImageTk.PhotoImage(image_capCaterpie)
        imagem_CapCaterpie.config(image=image_capCaterpie)
        imagem_CapCaterpie.image_types = image_capCaterpie
    if pokemonMato == "Pidgey":
        image_capPidgey = Image.open("imagens/pidgey-captura.png")
        image_capPidgey = image_capPidgey.resize((130, 130))
        image_capPidgey = ImageTk.PhotoImage(image_capPidgey)
        imagem_CapPidgey.config(image=image_capPidgey)
        imagem_CapPidgey.image_types = image_capPidgey
    if pokemonMato == "Spearow":
        image_capSpearow = Image.open("imagens/spearow-captura.png")
        image_capSpearow= image_capSpearow.resize((130, 130))
        image_capSpearow = ImageTk.PhotoImage(image_capSpearow)
        imagem_CapSpearow.config(image=image_capSpearow)
        imagem_CapSpearow.image_types = image_capSpearow


def capturar_pokemon_mato(nome):
        global pokebolas
        frame_pokedex.pack_forget()
        frame_menuCaverna.pack_forget()
        frame_entrarCaverna.pack_forget()
        frame_entrarMato.pack_forget()
        frame_menuMato.pack_forget()
        frame_mochila.pack_forget()
        frame_capturaCaverna.pack_forget()
        frame_capturaMato.pack()

        image_mato3= Image.open("imagens/captura-mato.png")
        image_mato3 = image_mato3.resize((800, 600))
        image_mato3 = ImageTk.PhotoImage(image_mato3)
        imagem_Mato3.create_image(0,0, anchor="nw", image=image_mato3)
        imagem_Mato3.image_types = image_mato3

        if  nome == "Capturar":
            if pokebolas != 0:
                if pokemonMato not in pokedex:
                    pokebolas -= 1
                    if random.random() < probCaverna:
                        lbl_capturaMato.config(text=f"Você capturou o {pokemonMato}!\n*{pokemonMato} foi adicionado a sua Pokédex")
                        image_pokeball4 = Image.open("imagens/pokebola1.png")
                        image_pokeball4 = image_pokeball4.resize((75, 75))
                        image_pokeball4 = ImageTk.PhotoImage(image_pokeball4)
                        imagem_pokebola4.config(image=image_pokeball4)
                        imagem_pokebola4.image_types = image_pokeball4
                        pokedex.append(pokemonMato)
                    else:
                        lbl_capturaMato.config(text="*O Pokémon escapou")
                        if pokebolas == 0:
                            lbl_capturaMato.config(text="Você não tem mais Pokébolas.\n"
                                                    "*O Pokémon fugiu")


def mostrar_mochila(event):
    frame_menu.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack()

    image_backpack = Image.open("imagens/mochila.png")
    image_backpack = image_backpack.resize((800, 600))
    image_backpack = ImageTk.PhotoImage(image_backpack)
    imagem_mochila.config(image=image_backpack)
    imagem_mochila.image_types = image_backpack

    image_pokeball = Image.open("imagens/pokebola1.png")
    image_pokeball = image_pokeball.resize((100, 100))
    image_pokeball = ImageTk.PhotoImage(image_pokeball)
    imagem_pokebola.config(image=image_pokeball)
    imagem_pokebola.image_types = image_pokeball

    lbl_pokedex.config(text=f"Pokebola             x  {pokebolas}")

    lbl_descricao_pokedex.config(text="É uma bola lançada para capturar\n"
                                    " um Pokémon selvagem.\n"
                                  "Ela foi projetada em estilo cápsula.")


def cave_to_menu():
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_menu.pack()


def mato_to_menu():
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaMato.pack_forget()
    frame_menu.pack()


def capturaMato_to_menu():
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaMato.pack_forget()
    frame_menu.pack()

def capturaCaverna_to_menu():
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaMato.pack_forget()
    frame_capturaCaverna.pack_forget()
    frame_menu.pack()


def mostrar_pokedex(event):
    frame_menu.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaCaverna.pack_forget()
    frame_capturaMato.pack_forget()
    frame_pokedex.pack()

def pokedex_to_menu(event):
    frame_pokedex.pack_forget()
    frame_menu.pack()


def mochila_to_menu(event):
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_menu.pack()


def atualizar_informacoes_bulbasaur(event):
    lbl_name.config(text=pokemons_regiao[0][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[0][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[0][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[0][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[0][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[0][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[0][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[0][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[0][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[0][10]}")
    imagePokemon = Image.open(pokemons_regiao[0][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_charmander(event):
    lbl_name.config(text=pokemons_regiao[1][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[1][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[1][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[1][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[1][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[1][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[1][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[1][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[1][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[1][10]}")
    imagePokemon = Image.open(pokemons_regiao[1][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_squirtle(event):
    lbl_name.config(text=pokemons_regiao[2][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[2][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[2][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[2][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[2][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[2][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[2][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[2][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[2][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[2][10]}")
    imagePokemon = Image.open(pokemons_regiao[2][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_caterpie(event):
    lbl_name.config(text=pokemons_regiao[3][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[3][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[3][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[3][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[3][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[3][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[3][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[3][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[3][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[3][10]}")
    imagePokemon = Image.open(pokemons_regiao[3][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_weedle(event):
    lbl_name.config(text=pokemons_regiao[4][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[4][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[4][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[4][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[4][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[4][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[4][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[4][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[4][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[4][10]}")
    imagePokemon = Image.open(pokemons_regiao[4][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_pidgey(event):
    lbl_name.config(text=pokemons_regiao[5][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[5][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[5][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[5][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[5][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[5][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[5][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[5][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[5][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[5][10]}")
    imagePokemon = Image.open(pokemons_regiao[5][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_spearow(event):
    lbl_name.config(text=pokemons_regiao[6][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[6][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[6][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[6][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[6][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[6][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[6][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[6][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[6][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[6][10]}")
    imagePokemon = Image.open(pokemons_regiao[6][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def atualizar_informacoes_rattata(event):
    lbl_name.config(text=pokemons_regiao[7][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[7][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[7][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[7][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[7][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[7][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[7][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[7][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[7][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[7][10]}")
    imagePokemon = Image.open(pokemons_regiao[7][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)
        

def atualizar_informacoes_ekans(event):
    lbl_name.config(text=pokemons_regiao[8][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[8][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[8][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[8][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[8][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[8][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[8][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[8][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[8][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[8][10]}")
    imagePokemon = Image.open(pokemons_regiao[8][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)        


def atualizar_informacoes_pikachu():
    lbl_name.config(text=pokemons_regiao[9][0])
    lbl_type.config(text=f"Tipo: {pokemons_regiao[9][2]}")
    lbl_secondtype.config(text=f"Tipo secundário: {pokemons_regiao[9][3]}")
    lbl_attack.config(text=f"Ataque: {pokemons_regiao[9][4]}")
    lbl_defense.config(text=f"Defensa: {pokemons_regiao[9][5]}")
    lbl_hp.config(text=f"HP: {pokemons_regiao[9][6]}")
    lbl_spAttack.config(text=f"Velocidade de Ataque: {pokemons_regiao[9][7]}")
    lbl_spDefense.config(text=f"Velocidade de Defesa: {pokemons_regiao[9][8]}")
    lbl_speed.config(text=f"Velocidade: {pokemons_regiao[9][9]}")
    lbl_total.config(text=f"Total: {pokemons_regiao[9][10]}")
    imagePokemon = Image.open(pokemons_regiao[9][1])
    imagePokemon = imagePokemon.resize((325, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    lbl_image.config(image=imagePokemon)
    lbl_image.image_types(imagePokemon)


def iniciar_menu(event, pokebolas):
    frame_pokemonInicial.destroy()

    btn_caverna = Button(frame_menu, text="Entrar na caverna", command=lambda:entrar_caverna(btn_caverna), width=30, height=2, relief="raised", anchor=CENTER, padx=18, pady=5, font=("Fixedsys 17 bold"), bg="#ffdf00", fg="#6E5820")
    btn_caverna.place(x=220, y=170)

    btn_mato = Button(frame_menu, text="Entrar no mato", command=lambda:entrar_mato(btn_mato), width=30, height=2, relief="raised", anchor=CENTER, padx=18, pady=5, font=("Fixedsys 17 bold"), bg="#ffdf00", fg="#6E5820")
    btn_mato.place(x=220, y=250)

    btn_pokedex = Button(frame_menu, text="Pokédex",command=lambda:mostrar_pokedex(btn_pokedex), width=30, height=2, relief="raised", anchor=CENTER, padx=18, pady=5, font=("Fixedsys 17 bold"), bg="#ffdf00", fg="#6E5820")
    btn_pokedex.place(x=220, y=330)

    btn_mochila = Button(frame_menu, text="Mostrar Mochila",command=lambda:mostrar_mochila(btn_mochila), width=30, height=2, relief="raised", anchor=CENTER, padx=18, pady=5, font=("Fixedsys 17 bold"), bg="#ffdf00", fg="#6E5820")
    btn_mochila.place(x=220, y=410)

    btn_sair = tk.Button(frame_menu, text="Sair", command=janela.destroy, width=30, height=2, relief="raised", anchor=CENTER, padx=18, pady=8, font=("Fixedsys 17 bold"), bg="#ffdf00", fg="#6E5820")
    btn_sair.place(x=220, y=490)

escolha = 0
#Definindo as variáveis
janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("800x600")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)
janela.config(bg ="#d93035")

pokedex = []
mochila = []

#TELA INICIAL
imagem_telaInicial = tk.Canvas(janela, width=800, height=600)
imagem_telaInicial.pack()

btn_jogar = tk.Button(janela, command=lambda: exibir_fala_professor(btn_jogar), text="", width=5, height=0, relief="raised", anchor=CENTER, padx=5, font=("Fixedsys 27"), bg='black', fg='white')
btn_jogar.place(x=235, y=450)

#TELA DA FALA DO PROFESSOR CARVALHO#
frame_falaprofessor = tk.Frame(janela, width=800, height=600, bg="#76a2b4")
frame_falaprofessor.pack()

imagem_fundoProfessor = Label(frame_falaprofessor, bg="#76a2b4")
imagem_fundoProfessor.place(x=0, y=0)

imagem_caixaTexto = Label(frame_falaprofessor, bg="#587873")
imagem_caixaTexto.place(x=50, y=400)

lbl_fala = Label(frame_falaprofessor, text="",  relief="flat", font=("Fixedsys 15"), fg="#20506E", bg="#d8e3e3")
lbl_fala.place(x= 75, y=430)

imagem_professor = Label(frame_falaprofessor, bg="#b9d4cd")
imagem_professor.place(x=370, y=40)

image_proximo = Image.open("imagens/proximo.png")
image_proximo = image_proximo.resize((25, 20))
image_proximo = ImageTk.PhotoImage(image_proximo)
btn_proximo = tk.Button(frame_falaprofessor, command=lambda:escolher_pokemon_inicial(btn_proximo), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo.place(x=675, y=495)

#TELA DE ESCOLHER O POKEMON INICIAL#
frame_pokemonInicial = tk.Frame(janela, width=800, height=600, bg="#3A8C73")
frame_pokemonInicial.pack()

imagem_mesaPokebola = Label(frame_pokemonInicial, bg="#3A8C73")
imagem_mesaPokebola.place(x=70, y=140)

imagem_pokebola1 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola1.place(x=157, y=210)

imagem_pokebola2 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola2.place(x=357, y=210)

imagem_pokebola3 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola3.place(x=550, y=210)

imagem_caixaTexto2 = Label(frame_pokemonInicial, bg="#3A8C73")
imagem_caixaTexto2.place(x=55, y=30)

#Botões para escolher o pokemon inicial
btn_bulbasaurInicial = Button(frame_pokemonInicial,command=lambda: evento_botao_pokemon_inicial(nome="Bulbasaur"), text="Bulbasaur", width=7, height=0, relief="raised", anchor=CENTER, padx=15, pady=2, font=("Fixedsys 15"), bg="#F0D882", fg="#6E5820")
btn_bulbasaurInicial.place(x=215, y=350,anchor="center")

btn_squirtleInicial = Button(frame_pokemonInicial,command=lambda: evento_botao_pokemon_inicial(nome="Squirtle"), text="Squirtle", width=7, height=0, relief="raised", anchor=CENTER, padx=15, pady=2, font=("Fixedsys 15"), bg="#F0D882", fg="#6E5820")
btn_squirtleInicial.place(x=415, y=350, anchor="center")

btn_charmanderInicial = Button(frame_pokemonInicial,command=lambda: evento_botao_pokemon_inicial(nome="Charmander"), text="Charmander", width=7, height=0, relief="raised", anchor=CENTER, padx=15, pady=2, font=("Fixedsys 15"), bg="#F0D882", fg="#6E5820")
btn_charmanderInicial.place(x=610, y=350, anchor="center")

#Mensagem da caixa de texto
lbl_escolhaPokemon = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 15"), fg="#20506E", bg="#d8e3e3")
lbl_escolhaPokemon.place(x=70, y=55)

lbl_escolheuBulbasaur = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 15"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuBulbasaur.place(x=99, y=67)

lbl_escolheuSquirtle = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 15"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuSquirtle.place(x=99, y=67)

lbl_escolheuCharmander = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 15"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuCharmander.place(x=99, y=67)

imagem_bulbasauro = Label(frame_pokemonInicial, bg="#88c088")
imagem_bulbasauro.place(x=140, y=200)

imagem_squirtle = Label(frame_pokemonInicial, bg="#88c088")
imagem_squirtle.place(x=350, y=200)

imagem_charmander = Label(frame_pokemonInicial, bg="#88c088")
imagem_charmander.place(x=530, y=200)

#TELA DO MENU#
frame_menu = Frame(janela, width=800, height=600, bg="#474c86")
frame_menu.pack()

image_border_main_menu = Image.open("imagens/borda-menu-principal.png")
image_border_main_menu = image_border_main_menu.resize((500, 100))
image_border_main_menu = ImageTk.PhotoImage(image_border_main_menu)
imagem_borda_menu_principal = Label(frame_menu, image=image_border_main_menu, bg="#474c86")
imagem_borda_menu_principal.place(x=155, y=40)

lbl_menu_principal = Label(frame_menu, text="Menu Principal", relief="flat", width=15, height=1, font=("Fixedsys 33 bold"), fg="#20506E", bg="#d8e3e3")
lbl_menu_principal.place(x=260, y=70)

#TELA DA CAVERNA
frame_entrarCaverna = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_entrarCaverna.pack()

imagem_caverna1 = tk.Canvas(frame_entrarCaverna, width=800, height=600)
imagem_caverna1.pack()

imagem_caixaTexto3 = Label(frame_entrarCaverna, bg="#587873")
imagem_caixaTexto3.place(x=88, y=50)

lbl_pokebolasCaverna = Label(frame_entrarCaverna, text="", relief="flat", font=("Fixedsys 17"), fg="#20506E", bg="#ECECEC")
lbl_pokebolasCaverna.place(x=275, y=78)

btn_proximo3 = tk.Button(frame_entrarCaverna, command=lambda:menu_caverna(btn_proximo3, pokebolas), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo3.place(x=625, y=78)

#menu da caverna
frame_menuCaverna = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_menuCaverna.pack()

imagem_caverna2 = tk.Canvas(frame_menuCaverna, width=800, height=600)
imagem_caverna2.pack()

imagem_CapWeedle = Label(frame_menuCaverna, bg="#bdb06e")
imagem_CapWeedle.place(x=530, y=75)

imagem_CapRattata = Label(frame_menuCaverna, bg="#bdb06e")
imagem_CapRattata.place(x=530, y=75)

imagem_CapEkans= Label(frame_menuCaverna, bg="#bdb06e")
imagem_CapEkans.place(x=530, y=75)

lbl_pokemonCaverna2 = Label(frame_menuCaverna, text="", relief="flat", font=("Fixedsys 18"), fg="white", bg="#29506d")
lbl_pokemonCaverna2.place(x=65, y=465)

btn_capturarCaverna = tk.Button(frame_menuCaverna, command=lambda: capturar_pokemon_caverna(nome="Capturar"), text="Capturar", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_capturarCaverna.place(x=590, y=460)

btn_voltarCavernaMenu = tk.Button(frame_menuCaverna, command=cave_to_menu, text="Fugir", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_voltarCavernaMenu.place(x=590, y=510)


#FRAME DE CAPTURA DO POKEMON NO MATO

frame_capturaCaverna = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_capturaCaverna.pack()

imagem_caverna3 = tk.Canvas(frame_capturaCaverna, width=800, height=600)
imagem_caverna3.pack()

btn_caverna_to_menu= tk.Button(frame_capturaCaverna, command=capturaCaverna_to_menu, text="Voltar", width=4, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_caverna_to_menu.place(x=680, y=480)

lbl_capturaCaverna = Label(frame_capturaCaverna, text="", relief="flat", font=("Fixedsys 18"), fg="white", bg="#29506d")
lbl_capturaCaverna.place(x=50, y=465)

imagem_pokebola5 = Label(frame_capturaCaverna, bg="#cec35a")
imagem_pokebola5.place(x=575, y=165)


#FRAME MATO#
frame_entrarMato = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_entrarMato.pack()

imagem_Mato = tk.Canvas(frame_entrarMato, width=800, height=600)
imagem_Mato.pack()

imagem_caixaTexto4 = Label(frame_entrarMato, bg="#587873")
imagem_caixaTexto4.place(x=88, y=50)

lbl_pokebolasMato = Label(frame_entrarMato, text="", relief="flat", font=("Fixedsys 17"), fg='#20506E', bg="#ECECEC")
lbl_pokebolasMato.place(x=275, y=78)

btn_proximo4 = tk.Button(frame_entrarMato, command=lambda:menu_Mato(btn_proximo4), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo4.place(x=625, y=78)

#Menu do Mato
frame_menuMato = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_menuMato.pack()

imagem_Mato2 = tk.Canvas(frame_menuMato, width=800, height=600)
imagem_Mato2.pack()

imagem_CapPikachu = Label(frame_menuMato, bg="#cfffd3")
imagem_CapPikachu.place(x=530, y=75)

imagem_CapCaterpie = Label(frame_menuMato, bg="#cfffd3")
imagem_CapCaterpie.place(x=530, y=75)

imagem_CapPidgey = Label(frame_menuMato, bg="#cfffd3")
imagem_CapPidgey.place(x=530, y=75)

imagem_CapSpearow= Label(frame_menuMato, bg="#cfffd3")
imagem_CapSpearow.place(x=530, y=75)

btn_capturarMato = tk.Button(frame_menuMato, command=lambda:capturar_pokemon_mato(nome="Capturar"), text="Capturar", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_capturarMato.place(x=590, y=460)

lbl_pokemonMato2 = Label(frame_menuMato, text="", relief="flat", font=("Fixedsys 18"), fg="white", bg="#29506d")
lbl_pokemonMato2.place(x=65, y=465)

btn_mato_to_menu= tk.Button(frame_menuMato, command=mato_to_menu, text="Fugir", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_mato_to_menu.place(x=590, y=510)


#FRAME DE CAPTURA DO POKEMON NO MATO

frame_capturaMato = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_capturaMato.pack()

imagem_Mato3 = tk.Canvas(frame_capturaMato, width=800, height=600)
imagem_Mato3.pack()

btn_mato_to_menu= tk.Button(frame_capturaMato, command=capturaMato_to_menu, text="Voltar", width=4, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_mato_to_menu.place(x=680, y=480)

lbl_capturaMato = Label(frame_capturaMato, text="", relief="flat", font=("Fixedsys 18"), fg="white", bg="#29506d")
lbl_capturaMato.place(x=50, y=465)

imagem_pokebola4 = Label(frame_capturaMato, bg="#a9f561")
imagem_pokebola4.place(x=575, y=165)

#TELA DA MOCHILA#
frame_mochila = Frame(janela, width=800, height=600, bg="blue")
frame_mochila.pack()

imagem_mochila= Label(frame_mochila, bg="#cfffd3")
imagem_mochila.place(x=0, y=0)

imagem_pokebola = Label(frame_mochila, bg="white")
imagem_pokebola.place(x=40, y=460)

lbl_pokedex = Label(frame_mochila, text="", width=25, height=0, relief="flat", anchor=NW, font=("Fixedsys 18"), fg="#595959", bg="#f8f8c8")
lbl_pokedex.place(x=325, y=53)

lbl_descricao_pokedex = Label(frame_mochila, text="", width=0, height=0, relief="flat", font=("Fixedsys 18 bold"), fg="white", bg="#0078c0")
lbl_descricao_pokedex.place(x=170, y=460)

btn_voltarMochilaMenu = tk.Button(frame_mochila, command=lambda:mochila_to_menu(btn_voltarMochilaMenu), text="Voltar", width=7, relief="raised" , anchor=CENTER, font=("Fixedsys 18 bold"), bg="#f8f8c8", fg="#595959")
btn_voltarMochilaMenu.place(x=388, y=123, anchor="center")

#TELA DA POKEDEX#
frame_pokedex = Frame(janela, width=800, height=600, bg ="#d93035")
frame_pokedex.pack()

pokemons_regiao = [
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
lbl_habilities = Label(frame_pokedex, text="Habilidade:", relief="flat", anchor=CENTER, font=("Fixedsys 13"), fg="black", bg="#8dc73f")
lbl_habilities.place(x=522, y=420)

lbl_type = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_type.place(x=522, y=445)

lbl_secondtype = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_secondtype.place(x=522, y=470)

#Atributos de cada Pokemon
lbl_status = Label(frame_pokedex, text="Status:", relief="flat", anchor=CENTER, font=("Fixedsys 13"), fg="black", bg="#8dc73f")
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
lbl_speed.place(x=370, y=445)

lbl_total = Label(frame_pokedex, text="", relief="flat", anchor=CENTER, font=("Fixedsys 10"), fg="black", bg="#8dc73f")
lbl_total.place(x=370, y=470)

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
btn_Pikachu = Button(frame_pokedex, command=lambda:atualizar_informacoes_pikachu(), image=imagePikachuIcone, text=(f"Pikachu   "), width=120, height=45, relief="raised", overrelief=RIDGE, compound=RIGHT, anchor=NW, padx=10, font=("Fixedsys 10"), bg='white', fg='black')
btn_Pikachu.place(x=10, y=530)

iniciar_jogo()
janela.mainloop()