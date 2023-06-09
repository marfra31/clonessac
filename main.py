import pygame
from room import Room
from character import Character
from staticobject import StaticObject
from enemy import Enemy
from menu import main_menu
from time import time


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def play(fullscreen=False):
    width, height = 800, 600
    if fullscreen:
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((width, height))
    pygame.init()
    pygame.display.set_caption("Clonessac")
    FPS = 60

    room = Room("Images/game.png")
    enemy = Enemy(width, height, "Images/Enemy.png", 500, 300, 3)
    character = Character(width, height, "Images/Character.png", 100, 300, 5)

    listOfObjects = [
        StaticObject("Images/rock1.png", 80, 175),
        StaticObject("Images/rock2.png", 80, 470),
        StaticObject("Images/rock1.png", 675, 175),
        StaticObject("Images/rock2.png", 670, 470),
        StaticObject("Images/rock1.png", 375, 300)
    ]

    running = True
    clock = pygame.time.Clock()
    bullets = []
    last_bullet = 0

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        print(bullets)
        keys = pygame.key.get_pressed()
        character.handle_movement(keys)
        if len(bullets) < 3:
            bullet = character.bullet(keys)
            if bullet is not None:
                if time() - last_bullet > 0.4:
                    bullets.append(bullet)
                    last_bullet = time()

        for item in listOfObjects:
            for bullet in bullets:
                if bullet.check_collision(item) or bullet.check_collision(enemy):
                    bullets.remove(bullet)
            if character.check_collision(item):
                character.rollback_movement()
            if enemy.check_collision(item):
                enemy.rollback_movement()
        if character.check_collision(enemy):
            character.rollback_movement()
        if enemy.check_collision(character):
            enemy.rollback_movement()
        enemy.move(character.x, character.y)
        screen.fill((0, 0, 0))
        room.draw(screen)
        character.draw(screen)
        enemy.draw(screen)
        for item in listOfObjects:
            item.draw(screen)
        for bullet in bullets:
            if bullet.move():
                bullets.remove(bullet)
            else:
                bullet.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main_menu(play)
