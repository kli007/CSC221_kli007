#screen for TIY

class screen:
     
    def __init__(self):
        self.screen_width = 1004
        self.screen_height = 669
        self.bg_color = (255, 0, 255)

        self.ship_speed = 6

        self.bullet_speed = 7
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 7

        self.alien_speed = 1
        self.fleet_direction = 1
