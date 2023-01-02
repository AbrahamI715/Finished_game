import pygame
import pygame_gui
from pygame import mixer
from main_menu import MainMenuState
from game_state import GameState
from options_state import OptionsState
from high_score_state import HighScoreState
from Level_selector_state import LevelSelectState
from game_over_state import GameOverState
from test_level import TestLevelState
from level_2 import Level2State
from level_3 import Level3State
from level_4 import Level4State
from settings import *
from player import Player


class MyGameApp:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512) # configurations for sounds
        pygame.init()
        mixer.init()
        self.display_size = (screen_width, screen_height)
        self.display_surface = pygame.display.set_mode(self.display_size)

        self.clock = pygame.time.Clock()

        self.ui_manager = pygame_gui.UIManager(self.display_size)
        self.states = {'main_menu': MainMenuState(self.ui_manager),
                       'game': GameState(self.display_surface),
                       'options': OptionsState(self.ui_manager),
                       'high_scores': HighScoreState(self.ui_manager, self.display_surface),
                       'level_select': LevelSelectState(self.ui_manager, self.display_surface),
                       'test_level': TestLevelState(self.display_surface),
                       'level_2': Level2State(self.display_surface),
                       'level_3': Level3State(self.display_surface),
                       'level_4': Level4State(self.display_surface),
                       'game_over': GameOverState(self.ui_manager, self.display_surface)}
        self.active_state = self.states['main_menu']
        self.active_state.start()

        self.running = True

    def run(self):
        while self.running:
            time_delta = self.clock.tick(90)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.active_state.handle_event(event)
                self.ui_manager.process_events(event)

            self.ui_manager.update(time_delta)
            self.active_state.update(time_delta)

            self.active_state.draw(self.display_surface)

            pygame.display.flip()

            self.check_time_to_switch_state()

    def check_time_to_switch_state(self):
        if self.active_state.time_to_switch:
            self.active_state.stop()
            self.active_state = self.states[self.active_state.state_to_switch_to_id]
            self.active_state.start()


my_game = MyGameApp()
my_game.run()


