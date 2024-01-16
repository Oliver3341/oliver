import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación de Flor Amarilla")

# Colores
YELLOW = (255, 255, 0)

# Variables para la animación
petal_height = 0
petal_width = 200
stem_height = 400
animate_petal = False

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Dibuja el tallo
    pygame.draw.rect(screen, (0, 255, 0), (width // 2 - 10, height - stem_height, 20, stem_height))

    # Dibuja los pétalos de la flor
    if animate_petal and petal_height < stem_height:
        petal_height += 5
    pygame.draw.ellipse(screen, YELLOW, (width // 2 - petal_width // 2, height - stem_height - petal_height, petal_width, petal_height * 2))

    pygame.display.flip()
    clock.tick(30)

    if petal_height >= stem_height:
        animate_petal = False

pygame.quit()
sys.exit()
