#TIY 4 for chapter 13

import pygame
import sys
from Rain import Raindrop
from screen import Screen

class rain:

    def __init__(self):
        self.rain = pygame.sprite.Group()
        self.settings = Screen()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.bg_color = (255, 255, 255)
        
        self._create_fleet()

        pygame.display.set_caption("TIY 13-4")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        rain = Raindrop(self)
        rain_width, rain_height = rain.rect.size

        current_x, current_y = rain.rect.size

        while current_y < (self.settings.screen_height - 2 * rain_height):
            while current_x < (self.settings.screen_width - 2 * rain_width):
                self._create_rain(current_x, current_y)
                current_x += 2 * rain_width

            current_x = rain_width
            current_y += 2* rain_height
        
    def _create_rain(self, x_position, y_position):
        new_rain = Raindrop(self)
        new_rain.x = x_position
        new_rain.rect.x = x_position
        new_rain.rect.y = y_position
        self.rain.add(new_rain)

    def _update_rain(self):
        self._check_fleet_edges()
        self.rain.update()

    def _check_fleet_edges(self):
        for raindrop in self.rain.sprites():
            if raindrop.check_edges():
                self.rain.remove(raindrop)
                self._add_new_row()
                break
                

    def _add_new_row(self):
        rain = Raindrop(self)
        rain_width = rain.rect.x

        current_x = rain.rect.x

        while current_x < (self.settings.screen_width - 2 * rain_width):
            self._create_rain(current_x, 0)
            current_x += 2 * rain_width

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)
        pygame.display.flip()
        
    def run_screen(self):
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    screen = rain()
    screen.run_screen()

    

