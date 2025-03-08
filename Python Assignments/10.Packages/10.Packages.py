#Packages.

class ClassOne:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Hello from Degree Final Year,", self.name)
class ClassTwo:
    def __init__(self, age):
        self.age = age
    def show_age(self):
        print("Age", self.age)
ClassOne("Prasanna").display()
ClassTwo(20).show_age()


