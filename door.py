import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, pos,direction,groups,enemy_sprites):
    
        super().__init__(groups)
        if not direction=="Boss":
            self.image = pygame.image.load("Images/closed_door.png").convert_alpha()
        else:
            self.image = pygame.image.load("Images/trophy.png").convert_alpha()
        
        self.direction=direction
        self.enemy_sprites=enemy_sprites
        self.pos=pos

                    

        self.rotate()
        self.rect = self.image.get_rect(topleft = self.pos)

    def rotate(self):
        if self.direction=="N" or self.direction=="S":
            self.pos=(self.pos[0]-15,self.pos[1])
        if self.direction=="E" or self.direction=="W":
            self.pos=(self.pos[0],self.pos[1]-20)

        if self.direction=="E":
            self.image = pygame.transform.rotate(self.image, 270)
        if self.direction=="W":
            self.image = pygame.transform.rotate(self.image, 90)
        if self.direction=="S":
            self.image = pygame.transform.rotate(self.image, 180)

    def check_collision_character(self, character):
        door_position = self.rect
        character_position=character.rect
        return character_position.colliderect(door_position)
    def move_character(self):        
            if self.direction=="N": #S=[8,7]
                return [7,7]            
            if self.direction=="E": #W=[0,4]
                return [1,4]
            if self.direction=="W": #E=[14,4]
                return [13,4]  
            if self.direction=="S": #W=[7,0]
                return [7,1]  
            


    def update(self):
        if len(self.enemy_sprites)==0:
            if not self.direction == "Boss":
                self.image = pygame.image.load("Images/open_door.png").convert_alpha()
                self.rotate()
            else:
                self.image=pygame.image.load("Images/trophy.png").convert_alpha()
                self.rect = self.image.get_rect(topleft=self.pos)
