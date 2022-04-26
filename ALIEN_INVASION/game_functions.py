import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    # moving the ship with keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update the screen and flip to new image"""
    # Redraw all bullets behind ship and aliens
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.draw(screen)

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


def get_number_aliens_x(ai_settings, screen):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
 
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
 
    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
