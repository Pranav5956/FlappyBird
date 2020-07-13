# Import the required module
from Utilities import *

# PyGame window macros
FPS = 30
CLOCK = pygame.time.Clock()
SCROLL_VEL = 2.75
BUFFER_TIME = 2
timer = BUFFER_TIME
running = True  # Mainloop Handler

# PyGame display setup
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")

# Initialize the objects
base, pipes, bird, score = start_game()
start_button_rect = pygame.Rect((WIN_WIDTH // 2 - BUTTON_SPRITES[ButtonsEnum.StartButton].get_width() // 2,
                                2 * WIN_HEIGHT // 3 - BUTTON_SPRITES[ButtonsEnum.StartButton].get_height() // 2),
                                BUTTON_SPRITES[ButtonsEnum.StartButton].get_size())
ok_button_rect = pygame.Rect((WIN_WIDTH // 2 - BUTTON_SPRITES[ButtonsEnum.OKButton].get_width() // 2,
                             2 * WIN_HEIGHT // 3 - BUTTON_SPRITES[ButtonsEnum.OKButton].get_height() // 2),
                             BUTTON_SPRITES[ButtonsEnum.OKButton].get_size())
state = StatesEnum.Intro

try:
    with open('highscore.txt') as f:
        high_score = int(f.read())
    f.close()
except FileNotFoundError or ValueError:
    high_score = 0
prev_high_score = high_score

# MainLoop
while running:
    # FPS handler
    CLOCK.tick(FPS)

    # Event handler
    for event in pygame.event.get():
        # Quit action
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state is StatesEnum.Intro:
                if start_button_rect.collidepoint(*event.pos):
                    state = StatesEnum.GetReady

            elif state is StatesEnum.GetReady:
                state = StatesEnum.Play
                pipes.append(Pipe(2 * WIN_WIDTH))

                # Make a flap if the user clicks the mouse
                bird.is_active = True
                bird.flap()

                # Play the flapping sound
                pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Wing])

                # Reset the timer
                timer = BUFFER_TIME

            elif state is StatesEnum.Play:
                # Make a flap if the user clicks the mouse
                bird.flap()

                # Play the flapping sound
                pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Wing])

            elif state is StatesEnum.Score:
                if ok_button_rect.collidepoint(*event.pos):
                    base, pipes, bird, score = start_game()
                    SCROLL_VEL = 2.75
                    state = StatesEnum.Intro
                    timer = BUFFER_TIME
                    prev_high_score = high_score

    # Base handler
    base.move(SCROLL_VEL)

    # Pipes handler
    crossed_pipe = None
    for pipe in pipes:
        # Remove the pipe if the current pipe has crossed the left border of the screen
        if pipe.x < -Pipe.Width:
            crossed_pipe = pipe
            continue

        # Create a new pipe from the right corner if the current pipe has crossed
        # half the screen
        if pipe.x < WIN_WIDTH // 2 and pipe.can_spawn_next:
            pipes.append(Pipe(WIN_WIDTH + Pipe.Width // 3))
            pipe.can_spawn_next = False

        # Move the pipe
        pipe.move(SCROLL_VEL)

        # Add the score if the player passes through the pipe
        if not pipe.passed and bird.x > pipe.x:
            # Add the point
            pipe.passed = True
            score += 1

            # Play the point sound
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Point])

        if (bird.check_for_collision(pipe, base)) and state is StatesEnum.Play:
            # Stop all motion
            state = StatesEnum.Crashed
            SCROLL_VEL = 0

            # Play the Hit sound
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Hit])
    # Remove the crossed pipes
    if crossed_pipe is not None:
        pipes.remove(crossed_pipe)

    # Animation handler
    redraw_window(screen, BACKGROUND_SPRITE, base, pipes, bird)

    # Display Handler
    if state is StatesEnum.Intro:
        draw_card(screen, CardsEnum.TitleCard, (WIN_WIDTH // 2, WIN_HEIGHT // 6))
        draw_card(screen, CardsEnum.CreditsCard, (WIN_WIDTH // 2, 31 * WIN_HEIGHT // 32))
        screen.blit(BUTTON_SPRITES[ButtonsEnum.StartButton], (start_button_rect.x, start_button_rect.y))
    elif state is StatesEnum.GetReady:
        draw_card(screen, CardsEnum.GetReadyCard, (WIN_WIDTH // 2, WIN_HEIGHT // 6))

        # Pop-up tutorial card
        timer -= 1 / FPS

        if timer <= BUFFER_TIME // 2:
            draw_card(screen, CardsEnum.TutorialCard, (2 * WIN_WIDTH // 3, 2 * WIN_HEIGHT // 5))
        if timer <= 0:
            timer = BUFFER_TIME
    elif state is StatesEnum.Play:
        draw_text(screen, str(score), (WIN_WIDTH // 2, WIN_HEIGHT // 8))
    elif state is StatesEnum.Crashed:
        draw_card(screen, CardsEnum.GameOverCard, (WIN_WIDTH // 2, WIN_HEIGHT // 6))

        timer -= 1 / FPS
        if timer <= 0:
            state = StatesEnum.Score
            pygame.mixer.Sound.play(SOUNDS[SoundsEnum.Die])
    elif state is StatesEnum.Score:
        draw_card(screen, CardsEnum.GameOverCard, (WIN_WIDTH // 2, WIN_HEIGHT // 6))
        draw_card(screen, CardsEnum.ScoreCard, (WIN_WIDTH // 2, (WIN_HEIGHT - Base.Height) // 2))
        screen.blit(BUTTON_SPRITES[ButtonsEnum.OKButton], (ok_button_rect.x, ok_button_rect.y))

        # Scores
        draw_text(screen, str(score), (WIN_WIDTH // 2 + 92, (WIN_HEIGHT - Base.Height) // 2 - 14), False, 'right')
        if score > high_score:
            high_score = score
            with open('highscore.txt', 'w') as f:
                f.write(str(high_score))
            f.close()
        width = draw_text(screen, str(high_score), (WIN_WIDTH // 2 + 92, (WIN_HEIGHT - Base.Height) // 2 + 26), False, 'right')
        if score > prev_high_score:
            draw_card(screen, CardsEnum.NewCard, (WIN_WIDTH // 2 + 92 - width - 24, (WIN_HEIGHT - Base.Height) // 2 + 26))

        # Coin
        if score >= 40:
            coin = COIN_SPRITES[CoinsEnum.Platinum]
        elif score >= 30:
            coin = COIN_SPRITES[CoinsEnum.Gold]
        elif score >= 20:
            coin = COIN_SPRITES[CoinsEnum.Silver]
        elif score >= 10:
            coin = COIN_SPRITES[CoinsEnum.Bronze]
        else:
            coin = None

        if coin:
            screen.blit(coin, (WIN_WIDTH // 2 - 88, (WIN_HEIGHT - Base.Height) // 2 - 16))

# Close the window on exit
pygame.quit()
