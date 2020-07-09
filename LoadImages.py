# Import the required modules
import pygame

# Importing all the sprites
BIRD_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame1.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame2.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame3.png'))
]

PIPE_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Pipes/PipeDown.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Pipes/PipeUp.png')),
]

BASE_SPRITE = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Base.png'))
BACKGROUND_SPRITE = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Background.png'))

FONT_BIG = pygame.transform.scale2x(pygame.image.load('Sprites/Fonts/FontBig.png'))
FONT_SMALL = pygame.transform.scale2x(pygame.image.load('Sprites/Fonts/FontSmall.png'))

ICON = pygame.image.load('Sprites/FlappyBirdIcon.ico')
