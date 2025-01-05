import pygame.font


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """得分渲染为图像"""

        # round参数1：
        # round参数2：指定为负数，会将数字舍入到最近的10的倍数
        round_score = round(self.stats.score, -1)
        # ;,  表示在合适的位置插入逗号 1,000,000
        score_str = f"{round_score:,}"

        self.score_image = self.font.render(
            score_str,
            True,
            self.text_color,
            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.score_image, self.score_rect)

    def prep_high_score(self):
        """总分渲染为图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color,
            self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def check_high_score(self):
        """检查是否超过了最高分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()