#Projeto: Jogo Pokémon Simplificado em Python
#Alunos: Arthur Rodrigues Pansera, Jean Inácio Praes Moura e Stefany Carlos de Oliveira
#Turma: C

print("\n---------------------------- JOGO POKÉMON ----------------------------")

print("\nOlá! Eu sou o Professor Carvalho, um pesquisador Pokémon.")
print("Esse mundo é habitado por várias criaturas chamadas de Pokémon.")
print("Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
nome = input("Antes de começar sua jornada, qual é o seu nome?\nInforme seu nome: ")
print(f"Ótimo! Prazer em conhecê-lo, {nome}!\nPrepare-se para embarcar em uma aventura emocionante!\n")
print("Primeiro você deve escolher o seu Pokémon inicial. Há três opções: ")

pokemon_inicial = int(input("1. Bulbasaur\n2. Squirtle\n3. Charmander\nFaça sua escolha: "))
pokemons_iniciais = ["Bulbasaur","Squirtle","Charmander"]
pokedex = []

if pokemon_inicial == 1:
    escolha = int(input("Então você quer ficar com Bulbasaur do tipo grama? (1- Sim / 2- Não)"))
    print("Ótima escolha!")
    print("*Bulbasaur foi adicionado a sua Pokédex")
    pokedex.append("Bulbasaur")
    print(pokedex)
elif pokemon_inicial == 2:
    escolha = int(input("Então você quer ficar com Squirtle do tipo água? (1- Sim / 2- Não)"))
    print("Ótima escolha!")
    print("*Squirtle foi adicionado a sua Pokédex")
    pokedex.append("Squirtle")
    print(pokedex)
elif pokemon_inicial == 3:
    escolha = int(input("Então você quer ficar com Charmander do tipo fogo? (1- Sim / 2- Não)"))
    print("Ótima escolha!")
    print("*Charmander foi adicionado a sua Pokédex")
    pokedex.append("Charmander")
    print(pokedex)
else:
    pokemon_inicial = int(input("Opção inválida. Faça sua escolha: "))

print(70*"-")

print("\nO que você deseja fazer?")
print("1. Entrar na caverna\n2. Entrar no mato\n3. Listar Pokémon na Pokédex\n4. Sair")
escolha = int(input("Escolha uma opção: "))

import random
pokemonsCaverna = ["Zubat","Geodude","Paras"]
pokemonsMato = ["Caterpie","Weedle","Pidgey","Rattata"]
if escolha == 1:
    pokemon = random.choice(pokemonsCaverna)
    print(f"Você entrou na caverna e encontrou um {pokemon}")
elif escolha == 2:
    pokemon = random.choice(pokemonsMato)
    print(f"Você entrou no mato e encontrou um {pokemon}")