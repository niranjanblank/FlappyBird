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

    def animate_state(self):
        self.bird_frame_index += 0.1
        if self.bird_frame_index >= len(self.bird_frames): self.bird_frame_index = 0
        self.image = self.bird_frames[int(self.bird_frame_index)]

    def update(self):
        self.animate_state()
