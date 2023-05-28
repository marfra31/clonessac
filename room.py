import pygame

class Room:
    def __init__(self, background_image_path):
        self.background_image = pygame.image.load(background_image_path)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
