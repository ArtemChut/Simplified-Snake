import pygame
from pygame.locals import *
import csv
import sys

def main():
    pygame.init()
    pygame.font.init()

    width, height = 800, 680
    screen = pygame.display.set_mode((width, height))

    font_colour, card_colour, background_colour = "black", "darkRed", "red"


    def find_button():
        x,y = event.pos

        # choosing a difficulty
        if width*0.15 <= x <= width*0.85:
            if height*0.2 <= y <= height*0.4:
                import snake
                snake.main("easy")
                return # exit
            elif height*0.5 <= y <= height*0.8:
                import snake
                snake.main("hard")
                return # exit
    


    name_font = pygame.font.SysFont("couriernew", 28)
    description_font = pygame.font.SysFont("arial", 20)

    while True:
        screen.fill(background_colour)

        name_text = name_font.render("Snake", False, font_colour)
        screen.blit(name_text, (width*0.47,height*0.1))

        # easy mode button
        pygame.draw.rect(screen, card_colour, (width*0.15,height*0.2, width*0.7,height*0.2),0, 16)
        description_text = description_font.render("Easy mode \n(teleporting through walls)", False, font_colour)
        screen.blit(description_text, (width*0.4, height*0.25))

        # hard mode button
        pygame.draw.rect(screen, card_colour, (width*0.15,height*0.5, width*0.7,height*0.2),0, 16)
        description_text = description_font.render("Hard mode \n(can't teleport through walls)", False, font_colour)
        screen.blit(description_text, (width*0.4, height*0.55))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    find_button()



        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
