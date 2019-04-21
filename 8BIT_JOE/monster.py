import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class representing a monster"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the monster image and set its rect attribute
        self.image = pygame.image.load("assets/monsters/monster.png")
        self.rect = self.image.get_rect()

        # Start each new monster near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores the monster's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the monster at its current location."""
        self.screen.blit(self.image, self.rect)



