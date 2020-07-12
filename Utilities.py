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


def draw_text(screen: pygame.Surface, value: str, pos: Tuple[int, int], big: bool = True) -> None:
    """
    Gets a number and prints sprites
    :param screen: SurfaceType
    :param value: str
    :param big: bool = True
    :param pos: Tuple[ int, int ]
    :return: None
    """
    if big:
        font = FONT_BIG_SPRITE_SHEET
        font_rect = FONT_BIG_RECT
    else:
        font = FONT_SMALL_SPRITE_SHEET
        font_rect = FONT_SMALL_RECT

    width, height = font_rect[0].size
    for i, digit in enumerate(value):
        screen.blit(font, (pos[0] - (width * len(value)) // 2 + i * width, pos[1] - height // 2), font_rect[int(digit)])
