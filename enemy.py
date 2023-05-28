import pygame

class Enemy:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y

    def move(self, target_x, target_y):
        if self.x < target_x:
            self.x += 1
        elif self.x > target_x:
            self.x -= 1

        if self.y < target_y:
            self.y += 1
        elif self.y > target_y:
            self.y -= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
