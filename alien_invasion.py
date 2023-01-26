import sys

import pygame


class AlienInvasion:
    """
    Generic class for resource management.
    """

    def __init__(self):
        """
        Game initialization and generation of resources.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        Start of the main game loop.
        """
        while True:
            # Waiting for keyboard/mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Showing modified game screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
