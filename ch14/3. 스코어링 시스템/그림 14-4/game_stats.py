# "14.3 스코어링 시스템"
# 그림 14-4

class GameStats:
    """Alien Invasion에 대한 통계 추적."""

    def __init__(self, ai_game):
        """통계 초기화."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # 최고 점수는 절대 리셋되면 안된다.
        self.high_score = 1200050

    def reset_stats(self):
        """게임 중 변하는 통계의 초기화."""
        self.ships_left = self.settings.ship_limit
        self.score = 0