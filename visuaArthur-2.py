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


def escolher_pokemon_inicial(event):
    imagem_caixaTexto.destroy()
    imagem_professor.destroy()
    imagem_fundoProfessor.destroy()
    lbl_fala.destroy()
    btn_proximo.destroy()
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

'''def iniciar_menu(pokemon_inicial):
    menu_frame = tk.Frame(janela)
    menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)
    btn_caverna = tk.Button(menu_frame, text="Entrar na caverna", command=lambda: entrar_caverna(pokemon_inicial))


    btn_caverna.pack(pady=10, fill=tk.X)

    btn_mato = tk.Button(menu_frame, text="Entrar no mato", command=lambda: entrar_mato(pokemon_inicial))
    btn_mato.pack(pady=10, fill=tk.X)

    btn_pokedex = tk.Button(menu_frame, text="Listar Pokémons na Pokédex", command=mostrar_pokedex)
    btn_pokedex.pack(pady=10, fill=tk.X)

    btn_mochila = tk.Button(menu_frame, text="Olhar itens na mochila", command=mostrar_mochila)
    btn_mochila.pack(pady=10, fill=tk.X)

    btn_sair = tk.Button(menu_frame, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10, fill=tk.X)'''

def entrar_caverna(pokemon):
    print(f"Você entrou na caverna e encontrou um {pokemon}")

def entrar_mato(pokemon):
    print(f"Você entrou no mato e encontrou um {pokemon}")

def mostrar_pokedex():
    print("Pokémons na sua Pokédex:")

def mostrar_mochila():
    print("Itens na sua mochila:")


###Precisa definir as variaveis no programa principal, igual ta daqui para baixo, pois quando a gente clica em um botão
### e vai para uma próxima tela, usamos o .destroy() para excluir as coisas da tela anterior
### Caso a variável não seja definida no programa principal, o .destroy() não funciona

janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("800x600")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)
janela.config(bg ="#d93035")

pokedex = []

#tela inicial
imagem_telaInicial = tk.Canvas(janela, width=800, height=600)
imagem_telaInicial.pack()

btn_jogar = tk.Button(janela, command=lambda: exibir_fala_professor(btn_jogar), text="", width=5, height=0, relief="raised", anchor=NW, padx=10, pady=1, font=("Fixedsys 33"), bg='black', fg='white')
btn_jogar.place(x=230, y=450)

#Tela da fala do professor Carvalho
frame_falaprofessor = tk.Frame(janela, width=800, height=600, bg="#76a2b4")
frame_falaprofessor.pack()

imagem_fundoProfessor = Label(frame_falaprofessor, bg="#76a2b4")
imagem_fundoProfessor.place(x=0, y=0)

imagem_caixaTexto = Label(frame_falaprofessor, bg="#587873")
imagem_caixaTexto.place(x=55, y=350)

lbl_fala = Label(frame_falaprofessor, text="",  relief="flat", font=("Fixedsys 17"), fg="black", bg="#d8e3e3")
lbl_fala.place(x=115, y=400)

imagem_professor = Label(frame_falaprofessor, bg="#b9d4cd")
imagem_professor.place(x=450, y=40)

image_proximo = Image.open("imagens/proximo.png")
image_proximo = image_proximo.resize((45, 40))
image_proximo = ImageTk.PhotoImage(image_proximo)
btn_proximo = tk.Button(frame_falaprofessor, command=lambda:escolher_pokemon_inicial(btn_proximo), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo.place(x=670, y=480)

#Tela de escolher o pokemon inicial
frame_pokemonInicial = tk.Frame(janela, width=800, height=600, bg="#3A8C73")
frame_pokemonInicial.pack()

imagem_caixaTexto2 = Label(frame_pokemonInicial, bg="#3A8C73")
imagem_caixaTexto2.place(x=30, y=50)

imagem_mesaPokebola = Label(frame_pokemonInicial, bg="#3A8C73")
imagem_mesaPokebola.place(x=60, y=150)

imagem_pokebola1 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola1.place(x=150, y=220)

imagem_pokebola2 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola2.place(x=345, y=220)

imagem_pokebola3 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola3.place(x=540, y=220)

#Botões para escolher o pokemon inicial
btn_bulbasaurInicial = tk.Button(frame_pokemonInicial,command=lambda: evento_botao_pokemon_inicial(nome="Bulbasaur"), text="Bulbasaur", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_bulbasaurInicial.place(x=220, y=400,anchor="center")

btn_squirtleInicial = tk.Button(frame_pokemonInicial,command=lambda: evento_botao_pokemon_inicial(nome="Squirtle"), text="Squirtle", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_squirtleInicial.place(x=415, y=400, anchor="center")

btn_charmanderInicial = tk.Button(frame_pokemonInicial,  command=lambda: evento_botao_pokemon_inicial(nome="Charmander"), text="Charmander", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg="#F0D882", fg="#6E5820")
btn_charmanderInicial.place(x=608, y=400, anchor="center")

#Mensagem da caixa de texto
lbl_escolhaPokemon = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolhaPokemon.place(x=72, y=78)

lbl_escolheuBulbasaur = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuBulbasaur.place(x=130, y=90)

lbl_escolheuSquirtle = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuSquirtle.place(x=130, y=90)

lbl_escolheuCharmander = Label(frame_pokemonInicial, text="",  relief="flat", height=2, font=("Fixedsys 17"), fg="#20506E", bg="#d8e3e3")
lbl_escolheuCharmander.place(x=130, y=90)

imagem_bulbasauro = Label(frame_pokemonInicial, bg="#88c088")
imagem_bulbasauro.place(x=150, y=220)

imagem_squirtle = Label(frame_pokemonInicial, bg="#88c088")
imagem_squirtle.place(x=345, y=230)

imagem_charmander = Label(frame_pokemonInicial, bg="#88c088")
imagem_charmander.place(x=540, y=230)





pokedex = []


iniciar_jogo()
janela.mainloop()