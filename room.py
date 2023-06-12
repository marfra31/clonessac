import pygame
import random
from settings import *
from objects import Object
from character import Character
from debug import debug
from enemy import Enemy
from door import Door
import copy
class Room:
    def __init__(self, background_image_path):
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load(background_image_path)
        screen.blit(self.background_image, (0, 0))
        self.obstacle_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.enemy_sprites=pygame.sprite.Group()
        self.doors_sprites=pygame.sprite.Group()
        self.current_room = [4, 4]
        self.room_generator()
        self.update_room(MAP)
        self.create_character(MAP)
        

    def create_character(self,map):
        for row_index,row in enumerate(map):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'p':
                    self.character = Character((x,y),[self.visible_sprites],"Images/Character.png",self.obstacle_sprites,self.enemy_sprites)            
        
    def update_room(self,map):
        for row_index,row in enumerate(map):
            for col_index, col in enumerate(row):
                x = 25+col_index * TILESIZE
                y = 125+row_index * TILESIZE
                if col == 'N' or col == 'E' or col == 'W' or col == 'S': 
                    self.object=self.draw_doors((x,y),col,[self.visible_sprites,self.doors_sprites],self.enemy_sprites)   
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
                elif col == 'e' and map[0][0]=='0':
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
                    self.enemy_killed_state()
                    self.change_current_room(door.direction)
                    character_position=door.move_character()
                    self.character.go_trough_door(character_position[0],character_position[1])
                    self.room_clear()                          
                    self.update_room(MAP_OF_ROOMS[self.current_room[0]][self.current_room[1]])
        if self.character.dead():
            pass          
            # miejsce na menu jak umrzesz
        mapa = MAP_OF_ROOMS[self.current_room[0]][self.current_room[1]]
        debug([self.character.hp,self.current_room,mapa[0][0]])

    def draw_doors(self, pos, direction, groups, enemy_sprites,type="room"):

        self.groups=groups
        self.direction = direction
        self.enemy_sprites = enemy_sprites
        self.pos = pos

        self.type=type
        horizontal_position = self.current_room[0]
        vertical_position = self.current_room[1]

        if direction=="N" and MAP_OF_WORLD[horizontal_position-1][vertical_position]=="r":
            return Door(pos, direction, [self.visible_sprites, self.doors_sprites], self.enemy_sprites)
        elif direction == "E" and MAP_OF_WORLD[horizontal_position][vertical_position+1] == "r":
            return Door(pos, direction, [self.visible_sprites, self.doors_sprites], self.enemy_sprites)
        elif direction=="W" and MAP_OF_WORLD[horizontal_position][vertical_position-1]=="r":
            return Door(pos, direction, [self.visible_sprites, self.doors_sprites], self.enemy_sprites)
        elif direction == "S" and MAP_OF_WORLD[horizontal_position+1][vertical_position] == "r":
            return Door(pos, direction, [self.visible_sprites, self.doors_sprites], self.enemy_sprites)
        else:
            return Object(pos, "Images/transparent.png", [self.obstacle_sprites])
        
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

    def enemy_killed_state(self):
        temp_map=copy.deepcopy(MAP_OF_ROOMS[self.current_room[0]][self.current_room[1]])
        temp_map[0][0]='1'
        MAP_OF_ROOMS[self.current_room[0]][self.current_room[1]] = temp_map
        del temp_map

    def room_generator(self):
        for row_index, row in enumerate(MAP_OF_WORLD):
            for col_index, col in enumerate(row):
                if col == 'r':
                    if row_index==4 and col_index==4:    
                        MAP_OF_ROOMS[row_index][col_index]=MAP
                    else:
                        temp_map = copy.deepcopy(UPDATE_MAP)
                        object = ['r', 'r2', 'r3', 'd', ' ', ' ',
                                  ' ', ' ', ' ', ' ']

                        corner_object_furthest=random.choice(object)
                        map_of_cof=[[1,1],[1,13],[7,13],[7,1]]
                        self.insert_to_map(temp_map, map_of_cof, corner_object_furthest)

                        corner_object = random.choice(object)
                        map_of_co = [[2, 2], [2, 12], [6, 12], [6, 2]]
                        self.insert_to_map(temp_map, map_of_co, corner_object)

                        center_vertical = random.choice(object)
                        map_of_cv=[[2,7],[6,7]]
                        self.insert_to_map(temp_map, map_of_cv, center_vertical)

                        center_vertical_door = random.choice(object)
                        map_of_cv_d =[[1, 5], [1, 9], [7,5], [7,9]]
                        self.insert_to_map(
                            temp_map, map_of_cv_d, center_vertical_door)

                        center_horizontal = random.choice(object)
                        map_of_ch=[[4,4],[4,10]]
                        self.insert_to_map(temp_map,map_of_ch,center_horizontal)

                        center_horizontal_door = random.choice(object)
                        map_of_ch_d = [[3, 1], [5, 1],[3,13],[5,13]]
                        self.insert_to_map(temp_map, map_of_ch_d, center_horizontal_door)

                        center_object = random.choice(object)
                        map_of_center = [[4,7]]
                        self.insert_to_map(temp_map, map_of_center, center_object)
                        
                        center_cross_object = random.choice(object)
                        map_of_center_c = [[4,8],[4,6],[3,7],[5,7]]
                        self.insert_to_map(temp_map, map_of_center_c, center_cross_object)

            
                        
                        MAP_OF_ROOMS[row_index][col_index]=temp_map
                        del temp_map

    def insert_to_map(self, map, object_location, object):
        for element in object_location:
            map[element[0]][element[1]] = object
