import pygame


class StaticObject():

    def __init__(self, image_path: str, x: int, y: int):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
