
import pygame
import sys
# Inicialização do Pygame
pygame.init()

# Configurações da janela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Selector")

# Dados dos Pokémon
pokemons = [
    ["Pikachu", "pikachu.png", "Electric", 35, 55, 40],
    ["Bulbasaur", "bulbasaur.png", "Grass/Poison", 45, 49, 49],
    ["Charmander", "charmander.png", "Fire", 39, 52, 43]
]

# Fontes
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Função para desenhar texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Função para exibir os detalhes do Pokémon
def display_pokemon_details(pokemon):
    # Nome
    draw_text(pokemon[0], font, (0, 0, 0), screen, 400, 50)
    # Imagem
    img = pygame.image.load(pokemon[1])
    img = pygame.transform.scale(img, (200, 200))
    screen.blit(img, (400, 100))
    # Atributos
    draw_text(f"Type: {pokemon[2]}", small_font, (0, 0, 0), screen, 400, 320)
    draw_text(f"HP: {pokemon[3]}", small_font, (0, 0, 0), screen, 400, 360)
    draw_text(f"Attack: {pokemon[4]}", small_font, (0, 0, 0), screen, 400, 400)
    draw_text(f"Defense: {pokemon[5]}", small_font, (0, 0, 0), screen, 400, 440)

# Loop principal
running = True
selected_pokemon = None
while running:
    screen.fill((255, 255, 255))
    # Desenha a lista de Pokémon
    y = 50
    for i, pokemon in enumerate(pokemons):
        draw_text(pokemon[0], small_font, (0, 0, 0), screen, 50, y)
        y += 40
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
        if mouse_x < 300:
            index = (mouse_y - 50) // 40
        if 0 <= index < len(pokemons):
            selected_pokemon = pokemons[index]
        # Exibe os detalhes do Pokémon selecionado
    if selected_pokemon:
        display_pokemon_details(selected_pokemon)
    # Atualiza a tela
    pygame.display.flip()
    # Quit Pygame
pygame.quit()
sys.exit()
