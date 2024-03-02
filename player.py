from settings import *
from pygame.math import Vector2
import sys


class Player(pg.sprite.Sprite):
    """
    Main Player controllable character class
    """
    def __init__(self, rect_center):
        pg.sprite.Sprite.__init__(self)
        self.image = tadpole_image
        self.rect = self.image.get_rect()
        self.rect.center = rect_center
        self.direction = Vector2()
        self.position = Vector2(self.rect.center)
        self.is_moving = False
        self.speed = 3

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

        if keys[pg.K_w] and self.position.y-(tile/2) > 150:
            self.direction.y = -1
            self.is_moving = True
        elif keys[pg.K_s] and self.position.y+(tile/2) < 350:
            self.direction.y = 1
            self.is_moving = True
        else:
            self.direction.y = 0

        if keys[pg.K_a] and self.position.x-(tile/2) > 0:
            self.direction.x = -1
            self.is_moving = True
        elif keys[pg.K_d] and self.position.x+(tile/2) < width:
            self.direction.x = 1
            self.is_moving = True
        else:
            self.direction.x = 0

    def move(self):
        # Normalize diagonal movement velocity
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        movement = self.direction * self.speed

        self.position += movement

        # set center position of player rect to the location of the position vector
        self.rect.center = round(self.position)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.input()
        self.move()
        self.draw()
