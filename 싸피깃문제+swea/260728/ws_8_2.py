# 아래 클래스를 수정하시오.
# class Dog:
#     pass
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
    

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def bark(self):
         print('멍멍 !')
    


class Cat(Animal):
    def __init__(self):
            super().__init__()


class Pet(Dog,Cat):
    pass

dog1 = Dog()
dog1.bark()
