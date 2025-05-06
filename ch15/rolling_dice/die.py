from random import randint

class Die:
    """한 개의 주사위를 나타내는 클래스."""

    def __init__(self, num_sides=6):
        """정육면체 주사위라고 가정."""
        self.num_sides = num_sides

    def roll(self):
        """"1과 면의 수(6) 사이의 무작위 값을 반환."""
        return randint(1, self.num_sides)