import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initializing game and making game screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(game_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings, screen, ship)

run_game()
