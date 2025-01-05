import pygame.font


class Button:
    """为游戏创建按钮"""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染成图像，并且在按钮上居中"""

        # 参数1: 文本
        # 参数2: 抗锯齿
        # 参数3: 文本颜色
        # 参数4: 背景颜色
        self.msg_image = self.font.render(msg,
                                          True,
                                          self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
