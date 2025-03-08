#1.Creating a default constructor,one argument,two argument constructions.

class MyClass:
    def __init__(self, a1=None, a2=None):
        if a1 is None and a2 is None:
            print("This is a Default Constructor")
        elif a2 is None:
            print(f"First Argument: {a1}")
        else:
            print(f"Second Argument: {a1}, {a2}")

obj1 = MyClass()
obj2 = MyClass("Prasanna")
obj3 = MyClass("Prasanna", 20)


#2.Calling constructors of super class from a child class.

class Parent:
    def __init__(self, a1=None):
        if a1 is None:
            print("Default Parent Constructor")
        else:
            print(f"First Parent Argument: {a1}")
class Child(Parent):
    def __init__(self, a1=None):
        if a1 is None:
            super().__init__()
            print("Default Child Constructor")
        else:
            super().__init__(a1)
            print(f"Child First Argument: {a1}")
obj1 = Child()
obj2 = Child("Welcome")


#3.Applying public,private and access modifiers to the constructors.

class MyClass:
    def __init__(self):  
        print("This is a Public Constructor.")
    def pro_con(self):  
        print("This is a Protected Constructor")
    def pri_con(self):  
        print("This is a Private Constructor.")
    def apri_con(self):
        self.pri_con()  
obj = MyClass()
obj.pro_con()  
obj.apri_con()  


#4.Attributes of a Constructors.

class Solution:
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
    def display(self):  
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
obj = Solution("Prasanna", 20)  
obj.display()  














