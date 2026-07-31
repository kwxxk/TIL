class Zergling:
    def __init__(self):
        self.hp =20
        self.mana =50

    def run(self):
        print("뛴다")
        self.hp -= 1
        self.mana += 1

    def show_status(self):
        print(f'hp : {self.hp}, mana : {self.mana}')

z1 = Zergling()
z2 = Zergling()

z1.run()
z1.show_status()
for i in range(5):
    z2.run()
z2.show_status()

'''
class Zergling:
    # 생성자 메서드
    def __init__(self):
        self.hp = 20 # 인스턴스 변수
        self.mana = 50

    # 메서드
    def run(self):
        print('뛴다')
        self.hp -= 1
        self.mana += 1

    # 메서드
    def show_status(self):
        print(f'HP : {self.hp}')
        print(f'MANA : {self.mana}')

# 인스턴스 생성
z1 = Zergling()
z2 = Zergling()

# 메서드 호출
z1.run()
z1.show_status()

# 메서드 호출
for _ in range(5): z2.run()
z2.show_status()
'''
