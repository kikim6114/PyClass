"""전기차를 나타내는 데 사용될 수 있는 클래스 모음."""

from car import Car

class Battery:
    """전기차 배터리를 모델링하기 위한 간단한 시도."""

    def __init__(self, battery_size=40):
        """배터리 속성 초기화."""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 용량을 나타내는 문장을 프린트."""
        print(f"이 자동차의 배터리 용량은 {self.battery_size}-kWh 입니다.")

    def get_range(self):
        """현재 배터리로 갈 수 있는 주행거리를 프린트."""
        if self.battery_size == 40:
            range = 450
        elif self.battery_size == 65:
            range = 625
        
        print(f"완전 충전 상태에서 {range} Km를 주행할 수 있습니다.")

class ElectricCar(Car):   # 괄호 안에 부모 클래스(superclass)
    """전기자동차에만 국한된 차의 특성들을 나타낸다."""

    def __init__(self, make, model, year):  # 부모 클래스인 Car의 인스턴스를 만들기 위해 제공해야 하는 정보
        """
        부모 클래스의 속성과 메서드를 초기화한다.
        그런 다음, 전기자동차에만 국한된 차의 특성들을 나타낸다.
        """
        super().__init__(make, model, year) # 부모 클래스의 __init__() 메서드 호출. 부모 클래스의 모든 속성과 메서드가 상속된다.
        self.battery = Battery()  # 컴포지션

    def fill_gas_tank(self):  # 전기차에서 이 메서드는 맞지 않는다. 충전하는 메서드로 바꿔야 한다.
        """전기차는 연료 탱크가 없다."""
        print(f"전기차는 연료 탱크가 없습니다!")