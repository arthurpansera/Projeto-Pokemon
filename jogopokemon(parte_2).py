#Projeto: Jogo Pokémon Simplificado em Python (Parte 2)
#Alunos: Arthur Rodrigues Pansera, Jean Inácio Praes Moura e Stefany Carlos de Oliveira
#Turma: C

import random

def iniciar_jogo():
    print("\n---------------------------- JOGO POKÉMON ----------------------------")
    print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
    print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
    print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
    nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
    print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")
    print("Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")

def encontrar_pokebolas():
    num = random.randint(0,2)
    return num

def sorteio_pokemon(lista_pokemons):
    indice_sorteado = random.randint(0, len(lista_pokemons)-1)
    pokemon_sorteado = lista_pokemons[indice_sorteado]
    return pokemon_sorteado

def capturar_pokemon(pokemon,prob):
    sorteio = random.random()
    if sorteio < prob:
        pokedex.append(pokemon)
        return print("Você capturou o Pokémon")
    else:
        return print("O Pokémon escapou")

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

def menu():
    escolha = 1
    mochila = []
    pokemonsCaverna = ["Zubat","Geodude","Paras"]
    pokemonsMato = ["Caterpie","Weedle","Pidgey","Rattata"]
    probCaverna = 0.35
    probMato = 0.5
    pokebolas = 3

    while True:
        print(70*"-")
        print("\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar Pokémon na Pokédex\n4. Olhar itens na mochila\n5. Sair")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            pokebolas_encontradas = encontrar_pokebolas()
            if pokebolas_encontradas == 1:
                pokebolas += 1
                print("Você encontrou 1 Pokébola")
            elif pokebolas_encontradas == 2:
                pokebolas += 2
                print("Você encontrou 2 Pokébolas")
            else:
                print("Você não encontrou Pokébolas")
            pokemon = sorteio_pokemon(pokemonsCaverna)
            print(f"Você entrou na caverna e encontrou um {pokemon}")
            escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
            if escolha_capturar == "s" and pokebolas != 0:
                if pokemon not in pokedex:
                    pokebolas -= 1
                    if random.random() < probCaverna:
                        print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                        pokedex.append(pokemon)
                    else:
                        print("*O Pokémon escapou")
                        if pokebolas == 0:
                            print("Você não tem mais Pokébolas")
                            print("*O Pokémon fugiu")
                        while pokebolas > 0:
                            tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                            if tentar_nov == "s" and random.random() < probCaverna:
                                pokebolas -= 1
                                print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                                pokedex.append(pokemon)
                                break
                            elif tentar_nov == "n":
                                print("Você optou por não capturar o Pokémon")
                                break
                            else:
                                pokebolas -= 1
                                print("*O Pokémon escapou")
                                if pokebolas == 0:
                                    print("Acabaram suas Pokébolas")
                                    print("*O Pokémon fugiu")
                else:
                    print("Você não pode capturar o mesmo Pokémon")
            elif escolha_capturar == "s" and pokebolas == 0:
                    print("Acabaram suas Pokébolas. Você não consegue capturar o Pokémon.")
            elif escolha_capturar == "n":
                print("Você optou por não capturar o Pokémon")
            else:
                print("Comando inválido")
        elif escolha == 2:
            pokebolas_encontradas = encontrar_pokebolas()
            if pokebolas_encontradas == 1:
                pokebolas += 1
                print("Você encontrou 1 Pokébola")
            elif pokebolas_encontradas == 2:
                pokebolas += 2
                print("Você encontrou 2 Pokébolas")
            else:
                print("Você não encontrou Pokébolas")
            pokemon = sorteio_pokemon(pokemonsMato)
            print(f"Você entrou no mato e encontrou um {pokemon}")
            escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
            if escolha_capturar == "s" and pokebolas != 0:
                if pokemon not in pokedex:
                    pokebolas -= 1
                    if random.random() < probMato:
                        print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                        pokedex.append(pokemon)
                    else:
                        print("*O Pokémon escapou")
                        if pokebolas == 0:
                            print("Você não tem mais Pokébolas")
                            print("*O Pokémon fugiu")
                        while pokebolas > 0:
                            tentar_nov = input(f"Você tem mais {pokebolas} Pokébolas. Deseja tentar novamente? (s/n): ")
                            if tentar_nov == "s" and random.random() < probMato:
                                pokebolas -= 1
                                print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                                pokedex.append(pokemon)
                                break
                            elif tentar_nov == "n":
                                print("Você optou por não capturar o Pokémon")
                                break
                            else:
                                pokebolas -= 1
                                print("*O Pokémon escapou")
                                if pokebolas == 0:
                                    print("Acabaram suas Pokébolas")
                                    print("*O Pokémon fugiu")
                else:
                    print("Você não pode capturar o mesmo Pokémon")
            elif escolha_capturar == "s" and pokebolas == 0:
                    print("Acabaram suas Pokébolas. Você não consegue capturar o Pokémon.")
            elif escolha_capturar == "n":
                print("Você optou por não capturar o Pokémon")
            else:
                print("Comando inválido")
        elif escolha == 3:
            print("Pokémons na sua Pokédex:")
            for pokemon in pokedex:
                print(f"- {pokemon}")
        elif escolha == 4:
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