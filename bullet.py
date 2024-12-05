import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所发射子弹的类"""

    def __init__(self, alien_invasion):
        """在飞船当前位置创建子弹对象"""
        super().__init__()
        self.screen = alien_invasion.screen
        self.settings = alien_invasion.settings
        self.color = self.settings.bullet_color

        # 默认子弹的位置在飞船的上部中央
        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = alien_invasion.ship.rect.midtop

        # 存储子弹的位置
        self.y = float(self.rect.y)

    def update(self, *args, **kwargs):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        print(self.rect.left, self.rect.top, self.rect.right, self.rect.bottom)
        pygame.draw.rect(self.screen, self.color, self.rect)
