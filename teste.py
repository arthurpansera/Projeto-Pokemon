import random

pokemons_regiao = [
    #Name, imagem, Primary Type,Secondary type,Attack,Defense,HP,Sp.Attack,Sp.Defense,Speed,Total
    ['Bulbasaur', 'imagens/bulbasaur.png', 'GRASS', 'POISON', 49, 49, 45, 65, 65, 45, 318],
    ['Charmander', 'imagens/charmander.png', 'FIRE', '', 52, 43, 39, 60, 50, 65, 309],
    ['Squirtle', 'imagens/squirtle.png', 'WATER', '', 48, 65, 44, 50, 64, 43, 314],
    ['Caterpie', 'imagens/caterpie.png', 'BUG', '', 30, 35, 45, 20, 20, 45, 195],
    ['Weedle', 'imagens/weedle.png', 'BUG', 'POISON', 35, 30, 40, 20, 20, 50, 195],
    ['Pidgey', 'imagens/pidgey.png', 'NORMAL', 'FLYING', 45, 40, 40, 35, 35, 56, 251],
    ['Spearow', 'imagens/spearow.png', 'NORMAL', 'FLYING', 60, 30, 40, 31, 31, 70, 262],
    ['Rattata', 'imagens/rattata.png', 'NORMAL', '', 56, 35, 30, 25, 35, 72, 253],
    ['Ekans', 'imagens/ekans.png', 'POISON', '', 60, 44, 35, 40, 54, 55, 288],
    ['Pikachu', 'imagens/pikachu.png', 'ELECTRIC', '', 55, 40, 35, 50, 50, 90, 320]
]

def iniciar_jogo():
    print("\n---------------------------- JOGO POKÉMON ----------------------------")
    print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
    print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
    print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
    nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
    print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")
    print("Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")

def encontrar_pokebolas():
    num = random.randint(0, 2)
    return num

def sorteio_pokemon_caverna(lista_pokemons):
    indice_sorteado = random.randint(0, len(lista_pokemons) - 1)
    pokemon_sorteado = lista_pokemons[indice_sorteado]
    return pokemon_sorteado

def sorteio_pokemon_mato(lista_pokemons, probPikachu):
    indice_sorteado = random.randint(0, len(lista_pokemons) - 1)
    if indice_sorteado == probPikachu:
        return "Pikachu"
    else:
        pokemon_sorteado = lista_pokemons[indice_sorteado]
        return pokemon_sorteado

def escolher_pokemon_inicial():
    pokemon_inicial = int(input("1. Bulbasaur\n2. Squirtle\n3. Charmander\nFaça sua escolha: "))
    pokedex = []
    while pokemon_inicial not in [1, 2, 3]:
        pokemon_inicial = int(input("Opção inválida. Faça sua escolha: "))
    if pokemon_inicial == 1:
        print("Ótima escolha!\n*Bulbasaur foi adicionado a sua Pokédex\n")
        pokedex.append("Bulbasaur")
    elif pokemon_inicial == 2:
        print("Ótima escolha!\n*Squirtle foi adicionado a sua Pokédex\n")
        pokedex.append("Squirtle")
    else:
        print("Ótima escolha!\n*Charmander foi adicionado a sua Pokédex\n")
        pokedex.append("Charmander")
    return pokedex


def batalhar(pokemon_luta, pokemon_selvagem):
    print(f"Seu {pokemon_luta} vai lutar contra {pokemon_selvagem}!")
    
    pokemon_luta_dados = None
    pokemon_selvagem_dados = None
    
    for pokemon in pokemons_regiao:
        if pokemon[0] == pokemon_luta:
            pokemon_luta_dados = pokemon
        if pokemon[0] == pokemon_selvagem:
            pokemon_selvagem_dados = pokemon

    if not pokemon_luta_dados or not pokemon_selvagem_dados:
        print("Erro: Pokémon não encontrado na região.")
        return
    
    speed_pokemon_luta = pokemon_luta_dados[9]
    speed_pokemon_selvagem = pokemon_selvagem_dados[9]
    
    if speed_pokemon_luta > speed_pokemon_selvagem:
        print(f"{pokemon_luta} ataca primeiro!")
        calcular_dano(pokemon_luta_dados, pokemon_selvagem_dados)
    elif speed_pokemon_luta < speed_pokemon_selvagem:
        print(f"{pokemon_selvagem} ataca primeiro!")
        calcular_dano(pokemon_selvagem_dados, pokemon_luta_dados)
    else:
        print("Ambos possuem a mesma velocidade! Vamos sortear quem ataca primeiro!")
        sorteio = random.randint(0, 1)
        if sorteio == 0:
            print(f"{pokemon_luta} ataca primeiro!")
            calcular_dano(pokemon_luta_dados, pokemon_selvagem_dados)
        else:
            print(f"{pokemon_selvagem} ataca primeiro!")
            calcular_dano(pokemon_selvagem_dados, pokemon_luta_dados)

