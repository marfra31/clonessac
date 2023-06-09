import pygame, sys
# from button import Button
from room import Room
# from character import Character
# from objects import Object
# from enemy import Enemy
# from menu import main_menu
# from debug import debug
from settings import *

# def get_font(size):  # Returns Press-Start-2P in the desired size
#     return pygame.font.Font("font.ttf", size)


# def play(fullscreen=True):
#     if fullscreen:
#         screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
#     else:
#         screen = pygame.display.set_mode((width, height))
#     pygame.init()
#     pygame.display.set_caption("Clonessac")
#     FPS = 60

#     room = Room("Images/game.png")
#     enemy = Enemy("Images/Enemy.png", 500, 300)
    # character = Character("Images/Character.png", 100, 300)

    # rock = Object("Images/rock.png", 80, 175)
    # rock2 = Object("Images/rock2.png", 80, 470)
    # rock3 = Object("Images/rock.png", 675, 175)
    # rock4 = Object("Images/rock2.png", 670, 470)
    # rock5 = Object("Images/rock.png", 375, 300)
    # listOfObjects = [rock, rock2, rock3, rock4, rock5]

#     running = True
#     clock = pygame.time.Clock()

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         keys = pygame.key.get_pressed()
#         for item in pygame.sprite.Group():
#             if enemy.check_collision(item):
#                 enemy.rollback_movement()
#         if enemy.check_collision_character(room.character):
#             enemy.rollback_movement()
#         screen.fill((0, 0, 0))
#         room.draw(screen)
#         enemy.draw(screen)
#         room.run()
#         # for item in listOfObjects:
#         #     item.draw(screen)
#         pygame.display.update()
#         clock.tick(FPS)

#     pygame.quit()



# if __name__ == "__main__":
#     play(fullscreen=False)






class Game:
    def __init__(self):
		  
		# general setup
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Room("Images/game.png")
        # self.level=Level()
	
    def run(self):
    	while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()	