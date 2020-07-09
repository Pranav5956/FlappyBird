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
FONT_BIG = pygame.transform.scale2x(pygame.image.load('Sprites/Fonts/FontBig.png'))
FONT_SMALL = pygame.transform.scale2x(pygame.image.load('Sprites/Fonts/FontSmall.png'))

# Icon
ICON = pygame.image.load('Sprites/FlappyBirdIcon.ico')
