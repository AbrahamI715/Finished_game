import pygame


class TileGrass(pygame.sprite.Sprite):
    def __init__(self,
                 pos,
                 size,
                 tile_set_x_pos,
                 tile_set_y_pos,
                 tile_set):
        super().__init__()
        tile_size = 60
        tile_set_sub_surf_rect = pygame.Rect(tile_set_x_pos * tile_size + 60,
                                             tile_set_y_pos * tile_size,
                                             tile_size,
                                             tile_size)
        self.image = pygame.transform.smoothscale(tile_set.subsurface(tile_set_sub_surf_rect), (60, 60))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
