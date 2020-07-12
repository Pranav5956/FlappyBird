# Import the required modules
import pygame

# Importing all the sprites
# Bird
BIRD_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame1.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame2.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Bird/frame3.png'))
]

# Pipes
PIPE_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Pipes/PipeDown.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Pipes/PipeUp.png')),
]

# Coins
COIN_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Coins/BlankCoin.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Coins/BronzeCoin.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Coins/SilverCoin.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Coins/GoldCoin.png'))
]

# Cards
CARD_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/FlappyBirdTitleCard.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/GetReadyCard.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/Tutorial.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/New.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/ScoreCard.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/GameOverCard.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Cards/Credits.png'))
]

# Buttons
BUTTON_SPRITES = [
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/MenuButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/OKButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/PauseButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/PlayButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/RateButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/ScoreButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/ShareButton.png')),
    pygame.transform.scale2x(pygame.image.load('Sprites/Buttons/StartButton.png'))
]

# Backgrounds
BASE_SPRITE = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Base.png'))
BACKGROUND_SPRITE = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Background.png'))

# Fonts
WIN_WIDTH, WIN_HEIGHT = BACKGROUND_SPRITE.get_size()
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FONT_BIG_SPRITE_SHEET = pygame.transform.scale2x(pygame.image.load('Fonts/FontBig.png'))
FONT_SMALL_SPRITE_SHEET = pygame.transform.scale2x(pygame.image.load('Fonts/FontSmall.png'))
FONT_BIG_RECT = [pygame.Rect(14 * i, 0, 14, 20) for i in range(10)]
FONT_SMALL_RECT = [pygame.Rect(12 * i, 0, 12, 14) for i in range(10)]

# Icon
ICON = pygame.image.load('Sprites/FlappyBirdIcon.ico')

# Theme and Sounds
pygame.mixer.init()
SOUNDS = [
    pygame.mixer.Sound('Sounds/sfx_die.wav'),
    pygame.mixer.Sound('Sounds/sfx_hit.wav'),
    pygame.mixer.Sound('Sounds/sfx_point.wav'),
    pygame.mixer.Sound('Sounds/sfx_wing.wav')
]
