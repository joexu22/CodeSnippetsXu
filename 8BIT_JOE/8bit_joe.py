# Quick 8Bit Character Movement
import pygame
from pygame.sprite import Group

from settings import Settings
from character import CharacterJoe

import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("8-Bit Joe")

    # Creating my character "Joe"
    character = CharacterJoe(ai_settings, screen)

    # Creating group of Fireballs
    fireballs = Group()

    # Creating a swarm of Monsters
    monsters = Group()
    gf.create_swarm(ai_settings, screen, character, monsters)

    # Start the Main Loop for the Game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, character, fireballs)
        character.update()
        gf.update_fireballs(ai_settings, screen, character, fireballs)
        gf.update_screen(ai_settings, screen, character, monsters, fireballs)

        # Getting rid of fireballs that have disappeared
        for fireball in fireballs.copy():
            if fireball.rect.bottom <= 0:
                fireballs.remove(fireball)
        print(len(fireballs))

run_game()
