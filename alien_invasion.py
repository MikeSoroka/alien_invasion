import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # initializing game and making game screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # creating ship, aliens group and bullets group
    ship = Ship(game_settings, screen)
    aliens = Group()
    gf.create_fleet(game_settings, screen, aliens)
    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        gf.update_fleet(game_settings, screen, aliens)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

run_game()
