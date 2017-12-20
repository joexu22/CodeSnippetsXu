# working through a python3 game
# alien invasion
import sys
import pygame

from settings import Settings

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		# Redraw the screen
		screen.fill(ai_settings.bg_color)
		
		# make the most recent drawn screen visible
		pygame.display.flip()

run_game()
