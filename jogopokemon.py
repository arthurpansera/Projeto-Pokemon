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

while pokemon_inicial != 1 and pokemon_inicial != 2 and pokemon_inicial != 3:
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

print(70*"-")

import random
pokemonsCaverna = ["Zubat","Geodude","Paras"]
pokemonsMato = ["Caterpie","Weedle","Pidgey","Rattata"]
probCaverna = 0.35
probMato = 0.5

while escolha != 4:
    print("\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar Pokémon na Pokédex\n4. Sair")
    escolha = int(input("Escolha uma opção: "))
    
while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
        escolha = int(input("Opção inválida! Escolha uma opção: "))
    
if escolha == 1:
    pokemon = random.choice(pokemonsCaverna)
    print(f"Você entrou na caverna e encontrou um {pokemon}")
    escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
elif escolha == 2:
    pokemon = random.choice(pokemonsMato)
    print(f"Você entrou no mato e encontrou um {pokemon}")
    escolha_capturar = input("Deseja tentar capturar este Pokémon? (s/n): ")
elif escolha == 3:
    for pokemon in pokedex:
        print(f"Pokémons na sua Pokédex:\n- {pokemon}")
else:
    print("Até logo!")