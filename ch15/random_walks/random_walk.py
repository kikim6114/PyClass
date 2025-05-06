from random import choice

class RandomWalk:
    """랜덤 워크를 생성하는 클래스."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # 모든 보행은 (0, 0)에서 시작.
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """보행 내의 모든 점들을 계산."""
        # 보행이 원하는 길이에 도달할 때까지 계속 걷는다.
        while len(self.x_values) < self.num_points:

            # 어느 방향으로 갈 지, 얼마만큼 갈 지 결정.
            x_direction = choice([1, -1])  # 우측, 좌측
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])  # 위, 아래
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 제자리인 이동은 무시하고 다시 방향을 결정한다.
            if x_step == 0 and y_step == 0:
                continue

            # 새 위치 계산.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)