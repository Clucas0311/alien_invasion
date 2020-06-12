import sys  # Use the tools in this module to exit the game when the player quits

import pygame  # contains the functionality we need in order to create a game

from settings import Settings  # import settings to the main file
from ship import Ship  # import ship class
from bullet import Bullet # imports the bullet class


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()  # Initializes the background settings
        self.settings = Settings()  # Created an instance of settings and set it equal to self.setting


        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # Tells pygame to figure out a window size that will fill the screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width # update the screen width
        self.settings.screen_height = self.screen.get_rect().height # updates the screen's height
        pygame.display.set_caption("Alien Invasion")  # Adds title

        self.ship = Ship(self)  # Create an instance for the ship
        # Set the background color.
        self.bullets = pygame.sprite.Group()
        self.bg_color = (230, 230, 230)  # Colors are RGB mix of red green and blue
        # Equal amounts of all colors produce a gray background


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            # Watch for keyboard and mouse events

        # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)


    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():  # an event is an action that
            # the user performs while playing the game such as a key or moving a mouse
            # Any keyboard or mouse event will cause the for loop to run
            if event.type == pygame.QUIT:  # if player clicks the close window the game will exit
                sys.exit()  # call this to end the game
            elif event.type == pygame.KEYDOWN:  # Key down - The key will move in a fluid motion continuously in the
                # on direction
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # if the left key is pressed
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # allows the user to exit the game by pressing "q"
            sys.exit()
        elif event.key == pygame.K_SPACE: # when the space key is pressed
            self._fire_bullet()  # bullet fires

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT: # if right key is released
            self.ship.moving_right = False # The ship will be back to false
        elif event.key == pygame.K_LEFT: # if left key is pressed
            self.ship.moving_left = False # the ship will be motionless set to False position

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # draw the ship on the screen
        # Make the most recently drawn screen visible

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()  # Shows the new position/display of the screen - shows smooth movement


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
