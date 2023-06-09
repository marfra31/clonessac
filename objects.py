import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, image_path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft = pos)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))