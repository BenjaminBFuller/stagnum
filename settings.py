import pygame as pg

pg.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Tadpole Game")

# Define colors (RGB)
WHITE = (255, 255, 255)