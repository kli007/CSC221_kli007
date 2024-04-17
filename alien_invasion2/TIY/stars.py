import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''A class for the aliens in the game'''

    def __init__(self, ai_game):
        '''Intialize the aliens and sets their position'''
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('alien_invasion\images\star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)