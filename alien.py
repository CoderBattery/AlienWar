import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, alien_invasion):
        """初始化外星人的类"""
        super().__init__()
        self.screen = alien_invasion.screen
        self.settings = alien_invasion.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人左上角的坐标x,y
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)



    def update(self, *args, **kwargs):
        self.x += self.settings.alien_speed
        self.rect.x = self.x
