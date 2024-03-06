# Stagnum main script
from settings import *
from player import Player
from level import Level
from pygame.sprite import Group
import time


class Game:
    def __init__(self):
        self.previous_time = time.time()  # start initial instance of timer for calculating delta time
        self.level = Level()
        self.player = Player((height/2, width/2))
        self.sprite_group = Group(self.player)

    def draw(self):
        #
        """
        Draw function;
        draw all current entities onto the screen
        """
        self.level.draw()
        self.sprite_group.update()
        self.sprite_group.draw(screen)

    def main(self):
        """
        Main game loop, encapsulates all draw and update functions
        """
        clock = pg.time.Clock()
        # group together sprites to update them altogether
        while True:
            clock.tick(FPS)
            self.draw()
            pg.display.flip()


if __name__ == "__main__":
    # Create game instance and run main game loop
    game = Game()
    game.main()
