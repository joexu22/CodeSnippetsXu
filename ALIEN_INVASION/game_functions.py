import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    # moving the ship with keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    # stoping the ship on key release
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # checking for quit command
        if event.type == pygame.QUIT:
            sys.exit()
        
        # checking for key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        
        # checking for key releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 

def update_screen(ai_settings, screen, ship, bullets):
    """Update the screen and flip to new image"""
    # Redraw all bullets behind ship and aliens
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    
    # Make the most recent drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
