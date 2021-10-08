# Object Orineted Programming - Class attributes
# Useful for constants e.g. gravity
# Classes should not need anything outside of their class deifinition

class Person:
    number_of_people = 0 # Class attribute - not inside any method, not specific to instance
                         # Values put here apply to all Persons
    GRAVITY = -9.8       # Better than putting the constant outside of teh class
                         # It is now transportable

    
    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1
        
p1 = Person("Tim")
p2 = Person("Jill")


print(p1.number_of_people)
print(Person.number_of_people)