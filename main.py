import pygame
from room import Room
from character import Character
from objects import Object

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
room = Room("Images/game.png")
FPS=60

character = Character("Images/Faceset.png", 100, 300, width, height)

rock=Object("Images/rock1.png", 80, 180)
rock2=Object("Images/rock2.png", 75, 470)
rock3=Object("Images/rock1.png", 670, 180)
rock4=Object("Images/rock2.png", 670, 470)
rock5=Object("Images/rock1.png", 375, 300)
listOfObjects=[rock,rock2,rock3,rock4,rock5] 

running = True
clock=pygame.time.Clock()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    character.handle_movement(keys)
    for item in listOfObjects:
        if character.check_collision(item):
            character.rollback_movement()

    screen.fill((0, 0, 0))
    room.draw(screen)
    character.draw(screen)
    for item in listOfObjects:
        item.draw(screen)
    pygame.display.flip()

pygame.quit()

