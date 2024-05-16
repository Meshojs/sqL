class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Woof!'

class Cat(Animal):
    def sound(self):
        return 'Meow!'

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())