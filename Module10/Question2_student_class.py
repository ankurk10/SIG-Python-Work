print("Ankur Kumar Kushwaha   1900300100034")

class Student:
    def __init__(self, roll,name):
        self.roll=roll
        self.name=name

    def display(self):
        print(f"Name = {self.name}\nRoll No = {self.roll}\nAge = {self.age}\nMarks = {self.marks}")

    def setAge(self):
        self.age=int(input("Enter your age : "))

    def setMarks(self):
        self.marks=int(input("Enter your marks : "))

student1 = Student(34, "Ankur")
student1.setAge()
student1.setMarks()
student1.display()