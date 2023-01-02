import pygame.draw
import pygame_gui


class LevelSelectState:
    def __init__(self, ui_manager, display_surface):
        self.ui_manager = ui_manager
        self.display_surface = display_surface

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        self.back_button = None
        self.level_1_button = None
        self.level_2_button = None
        self.level_3_button = None
        self.level_4_button = None

    def start(self):
        self.time_to_switch = False

        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 200, 150, 30),
                                                        text="Back",
                                                        manager=self.ui_manager)
        self.level_1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 250, 150, 30),
                                                        text="Level 1",
                                                        manager=self.ui_manager)
        self.level_2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 300, 150, 30),
                                                           text="Level 2",
                                                           manager=self.ui_manager)
        self.level_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 350, 150, 30),
                                                           text="Level 3",
                                                           manager=self.ui_manager)
        self.level_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 400, 150, 30),
                                                           text="Level 4",
                                                           manager=self.ui_manager)


    def stop(self):
        self.time_to_switch = False
        self.back_button.kill()
        self.back_button = None
        self.level_1_button.kill()
        self.level_1_button = None
        self.level_2_button.kill()
        self.level_2_button = None
        self.level_3_button.kill()
        self.level_3_button = None
        self.level_4_button.kill()
        self.level_4_button = None


    def handle_event(self, event: pygame.event.Event):
        self.ui_manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.back_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'main_menu'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "main_menu"

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.level_1_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'test_level'

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.level_2_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'level_2'

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.level_3_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'level_3'

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.level_4_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'level_4'

    def update(self, time_delta):
        self.ui_manager.update(time_delta)

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.ui_manager.draw_ui(display_surface)