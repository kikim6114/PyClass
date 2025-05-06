# "14.3 스코어링 시스템"
# 그림 14-3

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """점수 정보를 보고하기 위한 클래스."""

    def __init__(self, ai_game):
        """스코어 관리 속성 초기화."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 점수 정보를 위한 폰트 설정.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 최초 점수 이미지 준비.
        self.prep_score()
        # self.prep_high_score()
        # self.prep_level()
        # self.prep_ships()

    def prep_score(self):
        """점수를 렌더링된 이미지로 변환."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # 점수를 스크린의 우측 상단에 배치.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # def prep_high_score(self):
    #     """최고 점수를 렌러링된 이미지로 변환."""
    #     high_score = round(self.stats.high_score, -1)
    #     high_score_str = f"{high_score:,}"
    #     self.high_score_image = self.font.render(high_score_str, True,
    #             self.text_color, self.settings.bg_color)
        
    #     # 최고 점수를 스크린 상단 중앙에 배치.
    #     self.high_score_rect = self.high_score_image.get_rect()
    #     self.high_score_rect.centerx = self.screen_rect.centerx
    #     self.high_score_rect.top = self.score_rect.top

    # def prep_level(self):
    #     """레벨을 렌더링된 이미지로 변환."""
    #     level_str = str(self.stats.level)
    #     self.level_image = self.font.render(level_str, True,
    #             self.text_color, self.settings.bg_color)

    #     # 레벨을 점수 아래에 배치.
    #     self.level_rect = self.level_image.get_rect()
    #     self.level_rect.right = self.score_rect.right
    #     self.level_rect.top = self.score_rect.bottom + 10

    # def prep_ships(self):
    #     """남은 우주선 수 반환."""
    #     self.ships = Group()
    #     for ship_number in range(self.stats.ships_left):
    #         ship = Ship(self.ai_game)
    #         ship.rect.x = 10 + ship_number * ship.rect.width
    #         ship.rect.y = 10
    #         self.ships.add(ship)

    # def check_high_score(self):
    #     """새로운 최고 점수가 있는지 확인."""
    #     if self.stats.score > self.stats.high_score:
    #         self.stats.high_score = self.stats.score
    #         self.prep_high_score()

    def show_score(self):
        """점수를 스크린에 표시."""
        self.screen.blit(self.score_image, self.score_rect)
        # self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.screen.blit(self.level_image, self.level_rect)
        # self.ships.draw(self.screen)
