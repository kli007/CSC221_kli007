#TIY1

import pygame
import sys
from screen import screen

class Sky:

    def __init__(self):
        self.settings = screen()
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("TIY 1")

    def run_screen(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
        


if __name__ == '__main__':
    screen = Sky()
    screen.run_screen()

    

