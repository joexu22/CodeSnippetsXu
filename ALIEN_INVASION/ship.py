import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initializing the ship and setting its starting position."""

        # allows us to manipulate the screen
        self.screen = screen
        self.ai_settings = ai_settings

        # load image and its "rectangle coordinates"
        self.image = pygame.image.load("images/ship.bmp")

        # creats a rectangle representation using the demensions of image
        self.rect = self.image.get_rect()

        # get the rectuangle representation of the screen
        self.screen_rect = screen.get_rect()

        # aligns the center the ship at bottom-center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # stores a decimal value for the ship's cnter.
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's positiion based on the movement flag."""
        # Updating the ship's center value, not the rect value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updating rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
