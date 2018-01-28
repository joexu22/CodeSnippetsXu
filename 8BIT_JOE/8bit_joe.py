# Quick 8Bit Character Movement
import pygame

from settings import Settings
from character import CharacterJoe

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("8-Bit Joe")
    
    # Creating My Character "Joe"
    character = CharacterJoe(ai_settings, screen)
    
    # Start the Main Loop for the Game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(character)
        character.update()
        gf.update_screen(ai_settings, screen, character)

run_game()