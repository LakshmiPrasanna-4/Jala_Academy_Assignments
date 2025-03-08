#1.Creating an abstract and non abstract methods.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        print("This is a Square of area:") 
class S(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):  
        return self.side ** 2 
s = S(5)
s.describe()
print(s.area())

#2.Create a subclass from an abstract class.

from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method(self):
        return f"Value: {self.value}"
class SubClass(AbstractClass):
    def __init__(self, value, extra_value):
        super().__init__(value)
        self.extra_value = extra_value
    def abstract_method(self):
        return f"Abstract method called."
sub_obj= SubClass(10, "extra")
print(sub_obj.non_abstract_method())
print(sub_obj.abstract_method())
try:
    abstract_object = AbstractClass(5)
except TypeError as e:
    print(f"Error: {e}")


#3.Creating an instance for the child class in child class and call abstract methods.

from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method_1(self):
        pass
    @abstractmethod
    def abstract_method_2(self):
        pass

class ChildClass(AbstractClass):
    def abstract_method_1(self):        
        return "ChildClass: Implementation of abstract_method_1"
    def abstract_method_2(self):
        return "ChildClass: Implementation of abstract_method_2"
    def call_abstract_methods(self):
        return self.abstract_method_1(), self.abstract_method_2()
child_instance = ChildClass()
res1, res2 = child_instance.call_abstract_methods()
print(res1)
print(res2)



#4.Create an instance for the child class in child class and call non abstract method.

from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method_1(self):
        return "AbstractClass: Non-abstract method 1"
    def non_abstract_method_2(self):
        return "AbstractClass: Non-abstract method 2"
class ChildClass(AbstractClass):
    def abstract_method(self):
        return "ChildClass: Implementation of abstract_method"
    def non_abstract_methods(self):
        return self.non_abstract_method_1(), self.non_abstract_method_2()
child_instance = ChildClass()
res1, res2 = child_instance.non_abstract_methods()
print(res1)
print(res2)





















