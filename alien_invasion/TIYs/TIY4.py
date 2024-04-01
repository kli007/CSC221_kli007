#TIY4

import pygame
import sys
from screen import screen
from image import image

class controls:

    def __init__(self):
        self.settings = screen()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.image = image(self)
        pygame.display.set_caption("TIY 4")


    def run_game(self):
        while True:
            self._check_events()
            self.image.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.image.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.image.moving_left = True
        elif event.key == pygame.K_UP:
            self.image.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.image.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.image.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.image.moving_left = False
        elif event.key == pygame.K_UP:
            self.image.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.image.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.image.blitme()
        pygame.display.flip()
        


if __name__ == '__main__':
    control = controls()
    control.run_game()

    

