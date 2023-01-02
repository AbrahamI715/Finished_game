import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, enemies_group: pygame.sprite.Group):
        super().__init__(enemies_group)

        self.image_scale = 1.75
        self.image = pygame.transform.rotozoom(pygame.image.load('slime.png').convert_alpha(), 0, self.image_scale)

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.move_direction = 1
        self.move_counter = 0
        self.direction = pygame.math.Vector2(1, 0)  # movement is all in one neat variable :)

    def update(self, x_shift):
        self.rect.x += (x_shift + self.direction.x)



