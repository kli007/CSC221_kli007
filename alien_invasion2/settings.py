class Settings:
    """A class to store all the settings for Alien invasion"""
     
    def __init__(self):
        """Intialize the game"""
        #Screen settings
        self.screen_width = 1004
        self.screen_height = 669
        self.bg_color = (230, 230, 230)

        self.ship_speed = 5

        self.bullet_speed = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #directions of alien fleet, 1 is right, -1 is left
        self.fleet_direction = 1
