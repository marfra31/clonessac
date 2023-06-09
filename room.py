import pygame
from settings import *
from objects import Object
from character import Character
from debug import debug
from enemy import Enemy
class Room:
    def __init__(self, background_image_path):
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load(background_image_path)
        screen.blit(self.background_image, (0, 0))
        self.obstacle_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.enemy_sprites=pygame.sprite.Group()
        self.update_room()
        
    def update_room(self):
        for row_index,row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'r':
                    Object((x,y),"Images/rock.png",[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.character = Character((x,y),[self.visible_sprites],"Images/Character.png",self.obstacle_sprites)
                if col == 'e':
                    self.enemy=Enemy((x,y),[self.enemy_sprites],"Images/Enemy.png",self.obstacle_sprites,self.enemy_sprites)
                # self.character=Character((x,y),"Images/rock.png",self.obstacle_sprites)
    def run(self):
    		# update and draw the game
        screen.blit(self.background_image, (0, 0))
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(self.character)

        debug([self.character.direction,self.character.rect.x,self.character.rect.y])
