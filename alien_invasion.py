import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Generic class for resource management.
    """

    def __init__(self):
        """
        Game initialization and generation of resources.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Definition of shooting spaceship
        self.ship = Ship(self)

    def run_game(self):
        """
        Start of the main game loop.
        """
        while True:
            # Waiting for keyboard/mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Display refresh
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Showing modified game screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
