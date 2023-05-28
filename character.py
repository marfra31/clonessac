import pygame

class Character:
    def __init__(self, image_path, x, y,width,height):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.min_x = 75
        self.max_x = width - self.image.get_width()-75
        self.min_y = 175
        self.max_y = height - self.image.get_height()-75
    def handle_movement(self, keys):
        self.prev_x = self.x
        self.prev_y = self.y

        if keys[pygame.K_a]:
            self.x -= 5
            self.x = max(self.x, self.min_x)
        if keys[pygame.K_d]:
            self.x += 5
            self.x = min(self.x, self.max_x)
        if keys[pygame.K_w]:
            self.y -= 5
            self.y = max(self.y, self.min_y)
        if keys[pygame.K_s]:
            self.y += 5
            self.y = min(self.y, self.max_y)

    def check_collision(self, other):
        character_rect = self.image.get_rect()
        character_rect.x = self.x
        character_rect.y = self.y

        other_rect = other.image.get_rect()
        other_rect.x = other.x
        other_rect.y = other.y

        return character_rect.colliderect(other_rect)

    def rollback_movement(self):
        self.x = self.prev_x
        self.y = self.prev_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
