import sys
import pygame
from fireball import Fireball
from monster import Monster


def check_keydown_events(event, ai_settings, screen, character, fireballs):
    """Respond to keypresses."""
    # moving the character with keypresses
    if event.key == pygame.K_UP:
        character.moving_up = True
    if event.key == pygame.K_DOWN:
        character.moving_down = True
    if event.key == pygame.K_LEFT:
        character.moving_left = True
    if event.key == pygame.K_RIGHT:
        character.moving_right = True

    # casts a fireball
    if event.key == pygame.K_SPACE:
        cast_fireball(ai_settings, screen, character, fireballs)

    # quit game
    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ai_settings, screen, character, fireballs):
    """Respond to key releases."""
    # stoping the character on key release
    if event.key == pygame.K_UP:
        character.moving_up = False
    if event.key == pygame.K_DOWN:
        character.moving_down = False
    if event.key == pygame.K_LEFT:
        character.moving_left = False
    if event.key == pygame.K_RIGHT:
        character.moving_right = False


def cast_fireball(ai_settings, screen, character, fireballs):
    """Casts a fireball based on limit"""
    if len(fireballs) < ai_settings.fireballs_allowed:
        new_fireball = Fireball(ai_settings, screen, character)
        fireballs.add(new_fireball)


def check_events(ai_settings, screen, character, fireballs):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        # checking for quit command
        if event.type == pygame.QUIT:
            sys.exit()

        # checking for key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,
                                 screen, character, fireballs)

        # checking for key releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen,
                               character, fireballs)


def update_screen(ai_settings, screen, character, monsters, fireballs):
    """Update the screen and flip to new image"""
    # Redraw the screen
    screen.fill(ai_settings.bg_color)

    # Draws the swarm of monsters
    monsters.draw(screen)
    
    # Draws the character
    character.blitme()

    # Draws fireballs onto the screen
    for fireball in fireballs.sprites():
        fireball.draw_fireball()

    # Make the most recent drawn screen visible
    pygame.display.flip()


def get_number_of_monsters_x(ai_settings, monster_width):
    """Determins the amount of monsters that fit across the screen"""
    screen_space_x = ai_settings.screen_width - 2 * monster_width
    number_of_monsters_x = int(screen_space_x / (2 * monster_width))
    return number_of_monsters_x


def get_number_of_rows(ai_settings, character_height, monster_height):
    """Determins the number of rows of monsters that can fit onto the screen"""
    screen_space_y = ai_settings.screen_height - (3 * monster_height) - character_height
    number_of_rows = int(screen_space_y / (2 * monster_height))
    return number_of_rows


def create_monster(ai_settings, screen, monsters, monster_count, row_number):
    """Creates an monster"""
    monster = Monster(ai_settings, screen)
    monster_width = monster.rect.width
    monster_height = monster.rect.height
    # Calculates where the (X,Y) coordinates of the monster is
    monster_x = monster_width + 2 * monster_width * monster_count
    monster_y = monster_height + 2 * monster_height * row_number
    # Places the monster at (X,Y) coordinate
    monster.rect.x = monster_x
    monster.rect.y = monster_y
    monsters.add(monster)


def create_swarm(ai_settings, screen, character, monsters):
    """Create a swarm of monsters."""
    # Create an monster and find the number of monsters in a row
    # Space out the monsters
    monster = Monster(ai_settings, screen)
    number_of_monsters_x = get_number_of_monsters_x(ai_settings, monster.rect.width)
    row_number = get_number_of_rows(ai_settings, character.rect.height, monster.rect.height)
    # Create a row of monsters.
    for row in range(row_number):
        for monster_count in range(number_of_monsters_x):
            create_monster(ai_settings, screen, monsters, monster_count, row)


def update_fireballs(ai_settings, screen, character, fireballs):
    """Update position of fireballs and get rid of old fireballs."""
    # Update fireball positions.
    fireballs.update(character)

    # Get rid of bullets that have disappeared of the screen
    for fireball in fireballs.copy():
        # When fireball moves off the right edge
        if fireball.rect.left >= ai_settings.screen_width:
            fireballs.remove(fireball)

        # When fireball moves off the left edge
        if fireball.rect.right <= 0:
            fireballs.remove(fireball)
