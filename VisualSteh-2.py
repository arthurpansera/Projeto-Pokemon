import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
janela.title("Jogo Pokemon")
janela.geometry("1200x1000")
janela.iconphoto(False, PhotoImage(file="imagens/logo1.png"))
janela.resizable(width=False,height=False)
janela.config(bg = "#d93035")

def iniciar_jogo():
    # Definindo tela inicial com imagem do Pokémon Fire Red
    imagem_telaInicial.delete("all")
    image_homeScreen = Image.open("imagens/tela-inicial.png")
    image_homeScreen = image_homeScreen.resize((1200, 1000))
    image_homeScreen = ImageTk.PhotoImage(image_homeScreen)
    imagem_telaInicial.create_image(0,0, anchor="nw", image=image_homeScreen)
    imagem_telaInicial.image_types = image_homeScreen
    # Adicionando botão "Jogar
    btn_jogar.config(text="Jogar")
    

def exibir_fala_professor(event):
    btn_jogar.destroy()
    imagem_telaInicial.destroy()

    lbl_fala.config(text="Olá! Eu sou o Professor Carvalho, um pesquisador Pokémon.\n"
                                "Esse mundo é habitado por várias criaturas chamadas de Pokémon.\n"
                                "Algumas pessoas os tratam como mascotes, outras usam em batalhas.")

    image_textBox = Image.open("imagens/caixa-texto.png")
    image_textBox = image_textBox.resize((1100, 200))
    image_textBox = ImageTk.PhotoImage(image_textBox)
    imagem_caixaTexto.config(image=image_textBox)
    imagem_caixaTexto.image_types = image_textBox

    image_teacher = Image.open("imagens/professor-carvalho.png")
    image_teacher = image_teacher.resize((350, 400))
    image_teacher = ImageTk.PhotoImage(image_teacher)
    imagem_professor.config(image=image_teacher)
    imagem_professor.image_types = image_teacher

    image_backgroundTeacher = Image.open("imagens/imagem-fundo-professor.jpg")
    image_backgroundTeacher = image_backgroundTeacher.resize((1200, 850))
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
    image_tablePokeball = image_tablePokeball.resize((950, 550))
    image_tablePokeball = ImageTk.PhotoImage(image_tablePokeball)
    imagem_mesaPokebola.config(image=image_tablePokeball)
    imagem_mesaPokebola.image_types = image_tablePokeball

    image_pokeball1 = Image.open("imagens/pokebola1.png")
    image_pokeball1 = image_pokeball1.resize((200, 200))
    image_pokeball1 = ImageTk.PhotoImage(image_pokeball1)
    imagem_pokebola1.config(image=image_pokeball1)
    imagem_pokebola1.image_types = image_pokeball1

    image_pokeball2 = Image.open("imagens/pokebola2.png")
    image_pokeball2 = image_pokeball2.resize((200, 200))
    image_pokeball2 = ImageTk.PhotoImage(image_pokeball2)
    imagem_pokebola2.config(image=image_pokeball2)
    imagem_pokebola2.image_types = image_pokeball2

    image_pokeball3 = Image.open("imagens/pokebola3.png")
    image_pokeball3 = image_pokeball3.resize((200, 200))
    image_pokeball3 = ImageTk.PhotoImage(image_pokeball3)
    imagem_pokebola3.config(image=image_pokeball3)
    imagem_pokebola3.image_types = image_pokeball3

##### DAQUI PARA CIMA ESTA DANDO CERTO, AGORA É SÓ CONTINUAR ARRUMANDO #####   

