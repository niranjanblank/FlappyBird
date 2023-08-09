import pygame.display
from sys import exit
from settings import *

class Main:
    """
    This class will be used to run the event loop
    """
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # title of game
        pygame.display.set_caption("Flappy Bird")
        # icon for game
        icon = pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha()
        pygame.display.set_icon(icon)
        # screen to render the game

        self.clock = pygame.time.Clock()

    def run(self):
        """
        Event loop will be initiated here
        """
        while(True):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()



            #update the screen
            pygame.display.update()
            self.clock.tick(60)


if __name__ =="__main__":
    main = Main()
    main.run()