def calcular_dano(atacante, defensor):
    print(f"\n*{atacante[0]} tem {atacante[6]} de HP, {atacante[4]} de ataque e {atacante[5]} de defesa")
    print(f"*{defensor[0]} tem {defensor[6]} de HP, {defensor[4]} de ataque e {defensor[5]} de defesa")
    danos1 = []
    danos2 = []
    
    while atacante[6] > 0 and defensor[6] > 0:
        dano1 = random.randint(0, atacante[4])
        dano2 = random.randint(0, defensor[4])
        
        defensor[6] -= dano1
        danos1.append(dano1)
        print(f"\n*{atacante[0]} causou {dano1} de dano em {defensor[0]}")
        if defensor[6] > 0:
            print(f"*{defensor[0]} está com {defensor[6]} de HP restante")
        elif defensor[6] <= 0:
            print(f"\n*{defensor[0]} foi derrotado! {atacante[0]} venceu a batalha!")
            break
            
        atacante[6] -= dano2
        danos2.append(dano2)
        print(f"\n*{defensor[0]} causou {dano2} de dano em {atacante[0]}")
        if atacante[6] > 0:
            print(f"*{atacante[0]} está com {atacante[6]} de HP restante")
        elif atacante[6] <= 0:
            print(f"\n*{atacante[0]} foi derrotado! {defensor[0]} venceu a batalha!")
            break
            
    for dano_sofrido in danos1:
        defensor[6] += dano_sofrido
    for dano_sofrido in danos2:
        atacante[6] += dano_sofrido

