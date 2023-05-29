import pygame

class Przeciwnik(pygame.sprite.DirtySprite):
    def _init_(self):
        self.hp=100
        self.enemy_rectangle=(30,30)
    def obrazenie(self, _init_):
        uderzenie = 10
        self.hp -= uderzenie
        if self.hp<0:
            self.kill()


