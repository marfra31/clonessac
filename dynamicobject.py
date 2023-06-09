from staticobject import StaticObject


class DynamicObject(StaticObject):

    def __init__(self, width: int, height: int, image_path: str, x: int, y: int, v: int):
        super().__init__(image_path, x, y)
        self.prev_x = x
        self.prev_y = y
        self.width = width
        self.height = height
        self.velocity = v
        self.min_x = 75
        self.max_x = width - self.image.get_width() - 75
        self.min_y = 175
        self.max_y = height - self.image.get_height() - 75

    def borderlize(self) -> bool:
        """Metoda .... czy poza tablicą"""
        result = False
        if self.x < self.min_x:
            self.x = self.min_x
            result = True
        elif self.x > self.max_x:
            self.x = self.max_x
            result = True
        if self.y < self.min_y:
            self.y = self.min_y
            result = True
        elif self.y > self.max_y:
            self.y = self.max_y
            result = True

        return result

    def check_collision(self, obj: StaticObject) -> bool:
        ob1 = self.image.get_rect()
        ob1.x = self.x
        ob1.y = self.y
        ob2 = obj.image.get_rect()
        ob2.x = obj.x
        ob2.y = obj.y
        return ob1.colliderect(ob2)

    def rollback_movement(self):
        self.x = self.prev_x
        self.y = self.prev_y
