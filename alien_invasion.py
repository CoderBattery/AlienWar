import sys
from time import sleep

import pygame

import time

from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from settings import Settings
from ship import Ship
from button import Button


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

        self.stats = GameStats(self)

        self.ship = Ship(self)

        # 子弹编组
        self.bullets = pygame.sprite.Group()

        # 创建外星人舰队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_event()
            if self.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()

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
        """发射子弹，加入编组"""
        if len(self.bullets) < self.settings.bullet_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def update_bullets(self):
        """更新子弹位置并删除已消失的子弹"""
        self.bullets.update()
        # 删除出界的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_alien_collide()

    def check_bullet_alien_collide(self):
        # 当子弹和外星人精灵触碰后，两者都消失
        # 第一个True 表示触碰后子弹是否消失消失
        # 第二个True 表示触碰后外星人是否消失
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # groupcollide后 aliens中外星人会消失
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

        # 检测一个精灵和一个编组是否发生碰撞
        # 未碰撞则返回none
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("ship hit!!!")
            self.ship_hit()

        self.check_aliens_bottom()

    def check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.ship_hit()
                break

    def ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            # 清空子弹和外星人
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(5)
        else:
            self.game_active = False

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_speed_y
        self.settings.alien_direct *= -1

    def _create_fleet(self):
        """创建一个外星人舰队"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self.create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一行后，充值x值，并递增y
            current_x = alien_width
            current_y += 2 * alien_height

    def create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """更新屏幕上的图像"""
        # 设置背景色,必须每次要刷新，不然子弹变成一条线
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
