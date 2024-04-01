#TIY5

import pygame
import sys

class keys:

    def __init__(self):
        self.screen = pygame.display.set_mode((255, 100))
        pygame.display.set_caption("TIY 5")

    def run_screen(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(f'{event.key}\n')

    def _update_screen(self):
        pygame.display.flip()
        


if __name__ == '__main__':
    key = keys()
    key.run_screen()

    

