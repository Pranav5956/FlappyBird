# Import the required modules
from LoadImages import *


# Bird Object
class Bird:
    pass


# Scrolling base object
class Base:
    def __init__(self, y: int):
        """
        Create a scrolling background base object using 2 images, moving side-by-side
        :param y: int
        """
        self.y = y
        self.width = BASE_SPRITE.get_width()
        self.first_x = 0
        self.second_x = self.width

    def move(self, vel: float) -> None:
        """
        Move the 2 images and update the position once it has moved out of the screen
        :param vel: float
        :return: None
        """
        self.first_x -= vel
        self.second_x -= vel

        if self.first_x <= -self.width:
            self.first_x = self.width
        if self.second_x <= -self.width:
            self.second_x = self.width

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the object
        :param screen: SurfaceType
        :return: None
        """
        screen.blit(BASE_SPRITE, (int(self.first_x), self.y))
        screen.blit(BASE_SPRITE, (int(self.second_x), self.y))


# Moving Pipes object
class Pipe:
    pass
