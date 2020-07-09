# Import the required modules
import pygame


# Redraws the PyGame window
def redraw_window(screen: pygame.Surface, background: pygame.Surface, *objects) -> None:
    """
    Redraw the window during every frame
    :param screen: pygame.Surface
    :param background: pygame.surface
    :param objects: List[Any]
    :return: None
    """
    pygame.display.update()

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw all the objects
    for obj in objects:
        obj.draw(screen)
