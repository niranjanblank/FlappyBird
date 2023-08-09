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

        # importing background for day and night
        background_day = pygame.image.load('assets/sprites/background-day.png').convert()
        background_night = pygame.image.load('assets/sprites/background-night.png').convert()
        self.background_frames = [background_day,background_night]
        self.background_index = 0
        # scaling the background to the size of window
        self.background = pygame.transform.smoothscale(self.background_frames[self.background_index], (WIDTH,HEIGHT))

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

            # set the background
            self.screen.blit(self.background,(0,0))


            #update the screen
            pygame.display.update()
            self.clock.tick(60)


if __name__ =="__main__":
    main = Main()
    main.run()