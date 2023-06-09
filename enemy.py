import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos,groups, image_path,obstacle_sprites,enemy_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites=obstacle_sprites
        self.enemy_sprites=enemy_sprites

        self.direction = pygame.math.Vector2()        

        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.width = width
        self.height = height
        self.speed= 3
        self.min_x = 75
        self.max_x = width - self.image.get_width() - 75
        self.min_y = 175
        self.max_y = height - self.image.get_height() - 75

    def input(self, target_x, target_y):
        self.prev_x=self.rect.x
        self.prev_y=self.rect.y

        if self.rect.x < target_x:
            self.direction.x = 1
        elif self.rect.x > target_x:
            self.direction.x = -1
        else:
            self.direction.x=0
        if self.rect.y < target_y:
            self.direction.y = 1
        elif self.rect.y > target_y:
            self.direction.y = -1
        else:
            self.direction.y=0
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
            for enemi in self.enemy_sprites:
                if enemi.rect != self.rect and enemi.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.x = self.prev_x   
                    if self.direction.x < 0: # moving left
                        self.rect.x = self.prev_x            
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right                    

        if direction == 'vertical':
            for enemi in self.enemy_sprites:
                if enemi.rect != self.rect and enemi.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.y = self.prev_y
                    if self.direction.y < 0: # moving up
                        self.rect.y = self.prev_y                
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom     
    def check_collision_character(self, character):
        enemy_position = self.rect
        character_position=character.rect
        return character_position.colliderect(enemy_position)

    # def check_collision_character(self, character):
    #     enemy_position = self.image.get_rect()
    #     enemy_position.x = self.rect.x
    #     enemy_position.y = self.rect.y

    #     character_position = character.image.get_rect()
    #     character_position.x = character.rect.x
    #     character_position.y = character.rect.y

        # return enemy_position.colliderect(character_position)
    def collision_with_player(self,character):
        self.rect.x = self.prev_x
        self.rect.y = self.prev_y
        #tutaj kod który zabiera hp, np dodac do postaci hp i wykorzystać tu atrybut hp

    def update(self,character):
        direction_xy=character.get_pos()
        print(direction_xy, self.rect.x,self.rect.y)
        self.input(direction_xy[0],direction_xy[1])
        self.move(self.speed)
        print(self.check_collision_character(character))
        if self.check_collision_character(character):
            self.collision_with_player(character)

