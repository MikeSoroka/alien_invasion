import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initializing game and making game screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #creating ship
    ship = Ship(game_settings, screen)
    #creating group for storing bullets
    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(game_settings, screen, ship, bullets)

run_game()
