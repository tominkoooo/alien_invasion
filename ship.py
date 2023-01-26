import pygame


class Ship:
    """
    Class dedicated to alien ship management.
    """
    def __init__(self, ai_game):
        """
        Initialization of ship and its initial position.
        :param ai_game: instance of AlienInvasion class (actual game)
        """

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image 'ufo.bmp' and place it in rectangle
        self.image = pygame.image.load('images/spaceship.bmp')
        self.ship_size = (70, 70)
        self.image = pygame.transform.scale(self.image, self.ship_size)
        self.rect = self.image.get_rect()

        # Every new ship will appear on mid-bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        Show ship at its current poisition
        """
        self.screen.blit(self.image, self.rect)
