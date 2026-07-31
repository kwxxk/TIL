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
        self.sound = "멍멍 !"
    def bark(self):
         print('멍멍 !')
    


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound = "야옹 !"
    def meow(self):
        print('야옹 !')


class DogPet(Dog,Cat):
    def __init__(self, sound=None):
        super().__init__()
        if sound is not None:
            self.sound = sound
    def make_sound(self):
        print(self.sound)
    def play(self):
        print("애완동물과 놀기")

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    
class CatPet(Cat, Dog):
    def __init__(self, sound=None):
        super().__init__()
        if sound is not None:
            self.sound=sound
    def make_sound(self):
        print(self.sound)
    def play(self):
        print("애완동물과 놀기")

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

p1 =DogPet()
print(p1)
p2 =CatPet()
print(p2)