import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, pos,direction,groups,enemy_sprites):
    
        super().__init__(groups)
        
        self.image = pygame.image.load("Images/closed_door.png").convert_alpha()

        self.rect = self.image.get_rect(topleft = pos)
        self.direction=direction
        self.enemy_sprites=enemy_sprites
        self.pos=pos

        if self.direction=="N" or self.direction=="S":
            self.pos=(self.pos[0]-15,self.pos[1])
        if self.direction=="E" or self.direction=="W":
            self.pos=(self.pos[0],self.pos[1]-20)
        self.rect = self.image.get_rect(topleft = self.pos)            

        self.rotate()

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

    def update(self):
        if len(self.enemy_sprites)==0:
            self.image = pygame.image.load("Images/open_door.png").convert_alpha()
            self.rotate()