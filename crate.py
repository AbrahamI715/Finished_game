import pygame


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, pos, item_box_group: pygame.sprite.Group):
        super().__init__(item_box_group)


        self.image = pygame.image.load('crate.png')

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, x_shift):
        self.rect.x += x_shift
