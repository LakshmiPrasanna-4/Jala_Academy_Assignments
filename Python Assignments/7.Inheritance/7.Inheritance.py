#Inheritance

class A():  
    def display(d):
        print("Display the class inside A")   
class B (A): 
    def print(pt):
        print("B is the class inside A")    
class C (B): 
    def show(self):
        print("C is a class inside B ")         

a = A()
a.display()
b= B()
b.print()
c = C()   
c.show()
