import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class, which performs a single alien"""
    def __init__(self, game_settings, screen):
        """initializing an alien ship and picking a starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # loading an alien ships
        alien_img = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(alien_img, (game_settings.alien_width, game_settings.alien_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # every new alien appears in higher left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing accurate alien position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # current fleet movement direction
        self.moving_right = True

    def blitme(self):
        #drawing an alien
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.game_settings.alien_speed_factor
            self.rect.x = self.x
        else:
            self.x -= self.game_settings.alien_speed_factor
            self.rect.x = self.x

    def move_down(self):
        self.y -= self.game_settings.alien_speed_factor