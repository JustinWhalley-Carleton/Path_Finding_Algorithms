import pygame
from colors import *

# display how to use pane
def how_to_use(width):
    TEXTSPACING = 20
    HEADERSPACING = 25
    PARAGRAPHSPACING = 10
    display_surface = pygame.display.set_mode((width, width))
    pygame.display.set_caption('How To')

    header1 = make_header("Setting Points")
    header2 = make_header("Setting Algorithm")
    header3 = make_header("Reset")
    header4 = make_header("Execute")
    header5 = make_header("How To Read Results")
    header6 = make_header("Back To Menu")

    text1 = make_text("Choose the points you would like to add using the up and down keys. The current")
    text2 = make_text("choice of points is displayed in the bottom left corner. The orange point is start")
    text3 = make_text("point, the turqouise point is the end point and the black points are wall points.")
    text4 = make_text("There can only be 1 start and 1 end point. If another start or end point is added ")
    text5 = make_text("it will remove the other start or end point respectively.")

    text6 = make_text("Choose the algorithm to find the path using the left and right keys. The current")
    text7 = make_text("chosen algorithm is displayed in the bottom right corner.")

    text8 = make_text("To reset the grid, press the 'c' key.")

    text9 = make_text("To execute the algorithm, press the space key. Once completed the path length")
    text10 = make_text("will be displayed in the top right corner. No changes can be made to the grid")
    text11 = make_text("once the program is executed until the board is reset.")

    text12 = make_text("Once executed the points that have been checked will be colored in red, then")
    text13 = make_text("when the end point is found, the path will be colored in purple.")

    text14 = make_text("To go back to the menu, press the 'c' key.")

    while True:
        display_surface.fill(WHITE)
        i = 0
        j = 0
        display_surface.blit(header1, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text1, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text2, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text3, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text4, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text5, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header2, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text6, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text7, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header3, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text8, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header4, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text9, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text10, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text11, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header5, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text12, (i,j))
        j+=TEXTSPACING
        display_surface.blit(text13, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING

        display_surface.blit(header6, (i,j))
        j+=HEADERSPACING
        display_surface.blit(text14, (i,j))
        j+=TEXTSPACING+PARAGRAPHSPACING
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.display.set_caption("Menu")
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
#create text from parameter in the header font
def make_header(text):
    header_font = pygame.font.Font('freesansbold.ttf', 20)
    return header_font.render(text, True, BLACK, WHITE)
# create text from parameter in regular text font
def make_text(text):
    text_font = pygame.font.SysFont('timesnewroman',15)
    return text_font.render(text, True, BLACK, WHITE)