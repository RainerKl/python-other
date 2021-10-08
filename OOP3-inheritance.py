# Object Oriented Programming - file 3

# A study of inheritance
# We want to define a class of dogs and a class of cats, where the only difference is speak method

class Cat0:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Meow")
        
class Dog0:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Bark")
        
# Seems repetitive
# Let's use inheritance so that the Dogs and Cats can inherit something from an upper-level class
# We define a Pet class that contains functionality that we want Dogs and Cats to contain

class Pet: # super class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say")

class Cat(Pet): # Inheriting from the upper-level class Pet
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
        
class Dog(Pet): 
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass
        
p = Pet("Tim",19) # returns I am Tim and I am 19 years old
p.show()

c = Cat("Bill",34, "brown") # returns I am Bill and I am 34 years old
c.show() # returns I am Jill and I am 25 years old

d = Dog("Jill",25)
d.show()

p.speak() # returns I don't know what to say
c.speak() # returns Meow
# Cat.speak() overrides Pet.speak()
d.speak() # returns Bark

f = Fish("Bubbles",1)
f.speak() # returns I don't know what to say

c.show()