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
        self.direction = Vector2()
        self.position = [1, 1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0] * 50, self.position[1] * 50)
        self.speed = 250

    def update(self, dt):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        keys = pg.key.get_pressed()

        if keys[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        if keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # Normalize the vector to ensure constant speed
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        movement = self.direction * self.speed * dt

        # Calculate the player's position
        new_x = self.rect.x + round(movement.x)
        new_y = self.rect.y + round(movement.y)

        # Updates new player position if inside the game window
        # Collision handling
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y


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
