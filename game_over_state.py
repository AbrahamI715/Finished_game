import pygame.draw
import pygame_gui


class GameOverState:
    def __init__(self, ui_manager, display_surface):
        self.ui_manager = ui_manager
        self.display_surface = display_surface

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        self.back_button = None

        self.font_score = pygame.font.SysFont('Bauhaus 93', 60)
        self.font_score_2 = pygame.font.SysFont('Bauhaus 93', 30)
        self.white = (255, 255, 255)

        self.game_over_fx = pygame.mixer.Sound('Determination.mp3')
        self.game_over_fx.set_volume(0.5)

    def start(self):
        self.time_to_switch = False

        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 200, 150, 30),
                                                        text="Back",
                                                        manager=self.ui_manager)
        self.game_over_fx.play()


    def stop(self):
        self.time_to_switch = False
        self.back_button.kill()
        self.back_button = None

        self.game_over_fx.stop()

    def draw_text(self, text, font,text_col,x,y):
        self.img = font.render(text, True, text_col)
        self.display_surface.blit(self.img, (x, y))

    def handle_event(self, event: pygame.event.Event):
        self.ui_manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.back_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'level_select'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "level_select"

    def update(self, time_delta):
        self.ui_manager.update(time_delta)

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.ui_manager.draw_ui(display_surface)
        self.draw_text("Game over", self.font_score, self.white, 485, 300)
        self.draw_text("Try again?", self.font_score_2, self.white, 550, 350)
