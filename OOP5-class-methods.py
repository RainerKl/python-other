# Object Orineted Programming - Class methods


class Person:
    number_of_people = 0 # Class attribute - not inside any method, not specific to instance
                         # Values put here apply to all Persons
    GRAVITY = -9.8       # Better than putting the constant outside of teh class
                         # It is now transportable
    
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod # decorator for a class method
                 # the method is not going to act on behalf of any one instance
                 # class methods don't have access to any instance
    def number_of_people_(cls): # cls - acting on the class
                                # also added _ to separate it from the attribute with same name
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person("Tim")
p2 = Person("Jill")

print(Person.number_of_people_())