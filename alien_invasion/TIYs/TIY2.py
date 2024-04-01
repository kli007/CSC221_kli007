#TIY2

import pygame
import sys
from screen import screen
from image import image

class ship:

    def __init__(self):
        self.settings = screen()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.image = image(self)
        pygame.display.set_caption("TIY 2")


    def run_screen(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.image.blitme()
        pygame.display.flip()
        


if __name__ == '__main__':
    ship = ship()
    ship.run_screen()

    

