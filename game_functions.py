import sys
import pygame
from alien import Alien
from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Responds to key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def aliens_per_row(game_settings):
    available_space_x = game_settings.screen_width - (game_settings.aliens_distance_x + game_settings.alien_width)
    aliens_amount = int(available_space_x / (game_settings.aliens_distance_x + game_settings.alien_width))
    return aliens_amount

def alien_rows_amount(game_settings):
    usable_place = game_settings.screen_height * game_settings.aliens_fraction_modifier
    rows_amount = int((usable_place - game_settings.alien_height) / (game_settings.aliens_distance_y + game_settings.alien_height))
    return rows_amount

def create_alien(game_settings, screen, aliens, column_number, row_number):
    alien = Alien(game_settings, screen)
    alien.x = game_settings.aliens_distance_x + column_number * (game_settings.alien_width + game_settings.aliens_distance_x)
    alien.y = game_settings.aliens_distance_y + row_number * (game_settings.alien_height + game_settings.aliens_distance_y)
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(game_settings, screen, aliens):
    """creating an aliens fleet."""
    # neighbouring aliens interval is equal to single alien width
    for row in range(alien_rows_amount(game_settings)):
        for column in range(aliens_per_row(game_settings)):
            create_alien(game_settings, screen, aliens, column, row)


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

def update_screen(game_settings, screen, ship, aliens, bullets):
    screen.fill(game_settings.bg_color)
    # all bullets are drawed behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for  alien in aliens:
        alien.blitme()
    # last frame visualisation
    pygame.display.flip()

def update_bullets(bullets):
    """updating bullets positions and destroying old bullets"""
    #bullets positions updating.
    bullets.update()

    #deleting bullets, which have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_fleet(game_settings, screen, aliens):
    last = aliens.sprites()[-1]
    if last.moving_right:
        current_direction = 1
    else:
        current_direction = -1

    if current_direction == 1:
        if int(last.rect.right + game_settings.alien_speed_factor <= screen.get_rect().right):
            aliens.update()
        else:
            for alien in aliens:
                alien.moving_right = False
                alien.y -= game_settings.alien_speed_factor
                alien.rect.y = alien.y

    else:
        first = aliens.sprites()[0]
        if int(first.rect.left - game_settings.alien_speed_factor >= 0):
            aliens.update()
        else:
            for alien in aliens:
                alien.moving_right = True
                alien.y -= game_settings.alien_speed_factor
                alien.rect.y = alien.y
