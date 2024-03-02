from settings import *


class Level:
    def __init__(self):
        self.state = "menu"
        self.background = menu_bg
        self.curr_level_height_ceil = 150
        self.curr_level_height_floor = 350

    def draw(self):
        if self.state == "menu":
            self.curr_level_height_ceil = 150
            self.curr_level_height_floor = 350
            screen.blit(self.background, (0, 0))
