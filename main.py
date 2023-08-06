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
        self.speed = 1

    def update(self):
        # Get the keys pressed
        keys = pg.key.get_pressed()
        # Update the position based on the keys pressed
        if keys[pg.K_q]:
            pg.quit()
            sys.exit()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed


def main():
    # Create the tadpole object
    tadpole = Tadpole()
    all_sprites = pg.sprite.Group(tadpole)

    # Game loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Update tadpole position
        all_sprites.update()

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen
        all_sprites.draw(screen)  # Draw the tadpole
        pg.display.flip()  # Update the display


if __name__ == "__main__":
    main()
