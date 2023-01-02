import pygame.draw
import pygame_gui

from level1 import Level
from tiles import TileGrass


class OptionsState:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        self.keyboard_control_button = None
        self.audio_button = None
        self.Dyslexia_friendly_button = None
        self.Back_button = None

    def start(self):
        self.time_to_switch = False
        self.keyboard_control_button = pygame_gui.elements.UIButton(pygame.Rect(525, 200, 150, 30), "Keyboard controls",
                                                                    self.ui_manager)
        self.audio_button = pygame_gui.elements.UIButton(pygame.Rect(525, 250, 150, 30),
                                                           "Audio",
                                                           self.ui_manager)
        self.Dyslexia_friendly_button = pygame_gui.elements.UIButton(pygame.Rect(525, 300, 150, 30),
                                                     "Dyslexia Mode",
                                                     self.ui_manager)
        self.Back_button = pygame_gui.elements.UIButton(pygame.Rect(525, 350, 150, 30),
                                                        "Back",
                                                        self.ui_manager)

    def update(self, time_delta):
        pass

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "main_menu"

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.Back_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'main_menu'

    def stop(self):
        self.keyboard_control_button.kill()
        self.keyboard_control_button = None

        self.audio_button.kill()
        self.audio_button = None

        self.Dyslexia_friendly_button.kill()
        self.Dyslexia_friendly_button = None

        self.Back_button.kill()
        self.Back_button = None

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.ui_manager.draw_ui(display_surface)
