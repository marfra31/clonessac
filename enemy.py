from dynamicobject import DynamicObject


class Enemy(DynamicObject):

    def __init__(self, width: int, height: int, image_path: str, x: int, y: int, v: int, hp: int):
        super().__init__(width, height, image_path, x, y, v, hp)
        self.prev_x = x
        self.prev_y = y

    def move(self, target_x, target_y):
        self.prev_x = self.x
        self.prev_y = self.y
        if self.x < target_x:
            self.x += self.velocity
        elif self.x > target_x:
            self.x -= self.velocity
        if self.y < target_y:
            self.y += self.velocity
        elif self.y > target_y:
            self.y -= self.velocity
        self.borderlize()

