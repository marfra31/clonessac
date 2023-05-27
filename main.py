import pygame
# from pygame.locals import *

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

character_image = pygame.image.load("Images/Faceset.png")
character_x = 400
character_y = 300

min_x = 20
max_x = width - character_image.get_width()-20
min_y = 20
max_y = height - character_image.get_height()-20

plant_image = pygame.image.load("Images/Preview.gif")
plant_x = 200
plant_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Store the current position for rollback in case of collision
    prev_character_x = character_x
    prev_character_y = character_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= 0.2
        character_x = max(character_x, min_x)
    if keys[pygame.K_RIGHT]:
        character_x += 0.2
        character_x = min(character_x, max_x)
    if keys[pygame.K_UP]:
        character_y -= 0.2
        character_y = max(character_y, min_y)
    if keys[pygame.K_DOWN]:
        character_y += 0.2
        character_y = min(character_y, max_y)

    character_rect = character_image.get_rect()
    character_rect.x = character_x
    character_rect.y = character_y

    plant_rect = plant_image.get_rect()
    plant_rect.x = plant_x
    plant_rect.y = plant_y

    if character_rect.colliderect(plant_rect):
        # Collision occurred
        # Rollback to previous position to prevent movement
        character_x = prev_character_x
        character_y = prev_character_y

    screen.fill((0, 0, 0))
    screen.blit(character_image, (character_x, character_y))
    screen.blit(plant_image, (plant_x, plant_y))
    pygame.display.flip()

pygame.quit()