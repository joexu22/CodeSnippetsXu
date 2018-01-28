import sys
import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    # moving the ship with keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    # stoping the ship on key release
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # checking for quit command
        if event.type == pygame.QUIT:
            sys.exit()
        
        # checking for key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # checking for key releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Update the screen and flip to new image"""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recent drawn screen visible
    pygame.display.flip()
