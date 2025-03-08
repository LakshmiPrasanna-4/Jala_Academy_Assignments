#1.Define a static variable and access that through a class.

class name:
    s='Prasanna'
    def __init__(self):
        print(name.s)
obj=name()


#2.Defining a static variable and access that through an instance.

class accessThroughInstance():
    n=int(input('Enter a number:'))
    def __init__(self):
        if self.n%2==0:
            print(f'even number')
        else:
            print('odd number')
obj=accessThroughInstance()


#3.Defining a static variable and change within the instance.

class MyClass:
    SV= "I am a static variable"
    def __init__(self, value):
        self.IV = value  
    def modify(self, new_value):
        MyClass.SV = new_value
obj1 = MyClass("Instance 1")
obj1.modify("Changed from instance") 
print(MyClass.SV)  


#4.Define a static variable and changed within a class

class MyClass:
    static = "I am a Student"
    @classmethod
    def modify(cls, new_value):
        cls.static = new_value
print(MyClass.static)  
MyClass.modify("Studying in Aditya Degree College")
print(MyClass.static)
  

 
