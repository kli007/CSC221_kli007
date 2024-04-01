#TIY4

import pygame
import sys

from screen import screen
from image import image
from bullet import Bullet

class game:

    def __init__(self):
        self.settings = screen()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bullets = pygame.sprite.Group()
        self.image = image(self)
        pygame.display.set_caption("TIY 6")


    def run_game(self):
        while True:
            self._check_events()
            self.image.update()
            self._update_bullets()
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
        if event.key == pygame.K_UP:
            self.image.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.image.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.image.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.image.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.sprites():
            if bullet.rect.left > self.image.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.image.blitme()
        pygame.display.flip()
        


if __name__ == '__main__':
    game = game()
    game.run_game()

    

