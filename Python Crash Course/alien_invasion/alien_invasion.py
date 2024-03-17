import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

ai_setting = Settings()


def run_game():

    pygame.init()

    # this screen instance is called surface, so a part of the screen where elements are displayed
    screen = pygame.display.set_mode(ai_setting.dimensions)

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_setting)

    bullets = Group()

    while True:

        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()