def iniciar_menu(pokemon_inicial):
    global image
    image.delete("all")

    # Adicionar menu na esquerda
    menu_frame = tk.Frame(janela)
    menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    # Definir imagem de fundo
    imagem_casa = Image.open("casa_inicial.png")
    imagem_casa = imagem_casa.resize((800, 500), Image.ANTIALIAS)
    foto_casa = ImageTk.PhotoImage(imagem_casa)
    image.create_image(0, 0, anchor="nw", image=foto_casa)
    image.image_types = foto_casa

    # Adicionar opções do menu
    btn_caverna = tk.Button(menu_frame, text="Entrar na caverna", command=lambda: entrar_caverna(pokemon_inicial))
    btn_caverna.pack(pady=10, fill=tk.X)

    btn_mato = tk.Button(menu_frame, text="Entrar no mato", command=lambda: entrar_mato(pokemon_inicial))
    btn_mato.pack(pady=10, fill=tk.X)

    btn_pokedex = tk.Button(menu_frame, text="Listar Pokémons na Pokédex", command=mostrar_pokedex)
    btn_pokedex.pack(pady=10, fill=tk.X)

    btn_mochila = tk.Button(menu_frame, text="Olhar itens na mochila", command=mostrar_mochila)
    btn_mochila.pack(pady=10, fill=tk.X)

    btn_sair = tk.Button(menu_frame, text="Sair", command=janela.destroy)
    btn_sair.pack(pady=10, fill=tk.X)

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

#tela inicial
imagem_telaInicial = tk.Canvas(janela, width=1200, height=1000)
imagem_telaInicial.pack()

btn_jogar = tk.Button(janela, command=lambda: exibir_fala_professor(btn_jogar), text="", width=5, height=0, relief="raised", anchor=NW, padx=10, pady=1, font=("Fixedsys 33"), bg='black', fg='white')
btn_jogar.place(x=380, y=715)

#Tela da fala do professor Carvalho
frame_falaprofessor = tk.Frame(janela, width=1200, height=1000, bg="#76a2b4")
frame_falaprofessor.pack()

imagem_fundoProfessor = Label(frame_falaprofessor, bg="#76a2b4")
imagem_fundoProfessor.place(x=0, y=0)

imagem_caixaTexto = Label(frame_falaprofessor, bg="#587873")
imagem_caixaTexto.place(x=55, y=550)

lbl_fala = Label(frame_falaprofessor, text="",  relief="flat", font=("Fixedsys 18"), fg="black", bg="#d8e3e3")
lbl_fala.place(x= 82, y=600)

imagem_professor = Label(frame_falaprofessor, bg="#b9d4cd")
imagem_professor.place(x=570, y=40)

image_proximo = Image.open("imagens/proximo.png")
image_proximo = image_proximo.resize((45, 40))
image_proximo = ImageTk.PhotoImage(image_proximo)
btn_proximo = tk.Button(frame_falaprofessor, command=lambda:escolher_pokemon_inicial(btn_proximo), image=image_proximo, width=0, height=0, relief="raised", anchor=NW, padx=1, pady=1, bg='#d8e3e3')
btn_proximo.place(x=1040, y=690)

#Tela de escolher o pokemon inicial
frame_pokemonInicial = tk.Frame(janela, width=1200, height=1000, bg="#7FC9B5")
frame_pokemonInicial.pack()

imagem_mesaPokebola = Label(frame_pokemonInicial, bg="#7FC9B5")
imagem_mesaPokebola.place(x=130, y=120)

imagem_pokebola1 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola1.place(x=215, y=210)

imagem_pokebola2 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola2.place(x=500, y=210)

imagem_pokebola3 = Label(frame_pokemonInicial, bg="#88c088")
imagem_pokebola3.place(x=790, y=210)

btn_bulbasaurInicial = tk.Button(frame_pokemonInicial,command=lambda: iniciar_menu("Bulbasaur"), text="Bulbasaur", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg='black', fg='white')
btn_bulbasaurInicial.place(x=315, y=450,anchor="center")

btn_squirtleInicial = tk.Button(frame_pokemonInicial,command=lambda: iniciar_menu("Squirtle"), text="Squirtle", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg='black', fg='white')
btn_squirtleInicial.place(x=600, y=450, anchor="center")

btn_charmanderInicial = tk.Button(frame_pokemonInicial,  command=lambda: iniciar_menu("Charmander"), text="Charmander", width=10, height=0, relief="raised", anchor=NW, padx=35, pady=2, font=("Fixedsys 17"), bg='black', fg='white')
btn_charmanderInicial.place(x=890, y=450, anchor="center")


iniciar_jogo()
janela.mainloop()