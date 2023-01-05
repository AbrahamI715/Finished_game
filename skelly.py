import pygame


class Skelly(pygame.sprite.Sprite):
    def __init__(self, pos, skelly_group: pygame.sprite.Group()):
        super().__init__(skelly_group)


        self.image_scale = 2
        self.image = pygame.transform.rotozoom(pygame.image.load('skelly.png').convert_alpha(), 0, self.image_scale)


        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_shift):
        self.rect.x += x_shift