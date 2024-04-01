class Settings:
    """A class to store all the settings for Alien invasion"""
     
    def __init__(self):
        """Intialize the game"""
        #Screen settings
        self.screen_width = 1004
        self.screen_height = 669
        self.bg_color = (230, 230, 230)

        self.ship_speed = 10

        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
