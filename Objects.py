# Import the required modules
from Enums import *
from LoadAssets import *
from typing import Tuple
from random import randrange
import numpy as np


# Bird Object
class Bird:
    Width, Height = BIRD_SPRITES[1].get_size()

    def __init__(self):
        """
        Initialize the bird
        """
        self.y = (BACKGROUND_SPRITE.get_height() - Base.Height) // 2
        self.x = BACKGROUND_SPRITE.get_width() // 3

        # Physics controllers
        self.delta_time = 0.25  # For faster gravity action
        self.gravity = -9.8
        self.velocity = 0
        self.max_velocity = 35
        self.terminal_velocity = -10

        # Animation controllers
        self.up_angle = 30
        self.down_angle = -90
        self.angle = 0
        self.sprite_index = 0
        self.animation_wait_time = 4
        self.animation_time = self.animation_wait_time
        self.sprite = BIRD_SPRITES[self.sprite_index]

    def flap(self) -> None:
        """
        Provide a boost flap for the bird
        Achieved by a time-skip of a quarter of a second
        :return: None
        """
        self.delta_time = 0.25
        self.velocity = 35

    def move(self) -> None:
        """
        Apply physics on the bird
        :return: None
        """
        self.delta_time += 1 / 30  # FPS is 30 frames per second
        self.y -= self.velocity * self.delta_time + 0.5 * self.gravity * (self.delta_time ** 2)  # s = ut + 0.5at^2
        self.velocity = self.velocity + self.gravity * self.delta_time  # v = u + at

        # Limit the velocity to the terminal velocity
        self.velocity = max(self.terminal_velocity, self.velocity)

        # Limit the y-pos to within the top of the screen and the base
        self.y = min(max(0, self.y), BACKGROUND_SPRITE.get_height() - Base.Height - Bird.Height)

        # Animation
        # -e^-x graph is found suitable for the slow descent
        # The value of the function converges to -90 as x peaks out at 4.5
        # The value of the function converges to 0 as x becomes negative
        self.angle = -np.exp(self.velocity / self.terminal_velocity * 4.5) + (self.velocity > 0) * self.up_angle

    def _rotate_image(self) -> Tuple[pygame.Surface, pygame.Rect]:
        """
        Rotates the sprite
        :return: Tuple[ SurfaceType, RectType ]
        """
        sprite_rect = pygame.Rect(self.x, self.y, Bird.Width, Bird.Height)
        rotated_sprite = pygame.transform.rotate(self.sprite, self.angle)
        rotated_rect = rotated_sprite.get_rect(center=sprite_rect.center)
        return rotated_sprite, rotated_rect

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the bird at (x, y)
        :param screen: SurfaceType
        :return: None
        """
        sprite, rect = self._rotate_image()
        screen.blit(sprite, (rect.x, rect.y))

        # Animation controllers
        if self.animation_time == 0:
            self.sprite_index = (self.sprite_index + 1) % len(BIRD_SPRITES)
            self.sprite = BIRD_SPRITES[self.sprite_index]
            self.animation_time = self.animation_wait_time

        if self.velocity > self.terminal_velocity / 2:
            self.animation_time -= 1


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
            Pipe.TopPipeHeight + Pipe.Offset - 22  # 22px accounts for the brim of the bottom pipe
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
