import pygame

from character import Character
from objects import Object

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
FPS=60

character = Character("Images/Faceset.png", 400, 300, width, height)
plant = Object("Images/Preview.gif", 200, 200)
def drawingObjects():
    pass

running = True
clock=pygame.time.Clock()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    character.handle_movement(keys)

    if character.check_collision(plant):
        character.rollback_movement()

    screen.fill((0, 0, 0))
    character.draw(screen)
    plant.draw(screen)
    pygame.display.flip()

pygame.quit()

