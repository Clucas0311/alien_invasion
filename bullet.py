import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

    # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop # bullets will emerge from the top of the ship

    # Store the bullet's position as a decimal value.
    # this will make adjustments towards the bullets speed
        self.y = float(self.rect.y)
     # Changes the bullets position
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        # Allows us to increase the speed of the bullet when needed
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)