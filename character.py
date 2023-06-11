import pygame
from settings import *
from bullet import Bullet

class Character(pygame.sprite.Sprite):
    def __init__(self, pos,groups, image_path,obstacle_sprites,enemy_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites=obstacle_sprites
        self.enemy_sprites=enemy_sprites
        
        self.direction = pygame.math.Vector2()
        self.hp=6
        self.speed = 5
        self.shot_speed=2

        self.bullet_activate_x=0
        self.bullet_activate_y=0
        self.groups=groups

        self.min_x = 70
        self.max_x = width - self.image.get_width()-70
        self.min_y = 150
        self.max_y = height - self.image.get_height()-70
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_RIGHT]:
            self.bullet_activate_x += 1 * self.shot_speed
            if self.bullet_activate_x > 50:
                self.bullet_activate_x=0
                return Bullet(self.rect.centerx,self.rect.centery,"right",self.groups,self.obstacle_sprites,self.enemy_sprites)
        elif keys[pygame.K_LEFT]:
            self.bullet_activate_x += 1 * self.shot_speed
            if self.bullet_activate_x > 50:
                self.bullet_activate_x=0
                return Bullet(self.rect.centerx,self.rect.centery,"left",self.groups,self.obstacle_sprites,self.enemy_sprites)
        elif keys[pygame.K_UP]:
            self.bullet_activate_y += 1 * self.shot_speed
            if self.bullet_activate_y > 50:
                self.bullet_activate_y=0
                return Bullet(self.rect.centerx,self.rect.centery,"up",self.groups,self.obstacle_sprites,self.enemy_sprites)
        elif keys[pygame.K_DOWN]:
            self.bullet_activate_y += 1 * self.shot_speed
            if self.bullet_activate_y > 50:
                self.bullet_activate_y=0
                return Bullet(self.rect.centerx,self.rect.centery,"down",self.groups,self.obstacle_sprites,self.enemy_sprites)
        
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.x = min(self.rect.x, self.max_x)
        self.rect.x = max(self.rect.x, self.min_x)
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.y = min(self.rect.y, self.max_y)
        self.rect.y = max(self.rect.y, self.min_y)

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom
    def get_pos(self):
        return [self.rect.x,self.rect.y]
    def get_hit(self,damage=1):
            self.hp-=damage
            if self.hp<=0:
                super().kill()

    def dead(self):
        if self.hp<=0:
            return True
        else:
            return False
    
    def go_trough_door(self,position_x,position_y):
        self.rect.x = 25+ position_x * TILESIZE
        self.rect.y = 125+ position_y* TILESIZE


    def update(self):
        self.input()
        self.move(self.speed)
        print(self.hp)