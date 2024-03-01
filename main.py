# Stagnum

from settings import *
from player import Player
from pygame.math import Vector2
from pygame.sprite import Group
import time
import sys


class Game:
    def __init__(self):
        self.previous_time = time.time()  # start initial instance of timer for calculating delta time
        self.player = Player()

    def main(self):
        clock = pg.time.Clock()
        # group together sprites to update them altogether
        all_sprites = Group(self.player)
        while True:
            clock.tick(FPS)
            all_sprites.update()
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.main()
