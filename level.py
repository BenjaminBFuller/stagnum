from settings import *


class Level:
    def __init__(self):
        self.state = "menu"
        self.background = menu_bg
        self.curr_level_height_ceil = 150
        self.curr_level_height_floor = 350
        self.time = pg.time.get_ticks()
        self.text_bounce = 0

    def menu_titles(self, x1, y1, x2, y2):
        """
        Create, render, and blit menu titles to (x, y) positions on screen.
        Custom bouncing effect for (x1, y1) and blinking effect for (x2, y2)
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """
        title = title_font.render("STAGNUM", False, WHITE)
        screen.blit(title, (x1 + self.text_bounce, y1 + self.text_bounce))
        play_title = title_font.render("->", False, WHITE)

        cur = pg.time.get_ticks() - self.time
        if cur < 1000:
            screen.blit(play_title, (x2, y2))
            self.text_bounce += .05
        elif cur < 2000:
            self.text_bounce -= .05
        elif cur < 2500:
            self.time = pg.time.get_ticks()

    def draw(self):
        """
        Level draw function; blit based on level state
        :return:
        """
        if self.state == "menu":
            self.curr_level_height_ceil = 150
            self.curr_level_height_floor = 350
            screen.blit(self.background, (0, 0))
            self.menu_titles(.5 * tile, .5 * tile, 4 * tile, 7.5 * tile)
