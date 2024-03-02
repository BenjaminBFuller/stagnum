import pygame as pg
from pygame.locals import *

pg.init()

# Set up the screen dimensions
width, height = 500, 500
pg.mouse.set_visible(False)
flags = DOUBLEBUF | SCALED | FULLSCREEN  # fullscreen, double buffering, scaled resolution
screen = pg.display.set_mode((width, height), flags)
pg.display.set_caption("STAGNUM")
FPS = 60

# Set tile size at VALUE x VALUE
tile = 50

# Define colors (RGB)
WHITE = (255, 255, 255)

menu_bg = pg.image.load("images/watermenu.png").convert()
menu_bg = pg.transform.scale(menu_bg, (tile * 10, tile * 10))

tadpole_image = pg.image.load("images/tadpole.png").convert_alpha()
tadpole_image = pg.transform.scale(tadpole_image, (tile, tile))
