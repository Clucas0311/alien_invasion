import pygame


class Ship:  # Create a new module for ship that will allow us to manage the behavior
    """A class to manage the ship"""

    def __init__(self, ai_game):  # Two params - one for the self instance the other for the alien invasion game
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen  # assign screen to the ship attribute
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # allows us to place the ship in the correct location

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # To load the image and give the location of the ship image
        self.rect = self.image.get_rect()  # Load image in rectangle attributes
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # position the ship at the bottom center of the screen
        # when working with rect object you can use the x and y coordinates of the top,bottom, left or right

        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False  # add the self.moving_right and set it false
        self.moving_left = False  # movement flag when it is false the ship will me motionless

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Initially at False then moves to True when right key is pressed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # Moves to the right one increment

        if self.moving_left and self.rect.left > 0:  # Initially at False then moves to True when right key is pressed
            self.x -= self.settings.ship_speed  # Moves to the left one increment negatively

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
