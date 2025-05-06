# 1. Play 버튼 추가하기
# 그림 14-1 개선

class Settings:
    """Alien Invasion을 위한 모든 설정을 저장하는 클래스."""

    def __init__(self):
        """설정 초기화."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # 함대 방향: 1 은 우측, -1은 좌측.
        self.fleet_direction = 1