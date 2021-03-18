# We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?

class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()
