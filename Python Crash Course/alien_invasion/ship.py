import pygame


class Ship:

    def __init__(self, screen, ai_settings):

        self.screen = screen
        self.ai_settings = ai_settings
        # basic sprite creation and create another surface
        self.image = pygame.image.load('assets/mainShip.png')

        # getting the rectangle boundaries
        self.rect = self.image.get_rect()
        # store the main screen rect
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor

        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blit_me(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)