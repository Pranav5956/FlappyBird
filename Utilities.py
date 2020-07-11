# Import the required modules
from Objects import *
from typing import List


# Redraws the PyGame window
def redraw_window(screen: pygame.Surface, background: pygame.Surface, base: Base, pipes: List[Pipe], bird: Bird) -> None:
    """
    Redraw the window during every frame
    :param screen: SurfaceType
    :param background: SurfaceType
    :param base: objects.Base
    :param pipes: List[ objects.Pipe ]
    :param bird: Bird
    :return: None
    """
    pygame.display.update()

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the pipes
    for pipe in pipes:
        pipe.draw(screen)

    # Draw the bird
    bird.draw(screen)
    bird.move()

    # Draw the base
    base.draw(screen)
