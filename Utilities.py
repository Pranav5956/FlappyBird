# Import the required modules
from Objects import *
from typing import Union


# Redraws the PyGame window
def redraw_window(screen: pygame.Surface, background: pygame.Surface, *objects: Union[Base, Bird, Pipe]) -> None:
    """
    Redraw the window during every frame
    :param screen: SurfaceType
    :param background: SurfaceType
    :param objects: Union[Base, Bird, Pipe]
    :return: None
    """
    pygame.display.update()

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw all the objects
    for obj in objects:
        obj.draw(screen)
