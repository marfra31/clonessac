import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,direction,group,obstacle_sprites,enemy_sprites):
        super().__init__(group)
        self.group=group
        self.image=pygame.image.load("Images/tear.png")
        self.rect=self.image.get_rect(center=(pos_x,pos_y))
        self.direction=direction
        self.type=type
        self.enemy_sprites=enemy_sprites
        self.obstacle_sprites=obstacle_sprites
        self.min_x = 75
        self.max_x = width - self.image.get_width()-75
        self.min_y = 175
        self.max_y = height - self.image.get_height()-75    

    def check_collision_enemy(self):
        for enemy in self.enemy_sprites:
            if enemy.rect.colliderect(self.rect):
                super().kill()
                enemy.get_hit()
    def check_collision_obstacle(self):
        for object in self.obstacle_sprites:
            if object.rect.colliderect(self.rect):
                super().kill()        
    def move(self):
        if self.direction=="right":
            self.rect.x+=6
        if self.direction=="left":
            self.rect.x-=6
        if self.direction=="up":
            self.rect.y-=6
        if self.direction=="down":
            self.rect.y+=6
        if self.rect.x<self.min_x or self.rect.x>self.max_x or self.rect.y<self.min_y or self.rect.y>self.max_y:
            super().kill()                            
    def update(self):
        self.check_collision_enemy()
        self.check_collision_obstacle()
        self.move()            