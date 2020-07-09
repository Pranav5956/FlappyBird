# Import the required module
from Objects import *
from Utilities import *

# PyGame window macros
WIN_WIDTH = 288
WIN_HEIGHT = 512
FPS = 30
CLOCK = pygame.time.Clock()
running = True

# PyGame initialization
pygame.init()
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Initialize the objects
base = Base(400)

while running:
    # Set the FPS for the game
    CLOCK.tick(FPS)

    # Listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the base
    base.move(2)

    # Redraw the window
    redraw_window(screen, BACKGROUND_SPRITE, base)
pygame.quit()
