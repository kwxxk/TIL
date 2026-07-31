# 상속 하는 이유 (상속을 하면 할 수 있는 것)
# 1. 부모 메서드 교체 (오버라이딩)
# 2. 새로운 메서드를 추가

# 부모 클래스
class Bicycle:
    def pedal(self):
        print('자전거 페달을 밟는다')
    def gear(self):
        print('자전거 기어를 조정한다')

# 자식 클래스의 인자로 부모클래스가 들어 가야한다.
class AutoBicycle(Bicycle):
    def pedal(self): # 오버라이딩 (메서드 재정의) - 부모 메서드가 교체
        print('승차감이 정말 좋아요')

    def auto(self): # 메서드 추가
        print('오르막길에서 자동으로 운행해요')

    def bike(self):
        super().gear() # 부모 클래스의 메서드를 호출 할 수 있음
        print('그리고, 1단부터 5단까지 조절할 수 있어요')

#인스턴스 생성
cycle = AutoBicycle()

#메서드 호출
cycle.pedal()
cycle.auto()
cycle.bike()