def menu():
    escolha = 1
    pokemonsCaverna = ["Weedle", "Rattata", "Ekans"]
    pokemonsMato = ["Caterpie", "Pidgey", "Spearow", "Pikachu"]
    probCaverna = 0.35
    probMato = 0.5
    probPikachu = 0.02
    mochila = []
    pokebolas = 3
    
    while True:
        print(70 * "-")
        print("\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar Pokémon na Pokédex\n4. Olhar itens na mochila\n5. Sair")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            pokebolas_encontradas = encontrar_pokebolas()
            if pokebolas_encontradas == 1:
                pokebolas += 1
                print("Você encontrou 1 Pokébola!")
            elif pokebolas_encontradas == 2:
                pokebolas += 2
                print("Você encontrou 2 Pokébolas!")
            else:
                print("Você não encontrou Pokébolas!")

            pokemon = sorteio_pokemon_caverna(pokemonsCaverna)
            print(f"Você entrou na caverna e encontrou um {pokemon}!")
            escolha_capturar = input("Deseja tentar capturar este Pokémon (c), batalhar com ele (b) ou fugir (f)? ")
            if escolha_capturar == "c":
                if pokebolas != 0:
                    if pokemon not in pokedex:
                        pokebolas -= 1
                        if random.random() < probCaverna:
                            print(f"Você capturou o {pokemon}!\n*{pokemon} foi adicionado a sua Pokédex")
                            pokedex.append(pokemon)
                        else:
                            print("*O Pokémon escapou")
                            if pokebolas == 0:
                                print("Você não tem mais Pokébolas.")
                                print("*O Pokémon fugiu")
                            while pokebolas > 0:
                                tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                                while tentar_nov != "s" and tentar_nov != "n":
                                    print("Comando inválido")
                                    tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                                if tentar_nov == "s" and random.random() < probCaverna:
                                    pokebolas -= 1
                                    print(f"Você capturou o {pokemon}!\n*{pokemon} foi adicionado a sua Pokédex")
                                    pokedex.append(pokemon)
                                    break
                                elif tentar_nov == "s" and pokebolas == 0:
                                    print("Acabaram suas Pokébolas.")
                                    print("*O Pokémon fugiu")
                                    break
                                else:
                                    print("Você optou por não capturar o Pokémon.")
                                    break
                    else:
                        print("Você não pode capturar o mesmo Pokémon!")
                elif pokebolas == 0:
                        print("Acabaram suas Pokébolas. Você não consegue capturar o Pokémon.")
            elif escolha_capturar == "b":
                batalhar(pokedex[0], pokemon)
            elif escolha_capturar == "f":
                print("Você fugiu.")
            else:
                print("Comando inválido!")
        elif escolha == 2:
            pokebolas_encontradas = encontrar_pokebolas()
            if pokebolas_encontradas == 1:
                pokebolas += 1
                print("Você encontrou 1 Pokébola!")
            elif pokebolas_encontradas == 2:
                pokebolas += 2
                print("Você encontrou 2 Pokébolas!")
            else:
                print("Você não encontrou Pokébolas!")

            pokemon = sorteio_pokemon_mato(pokemonsMato, probPikachu)
            print(f"Você entrou no mato e encontrou um {pokemon}!")
            escolha_capturar = input("Deseja tentar capturar este Pokémon (c), batalhar com ele (b) ou fugir (f)? ")
            if escolha_capturar == "c":
                if pokebolas != 0:
                    if pokemon not in pokedex:
                        if random.random() < probMato:
                            pokebolas -= 1
                            print(f"Você capturou o {pokemon}!\n*{pokemon} foi adicionado a sua Pokédex")
                            pokedex.append(pokemon)
                        else:
                            pokebolas -= 1
                            print("*O Pokémon escapou")
                            if pokebolas == 0:
                                print("Você não tem mais Pokébolas!")
                                print("*O Pokémon fugiu")
                            while pokebolas > 0:
                                tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                                while tentar_nov != "s" and tentar_nov != "n":
                                    print("Comando inválido!")
                                    tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                                if tentar_nov == "s" and random.random() < probMato:
                                    pokebolas -= 1
                                    print(f"Você capturou o {pokemon}!\n*{pokemon} foi adicionado a sua Pokédex")
                                    pokedex.append(pokemon)
                                    break
                                elif tentar_nov == "s" and pokebolas == 0:
                                    print("Acabaram suas Pokébolas.")
                                    print("*O Pokémon fugiu")
                                    break
                                else:
                                    print("Você optou por não capturar o Pokémon.")
                                    break
                    else:
                        print("Você não pode capturar o mesmo Pokémon!")
                elif pokebolas == 0:
                        print("Acabaram suas Pokébolas. Você não consegue capturar o Pokémon")
            elif escolha_capturar == "b":
                batalhar(pokedex[0], pokemon)
            elif escolha_capturar == "f":
                print("Você fugiu.")
            else:
                print("Comando inválido!")
        elif escolha == 3:
            print("Pokémons na sua Pokédex:")
            for pokemon in pokedex:
                print(f"- {pokemon}")
        elif escolha == 4:
            mochila.clear()
            mochila.append(f"{pokebolas} Pokébolas")
            print("Itens na sua mochila:")
            for item in mochila:
                print(f"- {item}")
        elif escolha == 5:
            print("Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")
            continue

iniciar_jogo()
pokedex = escolher_pokemon_inicial()
menu()

