import pygame, sys
from button import Button
from main import main

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gra")

BG = pygame.image.load("tlomenu.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
#
#         SCREEN.fill("white")
#
#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
#
#         OPTIONS_BACK = Button(image=None, pos=(640, 460),
#                               text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
#
#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()
#

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("GRA TYPU ZELDA", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 300),
                             text_input="GRAJ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400),
        #                         text_input="ZAPIS?", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 450),
                             text_input="WYJŚCIE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()