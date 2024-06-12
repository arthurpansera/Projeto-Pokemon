#Projeto: Jogo Pokémon Simplificado em Python (Parte 2)
#Alunos: Arthur Rodrigues Pansera, Jean Inácio Praes Moura e Stefany Carlos de Oliveira
#Turma: C

import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd

dados = pd.read_csv("pokemons.csv")

pokemons = [
    dados
]

root = tk.Tk()
root.title("Jogo Pokémon")

def iniciar_jogo():
    print("\n---------------------------- JOGO POKÉMON ----------------------------")
    print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
    print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
    print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
    nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
    print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")
    print("Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")

def encontrar_pokebolas(pokebolas):
    pokebolas_encontradas = random.randint(0,2)
    if pokebolas_encontradas == 1:
        pokebolas += 1
        return print("Você encontrou 1 Pokébola")
    elif pokebolas_encontradas == 2:
        pokebolas += 2
        return print("Você encontrou 2 Pokébolas")
    else:
        return print("Você não encontrou Pokébolas")

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

def entrar_caverna(pokemon, pokebolas, probCaverna):
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

def entrar_mato(pokemon, pokebolas, probMato):
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

def mostrar_pokedex(pokemon, pokedex):
    print("Pokémons na sua Pokédex:")
    for pokemon in pokedex:
        print(f"- {pokemon}")

def mostrar_mochila(pokebolas):
    mochila = []
    mochila.append(f"{pokebolas} Pokébolas")
    print("Itens na sua mochila:")
    for item in mochila:
        print(f"- {item}")

def menu():
    escolha = 1
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
            encontrar_pokebolas(pokebolas)
            pokemon = sorteio_pokemon(pokemonsCaverna)
            entrar_caverna(pokemon, pokebolas, probCaverna)
        elif escolha == 2:
            encontrar_pokebolas(pokebolas)
            pokemon = sorteio_pokemon(pokemonsMato)
            entrar_mato(pokemon, pokebolas, probMato)
        elif escolha == 3:
            mostrar_pokedex(pokemon, pokedex)
        elif escolha == 4:
            mostrar_mochila(pokebolas)
        elif escolha == 5:
            print("Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")
            continue

frame_menu = tk.Frame(root)
frame_menu.pack()

label_titulo = tk.Label(frame_menu, text="Jogo Pokémon", font=("Helvetica", 20))
label_titulo.pack(pady=10)

btn_caverna = tk.Button(frame_menu, text="Entrar na caverna", command= entrar_caverna)
btn_caverna.pack(pady=5)

btn_mato = tk.Button(frame_menu, text="Entrar no mato", command= entrar_mato)
btn_mato.pack(pady=5)

btn_pokedex = tk.Button(frame_menu, text="Listar Pokémons na Pokédex", command= mostrar_pokedex)
btn_pokedex.pack(pady=5)

btn_mochila = tk.Button(frame_menu, text="Olhar itens na mochila", command= mostrar_mochila)
btn_mochila.pack(pady=5)

btn_sair = tk.Button(frame_menu, text="Sair", command=root.destroy)
btn_sair.pack(pady=5)

iniciar_jogo()
pokedex = escolher_pokemon_inicial()
menu()