import pygame

pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_icon(pygame.image.load('Sprites/FlappyBirdIcon.ico'))
pygame.display.set_caption("Flappy Bird")

bg = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Background.png'))
base = pygame.transform.scale2x(pygame.image.load('Sprites/Backgrounds/Base.png'))

running = True

clock = pygame.time.Clock()
base_x1, base_x2 = 0, base.get_width()

while running:
    clock.tick(30)

    # Draw the background
    screen.blit(bg, (0, 0))

    # Draw the scrolling base
    base_x1 -= 2
    base_x2 -= 2
    if base_x1 <= -base.get_width():
        base_x1 = base.get_width()
    if base_x2 <= -base.get_width():
        base_x2 = base.get_width()

    screen.blit(base, (base_x1, 512-base.get_height()))
    screen.blit(base, (base_x2, 512 - base.get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
