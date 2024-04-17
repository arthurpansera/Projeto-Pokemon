#Projeto: Jogo Pokémon Simplificado em Python
#Alunos: Arthur Rodrigues Pansera, Jean Inácio Praes Moura e Stefany Carlos de Oliveira
#Turma: C

print("\n---------------------------- JOGO POKÉMON ----------------------------")

print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")

print(70*"-")

print("\nO que você deseja fazer?")
print("1. Entrar na caverna\n2. Entrar no mato\n3. Lista Pokémon na Pokédex\n4. Sair")
escolha = int(input("Escolha uma opção: "))

import random
pokedex = []
pokemonsCaverna = ["Zubat","Geodude","Paras"]
pokemonsMato = ["Caterpie","Weedle","Pidgey","Rattata"]
if escolha == 1:
    pokemon = random.choice(pokemonsCaverna)
    print(f"Você entrou na caverna e encontrou um {pokemon}")
elif escolha == 2:
    pokemon = random.choice(pokemonsMato)
    print(f"Você entrou no mato e encontrou um {pokemon}")