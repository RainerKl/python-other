class Person:
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

print(id(person2))
print(id(person3))
print(person1.name)
print(person3==person2)