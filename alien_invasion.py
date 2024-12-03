import sys

import pygame
from pygame.event import event_name


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 设置屏幕宽高
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置屏幕标题
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏的主循环"""
        while True:

            # pygame.event.get()返回一个列表，包含上次调用后发生的所有事件
            for key_event in pygame.event.get():
                print(key_event.type)
                if key_event.type == pygame.QUIT:
                    # 点击小窗的X按钮，小窗直接关闭,
                    # 不写的话无法点击X关闭小窗
                    sys.exit()


            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
