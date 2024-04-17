import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class for the aliens in the game'''

    def __init__(self, ai_game):
        '''Intialize the aliens and sets their position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        '''Moves Alien left and right'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x