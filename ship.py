import pygame


class Ship:  # Create a new module for ship that will allow us to manage the behavior
    """A class to manage the ship"""

    def __init__(self, ai_game):  # Two params - one for the self instance the other for the alien invasion game
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen  # assign screen to the ship attribute
        self.screen_rect = ai_game.screen.get_rect()  # allows us to place the ship in the correct location

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # To load the image and give the location of the ship image
        self.rect = self.image.get_rect()  # When the image is loaded you call the get_rect to access the ships rect attributes
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # position the ship at the bottom center of the screen
        # when working with rect object you can use the x and y coordinates of the top,bottom, left or right

        #Movement flag
        self.moving_right = False # add the self.moving_right and set it false
        self.moving_left = False # movement flag when it is false the ship will me motion less

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right: # Initially at False then moves to True when right key is pressed
            self.rect.x += 1 # Moves to the right one increment
        if self.moving_left: # Initially at False then moves to True when right key is pressed
            self.rect.x -= 1 # Moves to the left one increment negatively


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
