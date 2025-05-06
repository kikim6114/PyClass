# "14.3 스코어링 시스템"
# 그림 14-4

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """함대에 속한 한 대의 외계인를 나타내는 클래스."""

    def __init__(self, ai_game):
        """외계인 초기화하고 출발 위치 설정."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 외계인 로드하고 rect 속성 설정.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 스크린 좌상단 근처에서 각 신규 외계인 출발.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 외계인의 정확한 수평 위치 저장.
        self.x = float(self.rect.x)

    def check_edges(self):
        """외계인이 스크린 좌/우 변에 있으면 True 반환."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """외계인을 좌측 또는 우측으로 이동."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x