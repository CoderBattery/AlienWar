class Settings:
    """存储游戏所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度，每次移动的像素值
        self.ship_speed = 3
        # 飞船数量
        self.ship_limit = 3

        # 子弹相关设置
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # 外星人左右移动的速度
        self.alien_speed = 1.0
        # 外星人向下移动的速度
        self.alien_speed_y = 40
        # 1表示向右移动 -1表示向左移动
        self.alien_direct = 1
