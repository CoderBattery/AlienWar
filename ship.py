import pygame.image


class Ship:
    """管理飞船的类"""

    def __init__(self, alien_invasion):
        """初始化飞船并设置初始位置"""

        self.screen = alien_invasion.screen
        self.settings = alien_invasion.settings

        # 加载飞船图标，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 飞船初始化放在屏幕底部的中央
        self.rect.midbottom = self.screen.get_rect().midbottom

        # 这里必须要浮点数，不然+=可能不变
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞创"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # 根据浮点数更新rect坐标
        self.rect.x = self.x
