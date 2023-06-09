import pygame, sys
from room import Room
from settings import *
from menu import main_menu

class Game:
    def __init__(self,fullscreen=True):
		  
		# general setup
        pygame.init()
        if fullscreen:
            self.screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Clonessac')
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
def play():
    game=Game()
    game.run()
if __name__ == '__main__':
    main_menu(play)