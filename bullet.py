from dynamicobject import DynamicObject


class Bullet(DynamicObject):

    def __init__(self, width: int, height: int, x: int, y: int, dx: int, dy: int, v: int, hp: int) -> None:
        super().__init__(width, height, "Images/tear.png", x, y, v, hp)
        self.dx = dx
        self.dy = dy
        rect=self.image.get_rect()
        self.x += self.dx*rect.width/2
        self.y += self.dy*rect.height/2

    def __repr__(self):
        return f'{self.x=},{self.y=}'

    def move(self) -> bool:
        """
        ruch pocisku. zwraca czy jest na tablicy
        """
        self.x += self.dx * self.velocity
        self.y += self.dy * self.velocity
        return self.borderlize()
