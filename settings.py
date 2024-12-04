class Settings:
    """存储游戏所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度，每次移动的像素值
        self.ship_speed = 1.5
