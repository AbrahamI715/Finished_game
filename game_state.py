import pygame.draw
from settings import *
from tiles import TileGrass
from level1 import Level
from player import Player
from file_interactions import FileInteractions


"""scroll = 0
key = pygame.key.get_pressed()
if key[pygame.K_a] and scroll > 0:
    scroll -= 5
if key[pygame.K_d] and scroll < 3000:
    scroll += 5"""


class GameState:
    def __init__(self, display_surface):
        self.time_to_switch = False
        self.state_to_switch_to_id = ""
        self.display_surface = display_surface
        self.level = None

        # will be updated in stop()
        self.player_kills = 0
        self.player_coins = 0


        self.file_interactor = None

    def start(self):
        self.time_to_switch = False
        self.file_interactor = FileInteractions()

        self.level = Level(level_map1, self.display_surface)

    def update(self, time_delta):
        self.level.run(time_delta)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "level_select"

    def stop(self):

        # save the player's score
        # first get the player's score from level
        self.player_kills = self.level.player.player_kills
        self.player_coins = self.level.player.player_coins
        # load the high scores from the file
        self.file_interactor.load()
        # update high scores
        self.file_interactor.add_high_score(level=1,
                                            player_kills=self.player_kills, player_coins=self.player_coins)
        # save scores
        self.file_interactor.save()

        # reset level
        self.level = None

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.level.draw()



