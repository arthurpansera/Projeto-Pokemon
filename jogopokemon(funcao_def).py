#Projeto: Jogo Pokémon Simplificado em Python (Atualizado com def)
#Alunos: Arthur Rodrigues Pansera, Jean Inácio Praes Moura e Stefany Carlos de Oliveira
#Turma: C

def iniciar_jogo():
    print("\n---------------------------- JOGO POKÉMON ----------------------------")
    print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
    print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
    print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
    nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
    print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")
    print("Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")

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
    import random
    pokemonsCaverna = ["Zubat","Geodude","Paras"]
    pokemonsMato = ["Caterpie","Weedle","Pidgey","Rattata"]
    probCaverna = 0.35
    probMato = 0.5
    pokebolas_extras = 3

    while escolha in [1, 2, 3]:
        print(70*"-")
        print("\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar Pokémon na Pokédex\n4. Sair")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            pokemon = random.choice(pokemonsCaverna)
            print(f"Você entrou na caverna e encontrou um {pokemon}")
            escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
            if escolha_capturar == "s":
                if pokemon not in pokedex:
                    if random.random() < probCaverna:
                        print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                        pokedex.append(pokemon)
                    else:
                        print("*O Pokémon escapou")
                        if pokebolas_extras == 0:
                            print("Você não tem mais Pokébolas extras")
                            print("*O Pokémon fugiu")
                        while pokebolas_extras > 0:
                            tentar_nov = input(f"Você tem mais {pokebolas_extras} Pokébolas. Deseja tentar novamente? (s/n): ")
                            if tentar_nov == "s" and random.random() < probCaverna:
                                pokebolas_extras -= 1
                                print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                                pokedex.append(pokemon)
                                break
                            elif tentar_nov == "n":
                                print("Você optou por não capturar o Pokémon")
                                break
                            else:
                                pokebolas_extras -= 1
                                print("*O Pokémon escapou")
                                if pokebolas_extras == 0:
                                    print("Acabaram suas Pokébolas extras")
                                    print("*O Pokémon fugiu")
                else:
                    print("Você não pode capturar o mesmo Pokémon")
            elif escolha_capturar == "n":
                print("Você optou por não capturar o Pokémon")
            else:
                print("Comando inválido")
        elif escolha == 2:
            pokemon = random.choice(pokemonsMato)
            print(f"Você entrou no mato e encontrou um {pokemon}")
            escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
            if escolha_capturar == "s":
                if pokemon not in pokedex:
                    if random.random() < probMato:
                        print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                        pokedex.append(pokemon)
                    else:
                        print("*O Pokémon escapou")
                        if pokebolas_extras == 0:
                            print("Você não tem mais Pokébolas extras")
                            print("*O Pokémon fugiu")
                        while pokebolas_extras > 0:
                            tentar_nov = input(f"Você tem mais {pokebolas_extras} Pokébolas. Deseja tentar novamente? (s/n): ")
                            if tentar_nov == "s" and random.random() < probMato:
                                pokebolas_extras -= 1
                                print(f"Você capturou o {pokemon}\n*{pokemon} foi adicionado a sua Pokédex")
                                pokedex.append(pokemon)
                                break
                            elif tentar_nov == "n":
                                print("Você optou por não capturar o Pokémon")
                                break
                            else:
                                pokebolas_extras -= 1
                                print("*O Pokémon escapou")
                                if pokebolas_extras == 0:
                                    print("Acabaram suas Pokébolas extras")
                                    print("*O Pokémon fugiu")
                else:
                    print("Você não pode capturar o mesmo Pokémon")
            elif escolha_capturar == "n":
                print("Você optou por não capturar o Pokémon")
            else:
                print("Comando inválido")
        elif escolha == 3:
            print("Pokémons na sua Pokédex:")
            for pokemon in pokedex:
                print(f"- {pokemon}")
        elif escolha == 4:
            print("Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

iniciar_jogo()
pokedex = escolher_pokemon_inicial()
menu()