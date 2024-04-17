#TIY5

import pygame
import sys

from screen import screen
from image import image
from bullet import Bullet
from Alien import Alien

class game:
    fleet = 0
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.settings = screen()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self._create_fleet()

        self.image = image(self)
        pygame.display.set_caption("TIY 13-5")


    def run_game(self):
        while True:
            self._check_events()
            self.image.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_over()

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
            self._game_over()
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
        self._check_bullet_alien_collision()

    
    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.image.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        self.fleet += 1
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = self.settings.screen_width  - alien_width
        current_y = self.settings.screen_height - alien_height

       

        while current_x > (self.settings.screen_width * 3/5):
            while current_y > (alien_height):
                self._create_alien(current_x, current_y)
                current_y -= 2 * alien_height
            current_x -= 2 * alien_width
            current_y = self.settings.screen_height - alien_height
        
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        screen_width = self.settings.screen_width
        section_width = screen_width / 3  # Divide the screen into 3 equal sections

        # Create a dictionary to store the edge status for each section
        edge_status = {section: False for section in range(3)}

        # Check each alien's edge status and update edge_status dictionary
        for alien in self.aliens.sprites():
            section = int(alien.rect.centerx // section_width)  # Determine which section the alien is in
            if alien.check_edges():
                edge_status[section] = True
            if alien.check_game():
                self._game_over()

        # Change fleet direction if any section has an edge
        if any(edge_status.values()):
            self.settings.fleet_direction *= -1

    def _game_over(self):
        print (f'Game Over: You lasted {self.fleet} fleets')
        sys.exit()


if __name__ == '__main__':
    game = game()
    game.run_game()

    

