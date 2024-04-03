class Dog:
    pass
class DogRex(Dog):
    name = 'Rex'
    def __init__(self):
        self. is_hungry = False
    def hungry(self):
        print('Dog hungry')
        self. is_hungry = True

my_dog = DogRex()
print(my_dog.name)#'Spike'
print(my_dog.is_hungry) #False
my_dog.hungry()
print(my_dog.is_hungry)