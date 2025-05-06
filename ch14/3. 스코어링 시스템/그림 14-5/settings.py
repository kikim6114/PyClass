# "14.3 스코어링 시스템"
# 그림 14-5

class Settings:
    """Alien Invasion을 위한 모든 설정을 저장하는 클래스."""

    def __init__(self):
        """정적(static) 설정 초기화."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 300 #3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30 # 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # 게임의 가속도.
        self.speedup_scale = 1.1
        # 외계인 파괴 득점 가속도.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """게임 중 변하는 설정(동적 설정)."""
        self.ship_speed = 3 # 1.5 
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # 함대 방향: 1 은 우측, -1은 좌측.
        self.fleet_direction = 1
        
        # 득점 설정
        self.alien_points = 50

    def increase_speed(self):
        """가속된 속도 설정 및 외계인 파괴 점수 설정"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)