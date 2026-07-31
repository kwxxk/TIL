# @ : 데코레이터
# 매직 메서드, 클래스 메서드, 스태틱 메서드

class Calculator:
    pi = 3.141592 # 클래스 변수

    #생성자 메서드
    def __init__(self, name):
        self.name = name #인스턴스 변수

    # 메서드
    def add(self, a, b):
        return a+b

    # 매직 메서드 ---> 객체를 문자열로 표현할때 호출됨
    def __str__(self):
        return f'Caculator name : {self.name}'

    # 클래스 메서드 ---> 클래스 자체를 첫 번째 인자로 받는다.
    @classmethod
    def get_pi(cls):
        return f'파이(pi)의 값은 {cls.pi}다.'

    # 스태틱 메서드 ---> 인자로 self나 cls가 X, 독립적으로 실행 가능
    @staticmethod
    def multiply(a,b):
        return a * b

# 인스턴스 생성
calc = Calculator("카시오 공학용 계산기")
# 메서드 호출
print(calc.add(5,7))

# 매직 메서드 호출 : 인스턴스 할당한 변수
print(calc)

# 클래스 메서드 호출
print(Calculator.get_pi())

# 스태틱 메서드
print(Calculator.multiply(2,3)) #클래스 직접 호출
print(calc.multiply(100,100)) #인스턴스로 호출