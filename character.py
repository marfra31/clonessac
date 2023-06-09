import pygame
from bullet import Bullet
from dynamicobject import DynamicObject


class Character(DynamicObject):

    def __init__(self, width: int, height: int, image_path: str, x: int, y: int, v: int, hp: int):
        super().__init__(width, height, image_path, x, y, v, hp)
        self.prev_x = x
        self.prev_y = y

    def handle_movement(self, keys):
        self.prev_x = self.x
        self.prev_y = self.y

        if keys[pygame.K_a]:
            self.x -= self.velocity
        if keys[pygame.K_d]:
            self.x += self.velocity
        if keys[pygame.K_w]:
            self.y -= self.velocity
        if keys[pygame.K_s]:
            self.y += self.velocity

        self.borderlize()

    def bullet(self, keys) -> None | Bullet:
        dx, dy = 0, 0
        if keys[pygame.K_RIGHT]:
            dx = 1
        elif keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        if dx != 0 or dy != 0:
            h = self.image.get_rect().height
            w = self.image.get_rect().width
            x = self.x+h/2+dx*h/2
            y = self.y+w/2+dy*w/2
            return Bullet(self.width, self.height, x, y, dx, dy, 3, 1)
        return None
