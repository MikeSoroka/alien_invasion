class Settings():
    #class for keeping game settings

    def __init__(self):
        """initializing game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_width = 35
        self.ship_height= 35

        #alien ships settings
        self.alien_speed_factor = 1.5
        self.alien_width = 40
        self.alien_height = 35
        self.aliens_fraction_modifier = 0.5
        self.aliens_distance_x = 1.5 * self.alien_width
        self.aliens_distance_y = 1.5 * self.alien_height

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
