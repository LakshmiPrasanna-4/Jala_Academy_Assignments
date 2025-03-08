#1.Creatinga a private fields.

class name():
    def __init__(self):
        self.__nameofst1='My name is Lakshmi Prasanna'
    def private_c(self):
        print('This is private class')
    def access_private(self):
        print(self.__nameofst1)

class roll(name):
    def rno(self):
        self.rollOfSt="My roll no is 18"
        print(self.rollOfSt)
        self.rollofSt2="My friend roll no is 12"
        print(self.rollofSt2)
    def access_parent_class(self):
        try:
            print(self.__nameofst1)
            print(self.__nameofst2)
        except AttributeError:
            print('parent class cannot be accessed')
obj=roll()
obj.rno()
obj.access_private()
obj.access_parent_class()
obj.private_c()



#2.Creating a main class.

from subclasses import _protected
class naming():
    def __init__(self):
        access=_protected()
        print(access._message)
obj=naming()



#2.1Creating a subclass.

class _protected():
    def __init__(self):
        self._message='welcome to vs code'
        print(self._message)
obj=_protected()


#3.Cretaing a Public class.

class ceatingPublicClass():
    def __init__(self):
        self.x=3.14
        print(self.x)
        print('its a public class')
obj=ceatingPublicClass()


#3.1Accessing a public class.

from public import ceatingPublicClass
class inAnotherFile():
    acess=ceatingPublicClass()
    print(acess.x)
obj=inAnotherFile()
























