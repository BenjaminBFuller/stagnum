# Flying Squirrel presents Stagnum

from settings import *
from pygame.math import Vector2
from pygame.sprite import Group
import time
import sys


class Tadpole(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.direction = Vector2()
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 300

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

        # Calculate the tadpole's position
        new_x = self.rect.x + round(movement.x)
        new_y = self.rect.y + round(movement.y)

        # Updates new tadpole position if inside the game window
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y


class Game:
    def __init__(self):
        self.previous_time = time.time()  # create clock for calculating delta time
        self.tadpole = Tadpole()

    def main(self):
        all_sprites = Group(self.tadpole)

        while True:
            # unused delta time to account for varying framerates
            dt = time.time() - self.previous_time  # delta time
            self.previous_time = time.time()
            all_sprites.update(dt)
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            pg.display.flip()


if __name__ == "__main__":
    game = Game()
    game.main()
