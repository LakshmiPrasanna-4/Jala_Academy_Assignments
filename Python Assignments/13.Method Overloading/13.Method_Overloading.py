#1.Methods with same name but with different parameters.

class Solution:
    def show(self, a, b=None):  
        if b is None:
            print(f"One Parameter: {a}")
        else:
            print(f"Two Parameters: {a}, {b}")
obj = Solution()
obj.show(25)    
obj.show(80,65)  


#2.Two methods with same name but different parameters with different datatypes.

class Solution:
    def show(self, *args):  
        if len(args) == 1:
            print(f"One Parameter: {args[0]} (Type: {type(args[0]).__name__})")
        elif len(args) == 2:
            print(f"Two Parameters: {args[0]} (Type: {type(args[0]).__name__}), {args[1]} (Type: {type(args[1]).__name__})")
        else:
            print("Invalid number of arguments")

obj = Solution()
obj.show(76)        
obj.show("Prasanna", 20)  
obj.show(8.765, True)  


#3.Methods with same name and same parameters.

class Solution:
    def display(self, a, b):  
        if isinstance(a,int) and isinstance(b,int):
            print(f"Integer Method: {a} and {b}")
        else:
            print(f"String Method: {a} and {b}")
obj = Solution()
obj.display(10, 20)  
obj.display("Hello", "World")  

