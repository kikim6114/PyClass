"""자동차를 나타내는 데 사용될 수 있는 클래스"""

class Car:
    """자동차를 나타내는 단순한 시도."""
    
    def __init__(self, make, model, year):
        """자동차를 설명하는 속성들을 초기화."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  
        
    def get_descriptive_name(self):
        """깔끔하게 처리된 이름을 반환."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """차량의 주행거리를 보여주는 문장을 프린트."""
        print(f"이 차량의 주행거리는 {self.odometer_reading} Km 입니다.")

    def update_odometer(self, mileage):  
        """
        주행계 값을 주어진 값으로 설정.
        주행계 값을 뒤로 돌리려는 시도는 거부.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행계는 되돌릴 수 없습니다!")

    def increment_odometer(self, miles):
        """주행계 값을 주어진 값만큼 더하기."""
        self.odometer_reading += miles

    def fill_gas_tank(self):  
        """연료 탱크를 채운다."""
        print(f"이제 연료 탱크를 가득 채웠습니다.")

    def decrement_odometer(self, miles):
        """주행계 값에서 주어진 값만큼 빼기."""
        self.increment_odometer(-miles)
        print(f"주행계가 {self.odometer_reading} Km로 줄었습니다.")