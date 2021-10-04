# https://www.youtube.com/watch?v=vRVVyl9uaZc

# We create a class with three people in it
# person 2 and 3 are identical in terms of data but they do not equal
class Person:
    # Typehints
    name:str
    job:str
    age:int
    
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
        
person1 = Person("Geralt","Witcher",30)
person2 = Person("Yennefer","Sorceress",25)
person3 = Person("Yennefer","Sorceress",25)

print(id(person2)) # Different IDs
print(id(person3))
print(person1.name)
print(person3==person2) #False even though they contain the same data


# We try the same with data class
# Import dataclass decorator and add it to the person class
from dataclasses import dataclass, field
#field is for sorting

@dataclass(order=True) 
# order = True necessary if we want to do < > operations
# frozen = True if we want to make it read-only
class Person:
    sort_index: int = field(init=False, repr=False) 
    # necessary to have sort_index if we want to do < > operations
    # init=False to not initialize it
    # repr=False to let the dataclass know that sort_index should not be a part of the string representation
    
    name:str
    job:str
    age:int
    strength: int=100 # strength with default value of 100
    
    # Using __post_init__method to use age as the sort index
    # __post_init__ is called after __init__ so the valeus have been set
    def __post_init__(self):
        self.sort_index = self.age # to sort by age
    #   self.sort_index = self.strength # to sort by strength
    
# Initialization not required because Person is a data class
        
person1 = Person("Geralt","Witcher",30,99)
person2 = Person("Yennefer","Sorceress",25)
person3 = Person("Yennefer","Sorceress",25)

print(id(person2)) # Different IDs
print(id(person3))
print(person1)
print(person1.name)
print(person3==person2) # True because they contain the same data
print(person1>person2) # True now that we have sorting