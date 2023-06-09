import pygame

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
FPS=60
TILESIZE=50
#r=rock, p=player N,E,W,S = north, east west and south doors

MAP = [
[' ',' ',' ',' ',' ',' ',' ','N',' ',' ',' ',' ',' ',' ',' '],
[' ','r','e',' ',' ',' ',' ',' ',' ',' ',' ',' ','e','r',''],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ','',' ',' ',' ',' ',' ',' ',' ','',' ',' ',' ',' '],
['W',' ','r','',' ',' ',' ','p',' ',' ','','',' ',' ','E'],
[' ',' ',' ','',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','',' ',' ',' ',' '],
[' ','r','e',' ',' ',' ',' ',' ',' ',' ',' ','','e','r',''],
[' ',' ',' ',' ',' ',' ',' ','S',' ',' ',' ',' ',' ',' ','']]

