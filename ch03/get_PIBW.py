"""
표준체중대비 백분율(PIBW)과 비만도 알아보기
"""
# 1. 함수 만들기
def get_std_weight(gender, height):
  height = height/100
  if gender == 0:
    weight_factor = 22
  else:
    weight_factor = 21
    
  return weight_factor*(height**2)

# 2. 간단한 인사 메시지 출력하기
print("안녕하세요! 파이썬 클래스에 오신 것을 환영합니다.")
print("자신의 표준체중과 비만도를 알아보세요.")

# 3. 키보드 입력, 스트링 변수
name = input("이름 : ")
gender = -1

# 4. while loop
while gender < 0:
  gender = int(input("성별(남=0, 여자=1) : "))
# 5. 조건문
  if gender == 0 or gender == 1:
    height = int(input("신장(cm) : "))
    weight = int(input("체중(Kg) : "))
  else:
    print("성별 입력 값을 바르게 입력하세요.")

# 6. 함수 호출
standard_weight = get_std_weight(gender, height)  # 표준체중
PIBW = int(100*weight/standard_weight)  # 표준체중 대비 백분율(PIBW, Percent of Ideal Body Weight)

# 7. 조건문
if PIBW < 90:
  obesity = "저체중"
elif 90 <= PIBW < 110:
  obesity = "정상 체중"
elif PIBW >= 110 and PIBW < 120:
  obesity = "과체중"
elif PIBW >= 120:
  obesity = "비만 체중"

# 8. 출력
print(f"{name}님의 표준체중은 {standard_weight: .1f}kg 입니다")
print(f"비만율은 {PIBW}% 이며,", end='')
print(f"{obesity}입니다.")