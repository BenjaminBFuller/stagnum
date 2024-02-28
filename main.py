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
        self.rect = self.image.get_rect()
        self.rect.center = (1 * tile, 1 * tile)
        self.direction = Vector2()
        self.position = Vector2(self.rect.center)
        self.last_position = self.position
        self.is_moving = False
        self.speed = 150

    def input(self):
        keys = pg.key.get_pressed()
        self.is_moving = False

        # direction handling
        # [WASD] keys for player direction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()  # quit on keystroke q
                    sys.exit()

        if keys[pg.K_w]:
            self.direction.y = -1
            self.is_moving = True
        elif keys[pg.K_s]:
            self.direction.y = 1
            self.is_moving = True
        else:
            self.direction.y = 0

        if keys[pg.K_a]:
            self.direction.x = -1
            self.is_moving = True
        elif keys[pg.K_d]:
            self.direction.x = 1
            self.is_moving = True
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        movement = self.direction * self.speed * dt

        self.last_position = self.position - movement
        self.position += movement

        # set center position of player rect to the location of the position vector
        self.rect.center = round(self.position)

    def update(self, dt):
        self.input()
        self.move(dt)


class Game:
    def __init__(self):
        self.previous_time = time.time()  # start initial instance of timer for calculating delta time
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
