import pygame
from settings import *
from objects import Object
from character import Character
from debug import debug
from enemy import Enemy
from door import Door
class Room:
    def __init__(self, background_image_path):
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load(background_image_path)
        screen.blit(self.background_image, (0, 0))
        self.obstacle_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.enemy_sprites=pygame.sprite.Group()
        self.doors_sprites=pygame.sprite.Group()
        self.update_room(MAP)
        self.create_character(MAP)
        self.current_room=[4,4]

    def create_character(self,MAP):
        for row_index,row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'p':
                    self.character = Character((x,y),[self.visible_sprites],"Images/Character.png",self.obstacle_sprites,self.enemy_sprites)            
        
    def update_room(self,MAP):
        for row_index,row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'N' or col == 'E' or col == 'W' or col == 'S': 
                    self.door=Door((x,y),col,[self.visible_sprites,self.doors_sprites],self.enemy_sprites)   
                elif col == '0':
                    self.object=Object((x,y),"Images/transparent.png",[self.obstacle_sprites])                                     
                elif col == 'r':
                    self.object=Object((x,y),"Images/rock.png",[self.visible_sprites,self.obstacle_sprites])
                elif col == 'r2':
                    self.object=Object((x,y),"Images/rock2.png",[self.visible_sprites,self.obstacle_sprites])   
                elif col == 'r3':
                    self.object=Object((x,y),"Images/rock3.png",[self.visible_sprites,self.obstacle_sprites])  
                elif col == 'd':
                    self.object = Object(
                        (x, y), "Images/dziura.png", [self.visible_sprites, self.obstacle_sprites],True)
                elif col == 'e':
                    self.enemy=Enemy((x,y),[self.enemy_sprites],"Images/Enemy.png",self.obstacle_sprites,self.enemy_sprites)
                # self.character=Character((x,y),"Images/rock.png",self.obstacle_sprites)
    def run(self):
    		# update and draw the game
        screen.blit(self.background_image, (0, 0))
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(self.character)
        if len(self.enemy_sprites)==0:
            for door in self.doors_sprites:
                if door.check_collision_character(self.character):
                    self.change_current_room(door.direction)
                    character_position=door.move_character()
                    self.character.go_trough_door(character_position[0],character_position[1])
                    self.room_clear()                          
                    self.update_room(UPDATE_MAP)
        if self.character.dead():
            pass          
            # miejsce na menu jak umrzesz

        debug([self.character.hp,self.current_room])
    def draw_doors(self):
        pass    
    def change_current_room(self,door_direction):
            if door_direction=="N":
                self.current_room[0]-=1           
            if door_direction=="E":
                self.current_room[1]+=1
            if door_direction=="W":
                self.current_room[1]-=1
            if door_direction=="S":
                self.current_room[0]+=1
    def room_clear(self):
        for sprite in self.visible_sprites:
            if sprite.rect!=self.character.rect:
                sprite.kill()
        for sprite in self.obstacle_sprites:
            sprite.kill()    
        for sprite in self.enemy_sprites:
            sprite.kill()
        del self.object
