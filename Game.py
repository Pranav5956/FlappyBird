# Import the required module
from Utilities import *

# PyGame window macros
WIN_WIDTH, WIN_HEIGHT = BACKGROUND_SPRITE.get_size()
FPS = 30
CLOCK = pygame.time.Clock()
SCROLL_VEL = 2
running = True  # Mainloop Handler

# PyGame initialization
pygame.init()
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Initialize the objects
base = Base(WIN_HEIGHT - Base.Height)
pipes = [Pipe(2 * WIN_WIDTH)]   # Initial delay is large

# MainLoop
while running:
    # FPS handler
    CLOCK.tick(FPS)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Base handler
    base.move(SCROLL_VEL)

    # Pipes handler
    # Since there is a maximum of only one pipe moving off-screen, it needn't be a list
    crossed_pipe = None
    for pipe in pipes:
        # Remove the pipe if the current pipe has crossed the left border of the screen
        if pipe.x < -Pipe.Width:
            crossed_pipe = pipe
            continue

        # Create a new pipe from the right corner if the current pipe has crossed
        # half the screen
        if pipe.x < WIN_WIDTH // 2 and pipe.can_spawn_next:
            pipes.append(Pipe(WIN_WIDTH + Pipe.Width // 3))
            pipe.can_spawn_next = False

        # Move the pipe
        pipe.move(SCROLL_VEL)
    # Remove the crossed pipes
    if crossed_pipe is not None:
        pipes.remove(crossed_pipe)

    # Animation handler
    redraw_window(screen, BACKGROUND_SPRITE, base, pipes)

# Close the window on exit
pygame.quit()
