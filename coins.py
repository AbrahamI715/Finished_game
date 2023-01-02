import pygame


class Coins(pygame.sprite.Sprite):
    def __init__(self, pos, coin_group: pygame.sprite.Group()):
        super().__init__(coin_group)


        self.image_scale = 0.12
        self.image = pygame.transform.rotozoom(pygame.image.load('coin.png').convert_alpha(), 0, self.image_scale)


        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_shift):
        self.rect.x += x_shift
