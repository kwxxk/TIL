# 클래스 정의
class SetMenu:
    #생성자 메서드
    def __init__(self):
        self.hambug = 400 # 인스턴스 변수(속성)
        self.potato = 100

    # 메서드
    def eat(self):
        print('햄버거 베토티 세트 맛있다.')
        print(f'음 {self.hambug + self.potato}불 비용이 들었네')

# 클래스 호출
# 변수 = 클래스명()
# 인스턴스 생성
betodi = SetMenu()
# 메서드 호출
betodi.eat()
# print(id(betodi))


