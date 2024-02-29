import pygame as pg

pg.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 800
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("STAGNUM")

FPS = 60

# Set tile size at VALUE x VALUE
tile = 50

# Define colors (RGB)
WHITE = (255, 255, 255)

tadpole_image = pg.image.load("images/tadpole1.png").convert_alpha()
tadpole_image = pg.transform.scale(tadpole_image, (tile, tile))