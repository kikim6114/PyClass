# "14.3 스코어링 시스템"
# 그림 14-4

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """우주선에서 발사한 총알을 처리하기 위한 클래스."""

    def __init__(self, ai_game):
        """우주선의 현재 위치에서 총알 객체 생성."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # (0, 0)에 bullet rect 생성하고 위치 지정.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # bullet 위치를 float로 저장.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # bullet의 정확한 위치 업데이트.
        self.y -= self.settings.bullet_speed
        # rect 위치 업데이트.
        self.rect.y = self.y

    def draw_bullet(self):
        """스크린에 총알 그리기."""
        pygame.draw.rect(self.screen, self.color, self.rect)