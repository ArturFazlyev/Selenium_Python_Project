import jsonpickle

class Student(object):
    def __init__(self, rollNumber, name, marks):
        self.rollNumber = rollNumber
        self.name = name
        self.marks = marks


class Marks(object):
    def __init__(self, english, geometry):
        self.english = english
        self.geometry = geometry


marks = Marks(82, 74)
student = Student(1, "Emma", marks)

studentJson = jsonpickle.encode(student)
print(studentJson)

studentObject = jsonpickle.decode(studentJson)
print(studentObject.rollNumber)
