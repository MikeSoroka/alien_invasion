import pygame

class Ship():

    def __init__(self, game_settings, screen):
        """initializing a ship and picking a starting position"""
        self.screen = screen
        self.game_settings = game_settings

        #loadind a ship
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #every new ship is appearing in the lowest part of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #saving real coordinate of ship center(self.rect.centerx is always belongs to int type)
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updating ship position depending on flag"""
        #calculating ship.center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.game_settings.ship_speed_factor

        #updating self.rect according to self.center
        self.rect.centerx = self.center
    def blitme(self):
        """Drawing ship in current position"""
        self.screen.blit(self.image, self.rect)
