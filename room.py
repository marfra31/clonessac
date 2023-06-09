import pygame
from settings import *
from objects import Object
class Room:
    def __init__(self, background_image_path):
        self.background_image = pygame.image.load(background_image_path)
        self.obstacle_sprites = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        
        self.update_room()
    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        
    def update_room(self):
        for row_index,row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'r':
                    Object((x,y),"Images/rock.png",self.obstacle_sprites)
                    print((x,y))
    def run(self):
    		# update and draw the game
        self.obstacle_sprites.draw(self.display_surface)
        self.obstacle_sprites.update()
