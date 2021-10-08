# Object Oriented Programming - file 2

# We want to a grading model for a school.
# Two classes and their interaction

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students =[] # A list of students initialized as a blank list
                          # We made an attribute and didnt assignt it to the arguments
                          
    # Method that allows us to add a student to the list
    # If we have not reached max_students, add student to the list
    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True # to indicate a successful addition
        return False # to indicate a failed addition
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)
    
    
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 19, 75)
    s3 = Student("Jill", 19, 65)
    
    course = Course("Science",2)
    course.add_student(s1) # returns True
    course.add_student(s2) # returns True
    
    print(course.students[1].grade) # returns 75
    
print(course.get_average_grade()) # returns 85.0