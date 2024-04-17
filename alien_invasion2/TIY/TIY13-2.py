#TIY12 from chapter 13

import pygame
import sys
from random import randint
from stars import Star

class night:

    def __init__(self):
        self.stars = pygame.sprite.Group()
        self.bg_color = (255, 255, 255)
        self.screen_height = 669
        self.screen_width = 1004
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self._create_fleet()

        pygame.display.set_caption("TIY 13-2")

    def run_screen(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star.rect.size

        while current_y < (self.screen_height - 2 * star_height):
            while current_x < (self.screen_width - 2 * star_width):
                random_number = randint(-40, 40)
                self._create_star(current_x + random_number, current_y + random_number)
                current_x += 2 * star_width
            current_x = star_width
            current_y += 2 * star_height
        
    def _create_star(self, x_position, y_position):
        '''Creates star and postions it in the row'''
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()
        


if __name__ == '__main__':
    screen = night()
    screen.run_screen()

    

