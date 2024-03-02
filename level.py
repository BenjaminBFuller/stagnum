from settings import *
from pygame.sprite import Group
from player import Player


class Level:
    def __init__(self):
        self.state = "menu"
        self.player = Player((1 * tile, 4 * tile))
        self.background = menu_bg
        self.curr_level_height_ceil = 150
        self.curr_level_height_floor = 350
        self.sprite_group = Group(self.player)

    def draw(self):
        if self.state == "menu":
            self.curr_level_height_ceil = 150
            self.curr_level_height_floor = 350
            screen.blit(self.background, (0, 0))
        self.sprite_group.update()
        self.sprite_group.draw(screen)
