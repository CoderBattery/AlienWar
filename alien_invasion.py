import sys

import pygame

import time

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
        # 设置屏幕标题
        pygame.display.set_caption("Alien Invasion")

        # 设置背景色
        self.screen.fill(self.settings.bg_color)

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()

            self.ship.update()

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
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像"""
        # 绘制飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
