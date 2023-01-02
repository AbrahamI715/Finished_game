import pygame.draw
import pygame_gui


class MainMenuState:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        self.new_game_button = None
        self.options_button = None
        self.quit_button = None
        self.high_score_button = None

    def start(self):
        self.time_to_switch = False
        self.new_game_button = pygame_gui.elements.UIButton(pygame.Rect(525, 200, 150, 30),
                                                            "New Game",
                                                            self.ui_manager)
        self.options_button = pygame_gui.elements.UIButton(pygame.Rect(525, 250, 150, 30),
                                                           "Options",
                                                           self.ui_manager)
        self.quit_button = pygame_gui.elements.UIButton(pygame.Rect(525, 350, 150, 30),
                                                        "Quit",
                                                        self.ui_manager)
        self.high_score_button = pygame_gui.elements.UIButton(pygame.Rect(525, 300, 150, 30),
                                                              "High Scores",
                                                              self.ui_manager)


    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.new_game_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = "level_select"
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.options_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = "options"
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.quit_button:
            quit()
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.high_score_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = "high_scores"

    def update(self, time_delta):
        pass

    def stop(self):
        self.new_game_button.kill()
        self.new_game_button = None

        self.options_button.kill()
        self.options_button = None

        self.quit_button.kill()
        self.quit_button = None

        self.high_score_button.kill()
        self.high_score_button = None

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.ui_manager.draw_ui(display_surface)
