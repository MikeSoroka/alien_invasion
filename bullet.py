import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        """Creating bullet object i nscurrent ship position."""
        super().__init__()
        self.screen = screen

        #creating bullet in position(0,0) and moving it to correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #keeping bullet position as float
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Moving bullet up"""
        #updating bullet position as float
        self.y -= self.speed_factor
        #updating rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)