# Object Oriented Programming

# Let's create a class that we can call from aywhere
# Static method
# These methods do not have access to an instance
# They don't change anything

class Math:
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    @staticmethod
    def pr():
        print("run")
    

print(Math.add5(5)) # returns 10
print(Math.add10(1)) # returns 11

Math.pr()