class Dog:
    pass
class DogSpike(Dog):
    name = 'Spike'
    def __init__(self):
        self. is_tired = False
    def tired(self):
        print('Dog tired')
        self. is_tired = True

my_dog = DogSpike()
print(my_dog.name)#'Spike'
print(my_dog.is_tired) #False
my_dog.tired()
print(my_dog.is_tired)