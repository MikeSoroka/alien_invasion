import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Responds to key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responds to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """detecting mouse and keyboard usage"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(game_settings, screen, ship, bullets):
    """fires a bullet, if bullets amount limit is not achieved"""
    # creating a new bullet and adding it to bullets group.
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(game_settings, screen, ship, bullets):
    screen.fill(game_settings.bg_color)
    #all bullets are drawed behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #last frame visualisation
    pygame.display.flip()

def update_bullets(bullets):
    """updating bullets positions and destroying old bullets"""
    #bullets positions updating.
    bullets.update()

    #deleting bullets, which have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)