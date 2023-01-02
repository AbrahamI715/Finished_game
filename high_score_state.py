import pygame.draw
import pygame_gui

from file_interactions import FileInteractions


class HighScoreState:
    def __init__(self, ui_manager, display_surface):
        self.ui_manager = ui_manager
        self.display_surface = display_surface

        self.time_to_switch = False
        self.state_to_switch_to_id = ""

        self.back_button = None

        # getting the high scores
        self.file_interactor = None
        self.high_scores = None

        # used to print all the high scores
        # I set it to hold 4 items to represent 4 levels
        self.uilabels_list = []

    def start(self):
        self.time_to_switch = False

        self.back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(525, 200, 150, 30),
                                                        text="Back",
                                                        manager=self.ui_manager)
        # make the file interactor
        # and load the high scores into a variable
        self.file_interactor = FileInteractions()
        self.file_interactor.load()
        self.high_scores = self.file_interactor.level_scores_data

        # printing the scores
        y_position_increment = 0  # shifts each label down by a few pixels
        # loop through every level's high score
        # in this case there are 4 levels
        for line in self.high_scores:
            # make a rect to hold the UILabel
            uilabel_position_rect = pygame.Rect(0, 0, 400, 40)
            # set the rect's position in the middle of the screen
            uilabel_position_rect.centerx = self.display_surface.get_rect().centerx
            # set the top of the rect to be 40% of the screen's height
            # and then add the increment so future labels move slightly down
            uilabel_position_rect.top = (self.display_surface.get_height() * 0.4) + y_position_increment

            # text to display
            text = 'Best level ' + line['level'] + ' kills: ' + line['kills'] + ' and coins collected: ' + line['coins']

            # make uiLabel
            # uilabels are basically just text boxes
            # you cant click them or anything
            self.uilabels_list.append(
                pygame_gui.elements.UILabel(relative_rect=uilabel_position_rect,
                                            text=text,
                                            manager=self.ui_manager)
            )
            y_position_increment += 50  # add 50 to the increment

    def stop(self):
        self.time_to_switch = False
        self.back_button.kill()
        self.back_button = None
        self.file_interactor = None

        # kill all the labels you made
        for label in self.uilabels_list:
            label.kill()
        self.uilabels_list = []

    def handle_event(self, event: pygame.event.Event):
        self.ui_manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.back_button:
            self.time_to_switch = True
            self.state_to_switch_to_id = 'main_menu'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.time_to_switch = True
            self.state_to_switch_to_id = "main_menu"

    def update(self, time_delta):
        self.ui_manager.update(time_delta)

    def draw(self, display_surface):
        display_surface.fill((0, 0, 0))
        self.ui_manager.draw_ui(display_surface)
