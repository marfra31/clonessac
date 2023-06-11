import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, groups, passable_for_bullet=False):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.passable_for_bullet=passable_for_bullet
