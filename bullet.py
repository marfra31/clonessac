from dynamicobject import DynamicObject


class Bullet(DynamicObject):

    def __init__(self, width: int, height: int, x: int, y: int, dx: int, dy: int, v: int) -> None:
        super().__init__(width, height, "Images/tear.png", x, y, v)
        self.dx = dx
        self.dy = dy
        rect=self.image.get_rect()
        self.x += self.dx*rect.width/2
        self.y += self.dy*rect.height/2

    def __repr__(self):
        return f'{self.x=},{self.y=}'

    def move(self) -> bool:
        self.x += self.dx * self.velocity
        self.y += self.dy * self.velocity
        return self.borderlize()

    # def handle_bullets(self, keys):

    #     if keys[pygame.K_LEFT] and len(tears) < MAX_BULLET:
    #         tear = pygame.Rect(
    #             self.x, self.y + self.y//2 - 6, 12, 12)
    #         tears.append(tear)
    #     if keys[pygame.K_RIGHT] and len(tears) < MAX_BULLET:
    #         tear = pygame.Rect(
    #             self.x + self.width, self.y + self.y//2 - 6, 12, 12)
    #         tears.append(tear)
    #     if keys[pygame.K_UP] and len(tears) < MAX_BULLET:
    #         tear = pygame.Rect(
    #             self.x + self.width//2 - 6, self.y, 12, 12)
    #         tears.append(tear)
    #     if keys[pygame.K_DOWN] and len(tears) < MAX_BULLET:
    #         tear = pygame.Rect(
    #             self.x + self.width//2 - 6, self.y + self.height, 12, 12)
    #         tears.append(tear)

    #     for tear in tears:
    #         pygame.draw.Rect(50, 50, (255, 255, 255), tear)


# def handle_tears(tears, enemy, keys):
#     if keys[pygame.K_RIGHT]:
#         for tear in tears:
#             tear.x += BULLET_VEL
#             if red.colliderect(bullet):
#                 pygame.event.post(pygame.event.Event(RED_HIT))
#                 yellow_bullets.remove(bullet)
#             elif bullet.x > WIDTH:
#                 yellow_bullets.remove(bullet)

#     for bullet in red_bullets:
#         bullet.x -= BULLET_VEL
#         if yellow.colliderect(bullet):
#             pygame.event.post(pygame.event.Event(YELLOW_HIT))
#             red_bullets.remove(bullet)
#         elif bullet.x < 0:
#             red_bullets.remove(bullet)
