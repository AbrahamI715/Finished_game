import pygame


class Right_turntile(pygame.sprite.Sprite):
    def __init__(self, pos, right_turn_group: pygame.sprite.Group):
        super().__init__(right_turn_group)

        width = 60
        height = 60


        self.image = pygame.Surface([width, height])
        self.image.fill('#00000000')

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_shift):
        self.rect.x += x_shift
