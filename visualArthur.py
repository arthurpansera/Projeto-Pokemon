import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Jogo Pokémon")

def iniciar_jogo():
    global canvas
    # Definindo tela inicial com imagem do Pokémon Fire Red
    canvas.delete("all")
    imagem_inicio = Image.open("imagens/tela_inicial.jpg")
    imagem_inicio = imagem_inicio.resize((500, 500))
    foto_inicio = ImageTk.PhotoImage(imagem_inicio)
    canvas.create_image(0, 0, anchor="nw", image=foto_inicio)
    canvas.image = foto_inicio

    # Adicionando botão "Jogar"
    btn_jogar = tk.Button(root, text="Jogar", command=lambda: exibir_fala_professor(btn_jogar))
    btn_jogar.place(relx=0.5, rely=0.9, anchor="center")

def exibir_fala_professor(btn_jogar):
    btn_jogar.destroy()
    # Exibir fala do Professor Carvalho
    global canvas
    label_fala = tk.Label(root, text="Olá! Eu sou o Professor Carvalho, um pesquisador Pokémon.\n"
                                     "Esse mundo é habitado por várias criaturas chamadas de Pokémon.\n"
                                     "Algumas pessoas os tratam como mascotes, outras usam em batalhas.")
    label_fala.place(relx=0.5, rely=0.5, anchor="center")
    root.after(5000, lambda: escolher_pokemon_inicial(label_fala))

def escolher_pokemon_inicial(label_fala):
    label_fala.destroy()
    global canvas
    # Criar tela para escolha do Pokémon inicial
    canvas.delete("all")
    imagem_pokebolas = Image.open("pokebolas.png")
    imagem_pokebolas = imagem_pokebolas.resize((500, 500))
    foto_pokebolas = ImageTk.PhotoImage(imagem_pokebolas)
    canvas.create_image(0, 0, anchor="nw", image=foto_pokebolas)
    canvas.image = foto_pokebolas

    # Adicionar botões para escolher o Pokémon inicial
    btn_bulbasaur = tk.Button(root, text="Bulbasaur", command=lambda: iniciar_menu("Bulbasaur"))
    btn_bulbasaur.place(relx=0.2, rely=0.8, anchor="center")

    btn_squirtle = tk.Button(root, text="Squirtle", command=lambda: iniciar_menu("Squirtle"))
    btn_squirtle.place(relx=0.5, rely=0.8, anchor="center")

    btn_charmander = tk.Button(root, text="Charmander", command=lambda: iniciar_menu("Charmander"))
    btn_charmander.place(relx=0.8, rely=0.8, anchor="center")

def iniciar_menu(pokemon_inicial):
    global canvas
    canvas.delete("all")

    # Adicionar menu na esquerda
    menu_frame = tk.Frame(root)
    menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    # Definir imagem de fundo
    imagem_casa = Image.open("casa_inicial.png")
    imagem_casa = imagem_casa.resize((800, 500), Image.ANTIALIAS)
    foto_casa = ImageTk.PhotoImage(imagem_casa)
    canvas.create_image(0, 0, anchor="nw", image=foto_casa)
    canvas.image = foto_casa

    # Adicionar opções do menu
    btn_caverna = tk.Button(menu_frame, text="Entrar na caverna", command=lambda: entrar_caverna(pokemon_inicial))
    btn_caverna.pack(pady=10, fill=tk.X)

    btn_mato = tk.Button(menu_frame, text="Entrar no mato", command=lambda: entrar_mato(pokemon_inicial))
    btn_mato.pack(pady=10, fill=tk.X)

    btn_pokedex = tk.Button(menu_frame, text="Listar Pokémons na Pokédex", command=mostrar_pokedex)
    btn_pokedex.pack(pady=10, fill=tk.X)

    btn_mochila = tk.Button(menu_frame, text="Olhar itens na mochila", command=mostrar_mochila)
    btn_mochila.pack(pady=10, fill=tk.X)

    btn_sair = tk.Button(menu_frame, text="Sair", command=root.destroy)
    btn_sair.pack(pady=10, fill=tk.X)

def entrar_caverna(pokemon):
    print(f"Você entrou na caverna e encontrou um {pokemon}")

def entrar_mato(pokemon):
    print(f"Você entrou no mato e encontrou um {pokemon}")

def mostrar_pokedex():
    print("Pokémons na sua Pokédex:")

def mostrar_mochila():
    print("Itens na sua mochila:")

# Definir canvas para exibir imagens
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

iniciar_jogo()

root.mainloop()