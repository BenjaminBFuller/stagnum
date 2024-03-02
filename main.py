# Stagnum
import level
from settings import *
from player import Player
from level import Level
import time


class Game:
    def __init__(self):
        self.previous_time = time.time()  # start initial instance of timer for calculating delta time
        self.level = Level()

    def main(self):
        clock = pg.time.Clock()
        # group together sprites to update them altogether
        while True:
            clock.tick(FPS)
            self.level.draw()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.main()
