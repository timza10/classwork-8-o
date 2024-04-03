class Dog:
    name='unknown'
    def __init__(self, breed, speed):
        self.is_walked= False

    def walk(self):
        print(f'dog {self.name} walks')
        self.is_walked = True

class DogSpike(Dog):
    name = 'Spike'

class DogMike(Dog):
    name='Mike'

my_dog=DogSpike()
friends_dog=DogMike()