# Stagnum
from settings import *
from player import Player
from level import Level
from pygame.sprite import Group
import time


class Game:
    def __init__(self):
        self.previous_time = time.time()  # start initial instance of timer for calculating delta time
        self.player = Player((1 * tile, 4 * tile))
        self.sprite_group = Group(self.player)
        self.level = Level()

    def draw(self):
        self.level.draw()
        self.sprite_group.update()
        self.sprite_group.draw(screen)

    def main(self):
        clock = pg.time.Clock()
        # group together sprites to update them altogether
        while True:
            clock.tick(FPS)
            self.draw()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.main()
