# Import the required modules
from Enums import *
from LoadImages import *
from random import randrange


# Bird Object
class Bird:
    pass


# Scrolling base object
class Base:
    Width, Height = BASE_SPRITE.get_size()

    def __init__(self, y: int):
        """
        Create a scrolling background base object using 2 images, moving side-by-side
        :param y: int
        """
        self.y = y
        self.first_x = 0
        self.second_x = Base.Width

    def move(self, vel: float) -> None:
        """
        Move the 2 images and update the position once it has moved out of the screen
        :param vel: float
        :return: None
        """
        self.first_x -= vel
        self.second_x -= vel

        if self.first_x <= -Base.Width:
            self.first_x = Base.Width
        if self.second_x <= -Base.Width:
            self.second_x = Base.Width

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the object
        :param screen: SurfaceType
        :return: None
        """
        screen.blit(BASE_SPRITE, (int(self.first_x), self.y))
        screen.blit(BASE_SPRITE, (int(self.second_x), self.y))


# Scrolling Pipes object
class Pipe:
    Width = PIPE_SPRITES[PipesEnum.Top].get_width()
    TopPipeHeight = PIPE_SPRITES[PipesEnum.Top].get_height()
    BottomPipeHeight = PIPE_SPRITES[PipesEnum.Bottom].get_height()
    Offset = 57

    def __init__(self, x):
        """
        Initialize the Pipe object
        :param x: int
        """
        self.x = x
        self.y = randrange(
            BACKGROUND_SPRITE.get_height() - Base.Height - Pipe.BottomPipeHeight - Pipe.Offset,
            Pipe.TopPipeHeight + Pipe.Offset - 22   # 22px accounts for the brim of the bottom pipe
        )
        self.can_spawn_next = True

    def move(self, vel: float) -> None:
        """
        Move the Pipe by a specified value
        :param vel: float
        :return: None
        """
        self.x -= vel

    def get_mask(self):
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the Pipes in pairs of two (Top and Bottom)
        :param screen: SurfaceType
        :return: None
        """
        screen.blit(PIPE_SPRITES[PipesEnum.Bottom], (int(self.x), self.y + Pipe.Offset))
        screen.blit(PIPE_SPRITES[PipesEnum.Top], (int(self.x), self.y - Pipe.TopPipeHeight - Pipe.Offset))
