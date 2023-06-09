import pygame, sys
from button import Button
from room import Room
from character import Character
from objects import Object
from enemy import Enemy
from menu import main_menu
from debug import debug
from settings import *

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def play(fullscreen=True):
    if fullscreen:
        screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((width, height))
    pygame.init()
    pygame.display.set_caption("Clonessac")
    FPS = 60

    room = Room("Images/game.png")
    enemy = Enemy("Images/Enemy.png", 500, 300)
    character = Character("Images/Character.png", 100, 300)

    # rock = Object("Images/rock.png", 80, 175)
    # rock2 = Object("Images/rock2.png", 80, 470)
    # rock3 = Object("Images/rock.png", 675, 175)
    # rock4 = Object("Images/rock2.png", 670, 470)
    # rock5 = Object("Images/rock.png", 375, 300)
    # listOfObjects = [rock, rock2, rock3, rock4, rock5]

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        character.handle_movement(keys)
        for item in pygame.sprite.Group():
            if character.check_collision(item):
                character.rollback_movement()
            if enemy.check_collision(item):
                enemy.rollback_movement()
        if character.check_collision_enemy(enemy):
            character.rollback_movement()
        if enemy.check_collision_character(character):
            enemy.rollback_movement()
        enemy.move(character.x, character.y)
        screen.fill((0, 0, 0))
        room.draw(screen)
        character.draw(screen)
        enemy.draw(screen)
        room.run()
        # for item in listOfObjects:
        #     item.draw(screen)
        debug([character.x,character.y])
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main_menu(play)






