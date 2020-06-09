import sys  # Use the tools in this module to exit the game when the player quits

import pygame  # contains the functionality we need in order to create a game

from settings import Settings  # import settings to the main file
from ship import Ship  # import ship class


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()  # Intializes the background settings
        self.settings = Settings()  # Created an instance of settings and set it equal to self.setting

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        # create a game window 1200 wide and 800 high
        self.screen = pygame.display.set_mode((1200, 600))
        # assign it to self.screen attribute so we can use it as a method later
        pygame.display.set_caption("Alien Invasion")  # Adds title

        self.ship = Ship(self)  # Create an instance for the ship
        # Set the background color.
        self.bg_color = (230, 230, 230)  # Colors are RGB mix of red green and blue
        # Equal amounts of all colors produce a gray background

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():  # an event is an action that
                # the user performs while playing the game such as a key or moving a mouse
                # Any keyboard or mouse event will cause the for loop to run
                if event.type == pygame.QUIT:  # if player clicks the close window the game will exit
                    sys.exit()  # call this to end the game

        # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # draw the ship on the screen
        # Make the most recently drawn screen visible
            pygame.display.flip()  # Shows the new position/display of the screen - shows smooth movement


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
