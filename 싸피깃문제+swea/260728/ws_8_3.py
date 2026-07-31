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
    def meow(self):
        print('야옹 !')


class Pet(Dog,Cat):
    pass

cat1 = Cat()
cat1.meow()
