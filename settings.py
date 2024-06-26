# settings.py
# setters; images; pygame window setup

import pygame as pg
from pygame.locals import *

# initialize pygame for use in accompanying modules
pg.init()

# Set up the screen dimensions
width, height = 500, 500

# sets flags: double buffering, scaled resolution, fullscreen, hardware accelaration (GPU rendering)
flags = DOUBLEBUF | SCALED | FULLSCREEN | HWSURFACE

# set up screen/window
screen = pg.display.set_mode((width, height), flags)
pg.display.set_caption("TADPOLARITY")

# cursor config
pg.mouse.set_visible(False)

# Set FPS for use in clock.tick()
FPS = 60

# Set tile size at VALUE x VALUE
tile = 50

# Define colors (RGB)
WHITE = (255, 255, 255)

# Set fonts
title_font = pg.font.Font("fonts/dpcomic.ttf", 80)

# Load images
menu_bg = pg.image.load("images/watermenu.png").convert()
menu_bg = pg.transform.scale(menu_bg, (tile * 10, tile * 10))

tadpole_image = pg.image.load("images/tadpole.png").convert_alpha()
tadpole_image = pg.transform.scale(tadpole_image, (tile, tile))
