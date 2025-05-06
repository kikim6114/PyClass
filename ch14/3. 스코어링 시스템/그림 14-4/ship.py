# "14.3 스코어링 시스템"
# 그림 14-4

import pygame

class Ship:
    """우주선을을 관리하는 클래스."""

    def __init__(self, ai_game):
        """우주선 초기화 및 출발 위치 설정."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """우주선을 스크린 중앙에 배치."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """이동 플래그를 기반으로 우주선의 위치를 업데이트."""
        # 우주선의 rect가 아니라 우주선의 x 값 을 업데이트.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # self.x로부터 rect 객체 업데이트트.
        self.rect.x = self.x

    def blitme(self):
        """현재 위치에 우주선 그리기."""
        self.screen.blit(self.image, self.rect)