def menu_Mato(event):
    global pokebolas
    frame_entrarMato.pack_forget()
    frame_menuMato.pack()

    image_mato2= Image.open("imagens/captura-mato.png")
    image_mato2 = image_mato2.resize((800, 600))
    image_mato2 = ImageTk.PhotoImage(image_mato2)
    imagem_Mato2.create_image(0,0, anchor="nw", image=image_mato2)
    imagem_Mato2.image_types = image_mato2

    lbl_pokemonMato2.config(text=f"Um {pokemon} selvagem apareceu!\n"
                              "O que você deseja fazer?")

    if pokemon == "Pikachu":
        image_capPikachu = Image.open("imagens/pikachu-captura.png")
        image_capPikachu = image_capPikachu.resize((130, 130))
        image_capPikachu = ImageTk.PhotoImage(image_capPikachu)
        imagem_CapPikachu.config(image=image_capPikachu)
        imagem_CapPikachu.image_types = image_capPikachu
    if pokemon == "Caterpie":
        image_capCaterpie = Image.open("imagens/caterpie-captura.png")
        image_capCaterpie = image_capCaterpie.resize((130, 130))
        image_capCaterpie = ImageTk.PhotoImage(image_capCaterpie)
        imagem_CapCaterpie.config(image=image_capCaterpie)
        imagem_CapCaterpie.image_types = image_capCaterpie
    if pokemon == "Pidgey":
        image_capPidgey = Image.open("imagens/pidgey-captura.png")
        image_capPidgey = image_capPidgey.resize((130, 130))
        image_capPidgey = ImageTk.PhotoImage(image_capPidgey)
        imagem_CapPidgey.config(image=image_capPidgey)
        imagem_CapPidgey.image_types = image_capPidgey
    if pokemon == "Spearow":
        image_capSpearow = Image.open("imagens/spearow-captura.png")
        image_capSpearow= image_capSpearow.resize((130, 130))
        image_capSpearow = ImageTk.PhotoImage(image_capSpearow)
        imagem_CapSpearow.config(image=image_capSpearow)
        imagem_CapSpearow.image_types = image_capSpearow


def capturar_pokemon_mato(nome):
        frame_menuCaverna.pack_forget()
        frame_capturaMato.pack
        global pokebolas

        image_mato3= Image.open("imagens/captura-mato.png")
        image_mato3 = image_mato3.resize((800, 600))
        image_mato3 = ImageTk.PhotoImage(image_mato3)
        imagem_Mato3.create_image(0,0, anchor="nw", image=image_mato3)
        imagem_Mato3.image_types = image_mato3

        if  nome == "Capturar":
            if pokebolas != 0:
                if pokemon not in pokedex:
                    pokebolas -= 1
                    if random.random() < probCaverna:
                        lbl_capturaMato.config(text=f"Você capturou o {pokemon}!\n*{pokemon} foi adicionado a sua Pokédex")
                        image_pokeball4 = Image.open("imagens/pokebola1.png")
                        image_pokeball4 = image_pokeball4.resize((75, 75))
                        image_pokeball4 = ImageTk.PhotoImage(image_pokeball4)
                        imagem_pokebola4.config(image=image_pokeball4)
                        imagem_pokebola4.image_types = image_pokeball4
                        pokedex.append(pokemon)
                    else:
                        lbl_capturaMato.config(text="*O Pokémon escapou")
                        if pokebolas == 0:
                            lbl_capturaMato.config(text="Você não tem mais Pokébolas.\n"
                                                    "*O Pokémon fugiu")




def mato_to_menu(event):
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_menu.pack()


def capturaMato_to_menu(event):
    frame_pokedex.pack_forget()
    frame_menuCaverna.pack_forget()
    frame_entrarCaverna.pack_forget()
    frame_entrarMato.pack_forget()
    frame_menuMato.pack_forget()
    frame_mochila.pack_forget()
    frame_capturaMato.pack_forget()
    frame_menu.pack()

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

btn_mato_to_menu= tk.Button(frame_menuMato, command=lambda:mato_to_menu(btn_mato_to_menu), text="Fugir", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_mato_to_menu.place(x=590, y=510)


#FRAME DE CAPTURA DO POKEMON NO MATO

frame_capturaMato = Frame(janela, width=800, height=600, bg="#f2f2f2")
frame_capturaMato.pack()

imagem_Mato3 = tk.Canvas(frame_capturaMato, width=800, height=600)
imagem_Mato3.pack()

btn_mato_to_menu123= tk.Button(frame_capturaMato, command=lambda: capturaMato_to_menu(btn_mato_to_menu123), text="Voltar", width=8, height=0, relief="raised", anchor=CENTER, padx=20, pady=5, font=("Fixedsys 17"), bg="#818690", fg="#ECECEC")
btn_mato_to_menu123.place(x=590, y=510)

lbl_capturaMato = Label(frame_capturaMato, text="", relief="flat", font=("Fixedsys 18"), fg="white", bg="#29506d")
lbl_capturaMato.place(x=50, y=465)

imagem_pokebola4 = Label(frame_capturaMato, bg="white")
imagem_pokebola4.place(x=570, y=150)