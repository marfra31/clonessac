import pygame
from settings import *

class Enemy:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.width = width
        self.height = height
        self.min_x = 75
        self.max_x = width - self.image.get_width() - 75
        self.min_y = 175
        self.max_y = height - self.image.get_height() - 75

    def move(self, target_x, target_y):
        self.prev_x=self.x
        self.prev_y=self.y
        if self.x < target_x:
            self.x += 2
            self.x = min(self.x, self.max_x)
        elif self.x > target_x:
            self.x -= 2
            self.x = max(self.x, self.min_x)

        if self.y < target_y:
            self.y += 2
            self.y = min(self.y, self.max_y)
        elif self.y > target_y:
            self.y -= 2
            self.y = max(self.y, self.min_y)

    def check_collision(self, object):
        enemy_position = self.image.get_rect()
        enemy_position.x = self.x
        enemy_position.y = self.y

        object_position = object.image.get_rect()
        object_position.x = object.x
        object_position.y = object.y

        return enemy_position.colliderect(object_position)

    def check_collision_character(self, character):
        enemy_position = self.image.get_rect()
        enemy_position.x = self.x
        enemy_position.y = self.y

        character_position = character.image.get_rect()
        character_position.x = character.x
        character_position.y = character.y

        return enemy_position.colliderect(character_position)
    def rollback_movement(self):
        self.x = self.prev_x
        self.y = self.prev_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

