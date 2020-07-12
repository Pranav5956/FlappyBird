# Import the required module
from Utilities import *

# PyGame window macros
FPS = 30
CLOCK = pygame.time.Clock()
SCROLL_VEL = 2.75
running = True  # Mainloop Handler

# PyGame initialization
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")

# Initialize the objects
base = Base(WIN_HEIGHT - Base.Height)
pipes = [Pipe(2 * WIN_WIDTH)]   # Initial delay is large
bird = Bird()
score = 0
crashed = False

# MainLoop
while running:
    # FPS handler
    CLOCK.tick(FPS)

    # Event handler
    for event in pygame.event.get():
        # Quit action
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not crashed:
            # Make a flap if the user clicks the mouse
            bird.flap()

            # Play the flapping sound
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Wing])

    # Base handler
    base.move(SCROLL_VEL)

    # Pipes handler
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

        # Add the score if the player passes through the pipe
        if not pipe.passed and bird.x > pipe.x:
            # Add the point
            pipe.passed = True
            score += 1

            # Play the point sound
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Point])

        if bird.check_for_collision(pipe) and not crashed:
            # Stop all motion
            crashed = True
            SCROLL_VEL = 0

            # Play the Hit sound
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Hit])
    # Remove the crossed pipes
    if crossed_pipe is not None:
        pipes.remove(crossed_pipe)

    # Animation handler
    redraw_window(screen, BACKGROUND_SPRITE, base, pipes, bird)

    # Score Handler
    draw_text(screen, str(score), (WIN_WIDTH // 2, WIN_HEIGHT // 8))

# Close the window on exit
pygame.quit()
