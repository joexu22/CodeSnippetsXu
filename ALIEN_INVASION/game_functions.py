import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
	"""Update the screen and flip to new image"""
	# Redraw the screen
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	# Make the most recent drawn screen visible
	pygame.display.flip()
