# Example showing how class and object hierarchy works in Python

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printName()


# Define child class with void implementation
class Student(Person):
    pass


stu = Student("Vineet", "Badoni")
stu.printName()


# Example showing how class and object hierarchy works in Python

# Overriding method

class Student(Person):
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__()function.

    def __init__(self, fname, lname, graduationYear):
        self.firstname = lname
        self.lastname = fname
        self.graduationYear = graduationYear

    def printName(self):
        print(
            "I am a student and I am known by firstname as {} and lastname as {}".format(self.firstname, self.lastname))

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


stu = Student("Vineet", "Badoni","2021")
stu.printName()
stu.welcome()


# Super function
class Teacher(Person):
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__()function.

    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def printName(self):
        print(
            "I am a Teacher and I am known by firstname as {} and lastname as {}. I used my parent's init"
            " super() . ROFL :)".format(self.firstname, self.lastname))


stu = Teacher("Vineet", "Badoni")
stu.printName()
