import sys

import pygame

import time

from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # 设置屏幕宽高
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # 设置全屏游戏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # 设置屏幕标题
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # 子弹编组
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # 不加clock flip这个方法的刷新频率有点高，需要控制下
            # 游戏的帧率，一秒60次
            self.clock.tick(60)

    def _check_event(self):
        """响应按键和鼠标事件"""
        # pygame.event.get()返回一个列表，包含上次调用后发生的所有事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 点击小窗的X按钮，小窗直接关闭,
                # 不写的话无法点击X关闭小窗
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应down"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 空格键发射子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像"""
        # 设置背景色,必须每次要刷新，不然子弹变成一条线
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
