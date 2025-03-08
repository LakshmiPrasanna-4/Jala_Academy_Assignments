#1.Arithmetic Exceptions without Exxception Handling.

ar = 10 / 0
print("This is an Example of Exception Handling.",ar)


#2.Handling the Exception using the except block.

try:
    ar = 10 / 0
    print(ar)
except Exception as e:
    print("An error occurred:", e)


#3.Throwing an exception.

def throw_exception():
    raise ZeroDivisionError("Division by zero error")

class Solution:
    def __init__(self):
        throw_exception()
Solution()


#4.Using Multiple except blocks.

try:
    a = int(input("Enter a 1st number: "))
    b = int(input("Enter a 2nd number: "))
    res = a / b
    print("Result:", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", e)


#5.Throwing an exception to print the message.

def Solution():
    raise Exception("This is my Sample Program.")
Solution()


#6.Creating own Exception.

class Solution(Exception):
    def __init__(self, message):
        super().__init__(message)

def checking(value):
    if value < 0:
        raise Solution("Negative values are not allowed.")
    if value==0:
        raise Solution("Zero is not allowed.")
n=int(input('Enter a value:'))
checking(n)


#7.Finally Block.

try:
    a = int(input("Enter a 1st number: "))
    b = int(input("Enter a 2nd number: "))
    res = a//b
    print("Result:", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
finally:
    print("Execution completed.")


#8.Generating Arithmetic Exception.

a=int(input('Enter a 1st Value:'))
b=int(input('Enter a 2nd Value:'))
if b==0:
    print('ZeroDivisionException')
else:
    res=a//b
    print(res)

#9.File not Found Exception Error.

a=input('Enter name of the file:')
f=open("a", "r#Class not found Error.

folder=input('Enter a Folder:')
file=input('Enter a File:')
try:
    from folder import file
except Error:
    print("Error: Class not Found.")


#10.Class not found Error.

folder=input('Enter a Folder:')
file=input('Enter a File:')
try:
    from folder import file
except Error:
    print("Error: Class not Found.")




#11.IOE Exception.

a=input('Enter a file path:')
try:
    with open("a", "r") as f:
        res = f.read()
except OSError as e:
    print("IO Exception occurred:", e)


#12.No such Field Exception.

class Display:
    def __init__(self):
        a=input('Enter a Name:')
        self.name = "a"
obj=Display()
print(obj.age)


























    
