import pygame


class CharacterJoe:
    def __init__(self, ai_settings, screen):
        """Initializing the ship and setting its starting position."""

        # allows us to manipulate the screen
        self.screen = screen
        self.ai_settings = ai_settings

        # load image and its "rectangle coordinates"
        # various configuration of the character
        self.image_back_left = pygame.image.load(
            "assets/character/8BitJoe_BackLeft.png")
        self.image_back_right = pygame.image.load(
            "assets/character/8BitJoe_BackRight.png")
        self.image_front_left = pygame.image.load(
            "assets/character/8BitJoe_FrontLeft.png")
        self.image_front_right = pygame.image.load(
            "assets/character/8BitJoe_FrontRight.png")

        # the main image being for the character
        # place your right foot forward
        self.image_character = self.image_front_right

        # creates a rectangle representation using the demensions of image
        self.rect = self.image_front_right.get_rect()

        # get the rectangular representation of the screen
        self.screen_rect = screen.get_rect()

        # aligns the center the ship at bottom-center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # stores a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # call the movement helper function
        self.move_character()

        # call the changes the direction the character is facing
        self.change_direction()

    def move_character(self):
        """Helper function for update that moves the ships position based on key presses"""
        # Updating the ship's center value, not the rect value
        # How the grid is layed out for PyGames is somewhat confusing (0,0) seems to be on the top/right corner
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_character_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_character_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_character_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_character_factor

        # Updates the final rect object position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def change_direction(self):
        """Helper function that changes the character's direction"""
        # exhaustive branch -> probably can simplify with karnaugh map
        # potentially refactor with a data structure
        if self.moving_up:
            if self.image_character == self.image_back_left:
                self.image_character = self.image_back_left
            if self.image_character == self.image_back_right:
                self.image_character = self.image_back_right
            if self.image_character == self.image_front_left:
                self.image_character = self.image_back_left
            if self.image_character == self.image_front_right:
                self.image_character = self.image_back_right
        if self.moving_down:
            if self.image_character == self.image_back_left:
                self.image_character = self.image_front_left
            if self.image_character == self.image_back_right:
                self.image_character = self.image_front_right
            if self.image_character == self.image_front_left:
                self.image_character = self.image_front_left
            if self.image_character == self.image_front_right:
                self.image_character = self.image_front_right
        if self.moving_left:
            if self.image_character == self.image_back_left:
                self.image_character = self.image_back_left
            if self.image_character == self.image_back_right:
                self.image_character = self.image_back_left
            if self.image_character == self.image_front_left:
                self.image_character = self.image_front_left
            if self.image_character == self.image_front_right:
                self.image_character = self.image_front_left
        if self.moving_right:
            if self.image_character == self.image_back_left:
                self.image_character = self.image_back_right
            if self.image_character == self.image_back_right:
                self.image_character = self.image_back_right
            if self.image_character == self.image_front_left:
                self.image_character = self.image_front_right
            if self.image_character == self.image_front_right:
                self.image_character = self.image_front_right

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image_character, self.rect)
