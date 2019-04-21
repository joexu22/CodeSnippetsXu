# settings for alien invasion game


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_character_factor = 1.5

        # Fireball settings
        self.fireball_speed_factor = 1.0
        self.fireball_width = 15
        self.fireball_height = 3
        self.fireball_color = 60, 60, 60
        self.fireballs_allowed = 3