import pygame
from settings import *
from objects import Object
from character import Character
from debug import debug
class Room:
    def __init__(self, background_image_path):
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load(background_image_path)
        screen.blit(self.background_image, (0, 0))
        self.obstacle_sprites = pygame.sprite.Group()
        self.entity_sprites = pygame.sprite.Group()
        
        self.update_room()
        
    def update_room(self):
        for row_index,row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'r':
                    Object((x,y),"Images/rock.png",self.obstacle_sprites)
                    print((x,y))
                if col == 'p':
                    self.player = Character((x,y),[self.entity_sprites],"Images/Character.png",self.obstacle_sprites)
                # self.character=Character((x,y),"Images/rock.png",self.obstacle_sprites)
    def run(self):
    		# update and draw the game
        screen.blit(self.background_image, (0, 0))
        self.entity_sprites.draw(self.display_surface)
        self.entity_sprites.update()
        self.obstacle_sprites.draw(self.display_surface)
        self.obstacle_sprites.update()

        debug(self.player.direction)
