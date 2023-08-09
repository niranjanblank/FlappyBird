import pygame.display
from sys import exit
from settings import *
from game import *
from random import randint

class Main:
    """
    This class will be used to run the event loop
    """
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # active state
        self.game_state = 1
        # importing background for day and night
        background_day = pygame.image.load('assets/sprites/background-day.png').convert()
        background_night = pygame.image.load('assets/sprites/background-night.png').convert()
        self.background_frames = [background_day,background_night]
        self.background_index = 0
        # scaling the background to the size of window
        self.background = pygame.transform.smoothscale(self.background_frames[self.background_index], (WIDTH,HEIGHT))

        # text
        self.font = pygame.font.Font('assets/fonts/flappy-font.ttf',80)

        #ground
        ground = pygame.image.load('assets/sprites/base.png').convert()

        self.ground = pygame.transform.smoothscale(ground, (WIDTH,ground.get_height()))
        self.ground_rect = self.ground.get_rect(topleft=(0, GROUND_POSITION_Y))
        self.ground_repeat = pygame.transform.smoothscale(ground, (WIDTH, ground.get_height()))
        self.ground_repeat_rect = self.ground_repeat.get_rect(topleft=(-WIDTH, GROUND_POSITION_Y))

        # title of game
        pygame.display.set_caption("Flappy Bird")
        # icon for game
        icon = pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha()
        pygame.display.set_icon(icon)
        # screen to render the game

        #bird
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Bird())

        # obstacles
        self.obstacles = pygame.sprite.Group()

        self.clock = pygame.time.Clock()



        # timer for obstacle
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 2500)


    def render_score(self, pos):
        font = pygame.font.Font('assets/fonts/flappy-font.ttf', 80)
        font_2 =  pygame.font.Font('assets/fonts/flappy-font.ttf', 90)
        score_message_border = font_2.render(f'{self.player.sprite.score}', False, 'black')
        score_message_border_rect = score_message_border.get_rect(center=pos)

        self.screen.blit(score_message_border, score_message_border_rect)
        score_message = font.render(f'{self.player.sprite.score}', False, 'white')
        score_message_rect = score_message.get_rect(center=pos)
        self.screen.blit(score_message, score_message_rect)
        # border

    def collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacles, False) or self.player.sprite.rect.bottom >= GROUND_POSITION_Y:
            # game over state
            self.game_state = 2

    def run(self):
        """
        Event loop will be initiated here
        """
        while(True):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                # spawn obstacle
                if self.game_state == 1:
                    if event.type == self.obstacle_timer:
                        bottom_center_position = randint(500, HEIGHT)
                        self.obstacles.add(Pipe('bottom', bottom_center_position))
                        top_center_position = bottom_center_position - 800
                        self.obstacles.add(Pipe('top', top_center_position))
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_state = 1
                        self.obstacles.empty()
                        self.player.sprite.reset()

            # set the background

            self.screen.blit(self.background, (0, 0))

            # render the obstacles
            self.obstacles.draw(self.screen)

            # set the ground
            self.screen.blit(self.ground, self.ground_rect)
            self.screen.blit(self.ground_repeat, self.ground_repeat_rect)


            # update logics when game state is active
            if self.game_state == 1:

                self.obstacles.update()

                # checking if the ground went out of screen and re-rendering based on it
                if self.ground_rect.right<2:
                    self.ground_rect.left = WIDTH
                if self.ground_repeat_rect.right <2:
                    self.ground_repeat_rect.left = WIDTH


                self.ground_rect.x -= 2
                self.ground_repeat_rect.x -= 2

                # check collision
                self.collision()

                # score points
                if self.game_state == 1:
                    self.player.sprite.score_point(self.obstacles)

                # render score
                self.render_score((WIDTH // 2, 100))

                # render the player/bird
                self.player.draw(self.screen)
                # update the player
                self.player.update()
            else:
                # render the player/bird
                self.player.draw(self.screen)
                self.render_score((WIDTH // 2, HEIGHT // 2 - 100))
                game_over = pygame.transform.rotozoom(pygame.image.load('assets/sprites/gameover.png').convert_alpha(),0,2)
                game_over_rect = game_over.get_rect(center=((WIDTH // 2, HEIGHT // 2)))
                self.screen.blit(game_over, game_over_rect)
                font = pygame.font.Font('assets/fonts/flappy-font.ttf',30)
                restart_message = font.render('Press space to restart',False, 'black')
                restart_rect = restart_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
                self.screen.blit(restart_message, restart_rect)


            #update the screen
            pygame.display.update()
            self.clock.tick(60)


if __name__ =="__main__":
    main = Main()
    main.run()