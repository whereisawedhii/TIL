# 아래 클래스를 수정하시오.
# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self) :
        Animal.num_of_animal += 1
        
    def bark(self) : 
        print('멍멍!')


class Cat(Animal):
    def __init__(self) :
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    def access_num_of_animal() :
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'

dog1 = Dog()
dog1.bark()
