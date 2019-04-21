import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    """A class to manage fireballs fired from character"""

    def __init__(self, ai_settings, screen, character):
        """Create a fireball object at the character's current position."""
        super().__init__()
        self.screen = screen

        # Create a fireball rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.fireball_width, ai_settings.fireball_height
        )
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top

        # Store the fireball's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = ai_settings.fireball_color
        self.speed_factor = ai_settings.fireball_speed_factor

    def update(self, character):
        """Move the fireball across the screen."""
        # Update the decimal position of the fireball, depending on the direction of the character
        
        """
        #! TODO: need to fix this later
        if character.moving_right:
            self.x += self.speed_factor
        if character.moving_left:
            self.x -= self.speed_factor
        """

        self.y -= self.speed_factor
        
        # Update the rect position.
        self.rect.y = self.y

    def draw_fireball(self):
        """Draw the fireball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
