import pygame
import pygame.draw
from tiles import TileGrass
from tiles_2 import TileDirt
from player import Player
from file_interactions import FileInteractions
from enemy import Enemy
from coins import Coins
from crate import ItemBox
from Left_tile import Left_turntile
from Right_tile import Right_turntile
from settings import tile_size, screen_width
from settings import *



class TestLevelState:
    def __init__(self, display_surface):
        self.display_surface = display_surface

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        # level setup
        self.tiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.item_box = pygame.sprite.Group()
        self.left_tile = pygame.sprite.Group()
        self.right_tile = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.player = None

        self.level = None
        self.level_data = level_map1

        self.world_shift = 0
        self.world_scroll = 0

        self.background_images = []
        self.background_image = None
        self.background_width = None
        self.speed = 0

        # will be updated in stop()
        self.player_kills = 0
        self.player_coins = 0


        self.file_interactor = None

    def start(self):
        self.time_to_switch = False
        self.file_interactor = FileInteractions()

        self.setup_level()

    def stop(self):

        # save the player's score
        # first get the player's score from level
        self.player_kills = self.player.player_kills
        self.player_coins = self.player.player_coins
        # load the high scores from the file
        self.file_interactor.load()
        # update high scores
        self.file_interactor.add_high_score(level=1,
                                            player_kills=self.player_kills, player_coins=self.player_coins)

        # save scores
        self.file_interactor.save()

        # reset level
        self.level = None

        for tile in self.tiles:
            if tile is not None:
                tile.kill()
        tiles = []

        for coin in self.coin:
            if coin is not None:
                coin.kill()
        coin = []

        for enemy in self.enemies:
            if enemy is not None:
                enemy.kill()
        enemy = []

        for item in self.item_box:
            if item is not None:
                item.kill()
        item = []

        for left in self.left_tile:
            if left is not None:
                left.kill()
        left = []

        for right in self.right_tile:
            if right is not None:
                right.kill()
        right = []

        self.player = None

        self.background_images = []
        self.background_image = None
        self.background_width = None

        self.ambience_fx.stop()

    def setup_level(self):
        tile_set_image = pygame.image.load("terrain.png")
        test_tile = TileGrass((0, 0), (32, 32), 0, 0, tile_set_image)

        for row_index, row in enumerate(self.level_data):
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
                    self.player = Player((x, y), self.enemies, self.coin, self.item_box, self.left_tile, self.right_tile)
                    self.player_group.add(self.player)
                elif cell == 'E':
                    enemy = Enemy((x, y + 20), self.enemies)
                    self.enemies.add(enemy)
                elif cell == 'C':
                    coins = Coins((x, y), self.coin)
                    self.coin.add(coins)
                elif cell == 'I':
                    item = ItemBox((x, y + 20), self.item_box)
                    self.item_box.add(item)
                elif cell == 'L':
                    left = Left_turntile((x, y), self.left_tile)
                    self.left_tile.add(left)
                elif cell == 'R':
                    right = Right_turntile((x, y), self.right_tile)
                    self.right_tile.add(right)

        for i in range(1, 4):
            self.background_image = pygame.transform.smoothscale(
                pygame.image.load(f'background_layer_{i}.png').convert_alpha(), (1200, 720))
            self.background_images.append(self.background_image)
        self.background_width = self.background_images[0].get_width()

        # coin counter stuff
        self.font_score = pygame.font.SysFont('Bauhaus 93', 30)
        self.font_score_2 = pygame.font.SysFont('Bauhaus 93', 20)
        self.white = (255, 255, 255)

        # music settings
        self.ambience_fx = pygame.mixer.Sound('field_theme_1.wav')
        self.jump_fx = pygame.mixer.Sound('Jump.wav')
        self.ambience_fx.set_volume(0.5)
        self.jump_fx.set_volume(0.5)
        self.ambience_fx.play()

        # player health
        self.current_health = 200
        self.max_health = 200
        self.health_bar_length = 300
        self.health_ratio = self.max_health / self.health_bar_length

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

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -=  amount
        if self.current_health <= 0:
            self.current_health = 0

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

    def basic_health(self):
        pygame.draw.rect(self.display_surface, (255,0,0), (875, 25, self.current_health/ self.health_ratio, 25))
        pygame.draw.rect(self.display_surface, (255, 255, 255), (875, 25, self.health_bar_length, 25), 4)

    def update(self, time_delta):
        player = self.player
        # tiles
        self.tiles.update(self.world_shift)  # 0 is the default position but when put at -1 or 1 level will shift
        self.enemies.update(self.world_shift)
        self.coin.update(self.world_shift)
        self.item_box.update(self.world_shift)
        self.left_tile.update(self.world_shift)
        self.right_tile.update(self.world_shift)
        # player
        self.player_group.update(time_delta)
        self.vert_collision()
        self.horiz_collision()

        for sprite in self.enemies.sprites():
            if sprite.rect.colliderect(player.collision_rect):
                self.get_damage(2)
                if self.current_health == 0:
                    self.time_to_switch = True
                    self.state_to_switch_to_id = "game_over"


    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "level_select"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            self.stop()
            self.start()

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.left_tile.draw(self.display_surface)
        self.right_tile.draw(self.display_surface)
        self.draw_background()
        self.tiles.draw(self.display_surface)
        self.basic_health()
        self.draw_text("coins collected: " + str(self.player.player_coins), self.font_score, self.white, 25, 25)
        self.draw_text("(press r to reset)", self.font_score_2, self.white, 25, 45)
        self.enemies.draw(self.display_surface)
        self.item_box.draw(self.display_surface)
        self.coin.draw(self.display_surface)
        self.player_group.draw(self.display_surface)
        self.scroll_x()
