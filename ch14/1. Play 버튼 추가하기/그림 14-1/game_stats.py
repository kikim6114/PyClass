# 1. Play 버튼 추가하기
# 그림 14-1

class GameStats:
    """Alien Invasion에 대한 통계 추적."""

    def __init__(self, ai_game):
        """통계 초기화."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """게임 중 변하는 통계의의 초기화."""
        self.ships_left = self.settings.ship_limit
        self.score = 0