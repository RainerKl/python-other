# Some Object Oriented Programming
# https://www.youtube.com/watch?v=JeznW_7DlB0

def hello():
    print("hello")

x=1

# we see that everything in python is an object of some type of class
print(type(x)) # returns <class 'int'>
print(type(hello)) # returns <class 'function'>
# these here are called built-in types
# class defines the way the objects can interact with other things in the program

# Method upper() acting on an object string
string = "hello"
print(string.upper()) # returns HELLO

# Defining the class
class Dog: # Convention is to start with an upper-case letter
    def __init__(self, name): # allows us to instantiate the object right as it is created
        self.name = name      # whenever we create a new Dog() instance, this method will be called
                              # and it will pass any arguments that we put in
                              # e.g. can be used for giving the dog a name
                              # we have created an attribute of the class Dog() which is name
    
    # self - any time a method is called, the reference to the Dog object is passed
    #       so we can access attributes that are specific to each dog
    
    def bark(self): # defining a method
        print("bark")
    
    def add_one(self, x): # defining a method
        return x + 1
d = Dog("Tim") #returns Tim
d.bark() # returns bark        
# Creating a new instance of the class Dog
print(type(d)) # returns <class '__main__.Dog'>
               # the __main__ tells us what module the class was defined in
               # in this case the default __main__
               # this is an object of the class Dog

print(type(d))

print(d.add_one(5)) # returns 6


d2 = Dog("Bill") #returns Tim

print(d.name) # returns Tim
print(d2.name) # returns Bill



class Cat: 
    # the first argument is always self because we need to pass the invisible Cat object itself
    # so that we know which cat object we are accessing
    def __init__(self, name, age): 
        self.name = name # initializing object with a name
        self.age = age # initializing object with an age
    def get_name(self):
        return self.name 
    def get_age(self):
        return self.age 
    def set_age(self, age):
        self.age = age # changing the age
    
c = Cat("Whiskers", 3) 
print(c.get_name()) # returns Whiskers
print(c.get_age()) # returns 3

c = Cat("Whiskers", 3) 

# We can modify and access these different attributes from methods inside our class
# This allows us to access data stored within a specific object
c.set_age(5)
print(c.get_age()) # returns 5