# Stagnum

from settings import *
from pygame.math import Vector2
from pygame.sprite import Group
import time
import sys


class Player(pg.sprite.Sprite):
    """
    Main Player controllable character class
    """
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.position = [1, 1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0] * tile, self.position[1] * tile)
        self.speed = 250

    def update(self, dt):
        """

        :param dt:
        :return:
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:  # key mapping
                # controls: WASD for move, SPACE for stop/resume, q for quit
                # SPACE will stop and resume movement and inputting WASD after stopping will also resume
                if event.key == pg.K_w:
                    # North
                    self.position[1] -= 1
                elif event.key == pg.K_d:
                    # East
                    self.position[0] += 1
                elif event.key == pg.K_s:
                    # South
                    self.position[1] += 1
                elif event.key == pg.K_a:
                    # West
                    self.position[0] -= 1
                if event.key == pg.K_q:
                    pg.quit()  # quit on keystroke q
                    sys.exit()

                if 0 <= self.position[1] <= screen_width - self.rect.width:
                    self.rect.x = self.position[0] * tile

                if 0 <= self.position[0] <= screen_height - self.rect.height:
                    self.rect.y = self.position[1] * tile



class Game:
    def __init__(self):
        self.previous_time = time.time()  # create clock for calculating delta time
        self.player = Player()

    def main(self):
        # group together sprites to update them altogether
        all_sprites = Group(self.player)
        while True:
            dt = time.time() - self.previous_time  # calculation of 1 game loop / delta time
            self.previous_time = time.time()  # start of delta time loop
            all_sprites.update(dt)
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            pg.display.flip()


if __name__ == "__main__":
    game = Game()
    game.main()
