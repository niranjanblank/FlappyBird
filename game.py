from settings import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_1 = pygame.transform.rotozoom(pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha(), 0, 1.5)
        bird_2 = pygame.transform.rotozoom(pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha(), 0, 1.5)
        bird_3 = pygame.transform.rotozoom(pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha(), 0, 1.5)
        self.bird_frames = [bird_1, bird_2, bird_3]
        self.bird_frame_index = 0
        self.image = self.bird_frames[self.bird_frame_index]
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT//2))
        self.gravity = 0
    def animate_state(self):
        self.bird_frame_index += 0.1
        if self.bird_frame_index >= len(self.bird_frames): self.bird_frame_index = 0
        self.image = self.bird_frames[int(self.bird_frame_index)]

    def apply_gravity(self):
        self.gravity += 1
        if self.rect.bottom >GROUND_POSITION_Y:
            self.gravity = 0
        self.rect.y += self.gravity

        if self.rect.bottom >= GROUND_POSITION_Y:
            self.rect.bottom = GROUND_POSITION_Y

    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -15
    def update(self):
        self.animate_state()
        self.apply_gravity()
        self.user_input()

