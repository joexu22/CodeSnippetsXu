import sys
import pygame


def check_keydown_events(event, chracter):
    """Respond to keypresses."""
    # moving the chracter with keypresses
    if event.key == pygame.K_UP:
        chracter.moving_up = True
    if event.key == pygame.K_DOWN:
        chracter.moving_down = True
    if event.key == pygame.K_LEFT:
        chracter.moving_left = True
    if event.key == pygame.K_RIGHT:
        chracter.moving_right = True


def check_keyup_events(event, chracter):
    """Respond to key releases."""
    # stoping the chracter on key release
    if event.key == pygame.K_UP:
        chracter.moving_up = False
    if event.key == pygame.K_DOWN:
        chracter.moving_down = False
    if event.key == pygame.K_LEFT:
        chracter.moving_left = False
    if event.key == pygame.K_RIGHT:
        chracter.moving_right = False


def check_events(chracter):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # checking for quit command
        if event.type == pygame.QUIT:
            sys.exit()

        # checking for key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, chracter)
        # checking for key releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, chracter)


def update_screen(ai_settings, screen, chracter):
    """Update the screen and flip to new image"""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    chracter.blitme()

    # Make the most recent drawn screen visible
    pygame.display.flip()
