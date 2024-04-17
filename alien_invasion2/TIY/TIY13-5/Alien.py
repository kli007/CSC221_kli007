import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('alien_invasion2/TIY/TIY13-5/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom)
    
    def check_game(self):
        return self.rect.left <= 0
    
    def update(self):
        self.rect.x -= self.settings.alien_speed
        self.rect.y += self.settings.alien_speed * self.settings.fleet_direction
        