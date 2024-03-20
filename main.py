class Dog:
    pass
class DogSpike(Dog):
    name = 'Spike'
    def __init__(self):
        self. is_walked = False
    def walk(self):
        print('Dog walked')
        self. is_walked = True

my_dog = DogSpike()
print(my_dog.name)#'Spike'
print(my_dog.is_walked) #False
my_dog.walk()
print(my_dog.is_walked)