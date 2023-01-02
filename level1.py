import pygame
from tiles import TileGrass
from tiles_2 import TileDirt
from player import Player
from enemy import Enemy
from coins import Coins
from settings import tile_size, screen_width


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.tiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.player = None

        self.setup_level(level_data)
        self.display_surface = surface
        self.world_shift = 0
        self.world_scroll = 0

    def setup_level(self, layout):
        tile_set_image = pygame.image.load("terrain.png")
        test_tile = TileGrass((0, 0), (32, 32), 0, 0, tile_set_image)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = TileGrass((x, y), tile_size, 0, 0, tile_set_image)
                    self.tiles.add(tile)
                elif cell == 'D':
                    tile = TileDirt((x, y), tile_size, 0, 0, tile_set_image)
                    self.tiles.add(tile)
                elif cell == 'P':
                    self.player = Player((x, y), self.enemies, self.coin)
                    self.player_group.add(self.player)
                elif cell == 'E':
                    enemy = Enemy((x, y), self.enemies)
                    self.enemies.add(enemy)
                elif cell == 'C':
                    coins = Coins((x, y), self.coin)
                    self.coin.add(coins)

        self.background_images = []
        for i in range(1, 4):
            self.background_image = pygame.transform.smoothscale(
                pygame.image.load(f'background_layer_{i}.png').convert_alpha(), (1200, 720))
            self.background_images.append(self.background_image)
        self.background_width = self.background_images[0].get_width()

        # coin counter stuff
        self.font_score = pygame.font.SysFont('Bauhaus 93', 30)
        self.white = (255, 255, 255)

    def scroll_x(self):
        # scrolling camera for player
        player = self.player
        player_x = player.rect.centerx  # where player is on x coord
        direction_x = player.direction.x  # what direction player is moving in

        if player_x < screen_width / 4 and direction_x < 0:  # if player is heading left
            self.world_shift = 4
            player.speed = 0

        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:  # if player is heading right
            self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 4

        self.world_scroll += self.world_shift

    def horiz_collision(self):
        player = self.player
        player.collision_rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.collision_rect):  # more convenient so we have access to each of the tiles
                if player.direction.x < 0:  # if the player is moving left
                    player.collision_rect.left = sprite.rect.right
                    # collision happening on left side of player moves player to right side of obstacle it collided with
                elif player.direction.x > 0:
                    player.collision_rect.right = sprite.rect.left

    def vert_collision(self):
        player = self.player
        player.activate_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.collision_rect):  # more convenient so we have access to each of the tiles
                if player.direction.y > 0:
                    player.collision_rect.bottom = sprite.rect.top
                    player.direction.y = 0  # gravity cancels out
                elif player.direction.y < 0:  # if the player is jumping
                    player.collision_rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self, time_delta):
        # tiles
        self.tiles.update(self.world_shift)  # 0 is the default position but when put at -1 or 1 level will shift
        self.enemies.update(self.world_shift)
        self.coin.update(self.world_shift)
        # player
        self.player_group.update(time_delta)
        self.vert_collision()
        self.horiz_collision()

    def draw(self):
        self.draw_background()
        self.tiles.draw(self.display_surface)
        self.draw_text("coins collected: " + str(self.player.player_coins), self.font_score, self.white, 25, 25)
        self.enemies.draw(self.display_surface)
        self.coin.draw(self.display_surface)
        self.player_group.draw(self.display_surface)
        self.scroll_x()
        #pygame.draw.rect(self.display_surface, pygame.Color('#FF0000'), self.player.rect, 1)
        #pygame.draw.rect(self.display_surface, pygame.Color('#FF00FF'), self.player.collision_rect, 1)

    def draw_background(self):
        for x in range(8):
            self.speed = 0.5
            for i in self.background_images:
                position = ((x * self.background_width) + self.world_scroll * self.speed, 0)
                self.display_surface.blit(i, position)
                self.speed += 0.12

    def draw_text(self, text, font,text_col,x,y):
        self.img = font.render(text, True, text_col)
        self.display_surface.blit(self.img, (x, y))



