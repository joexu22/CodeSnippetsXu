import pygame

class Ship():
	
	def __init__(self, screen):	
		"""Initializing the ship and setting its starting position."""
		
		# allows us to manipulate the screen
		self.screen = screen
		
		# load image and its "rectangle coordinates"
		self.image = pygame.image.load('images/ship.bmp')
		
		# creats a rectangle representation using the demensions of image
		self.rect = self.image.get_rect()
		
		# get the rectuangle representation of the screen
		self.screen_rect = screen.get_rect()
		
		# aligns the center the ship at bottom-center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
