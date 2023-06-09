from staticobject import StaticObject


class Room(StaticObject):
    def __init__(self, background_image_path):
        super().__init__(background_image_path, 0, 0)
