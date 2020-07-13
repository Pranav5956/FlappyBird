# Import the required modules
from Objects import *


def start_game() -> Tuple[Base, List, Bird, int]:
    """
    Returns the initial states of the game (can also be called during restart)
    :return: Tuple[ Base, List, Bird, int]
    """
    return Base(WIN_HEIGHT - Base.Height), [], Bird(), 0


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

    # Draw the base
    base.draw(screen)

    # Draw the bird
    bird.draw(screen)
    bird.move()


def draw_text(screen: pygame.Surface, value: str, pos: Tuple[int, int], big: bool = True, align: str = 'center') -> int:
    """
    Gets a number and prints sprites
    :param screen: SurfaceType
    :param value: str
    :param big: bool = True
    :param pos: Tuple[ int, int ]
    :param align: str
    :return: int
    """
    if big:
        font = FONT_BIG_SPRITE_SHEET
        font_rect = FONT_BIG_RECT
    else:
        font = FONT_SMALL_SPRITE_SHEET
        font_rect = FONT_SMALL_RECT

    width, height = font_rect[0].size
    if align == 'right':
        for i, digit in enumerate(value):
            screen.blit(font, (pos[0] - (width * len(value)) + i * width, pos[1] - height // 2), font_rect[int(digit)])
    else:
        for i, digit in enumerate(value):
            screen.blit(font, (pos[0] - (width * len(value)) // 2 + i * width, pos[1] - height // 2), font_rect[int(digit)])

    return width * len(value)


def draw_card(screen: pygame.Surface, card: int, pos: Tuple[int, int]):
    """
    Draws a card at a position
    :param screen: SurfaceType
    :param card: int
    :param pos: Tuple[int, int]
    :return:
    """
    sprite = CARD_SPRITES[card]
    screen.blit(sprite, (pos[0] - sprite.get_width() // 2, pos[1] - sprite.get_height() // 2))
