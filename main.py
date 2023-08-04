import pygame as pg
import sys

pg.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Tadpole Game")

# Define colors (RGB)
WHITE = (255, 255, 255)


class Tadpole(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the tadpole image
        self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5

    def update(self):
        # Get the keys pressed
        keys = pg.key.get_pressed()
        # Update the position based on the keys pressed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
