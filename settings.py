class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        # The initial value of the ship speed is 1.5
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
    # The amount of bullets a player can shoot on the screen at a time
        self.bullets_allowed = 3