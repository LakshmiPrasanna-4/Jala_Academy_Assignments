#1.Arithmetic Operators.

def ar(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
a=10
b=20
k=ar(a,b)
print(k)



#2.Increment and Decrement

#Increment
'''
a=10
s=a+1
print(s)

'''

#Decrement
'''
a=10
s=a-1
print(s)

'''

#3.Equal numbers or not

a=int(input())
b=int(input())
if a==b:
    print("Equal")
else:
    print("Not Equal")


#4.Relational Operators.

a=int(input())
if a>0:
    print('Greater than 0')
elif a<0:
    print('Less than 0')
elif a>=0:
    print('Greater than or equal to 0')
elif a<=0:
    print('Less than or equal to 0')
else:
    print('Invalid')
    

#5.Smaller and Larger Number.

#Larger Number
'''
a=int(input())
b=int(input())
if a>b:
    print(a,'a is greater')
else:
    print(b,'b is greater')

'''

#Smaller Number
'''
a=int(input())
b=int(input())
if a<b:
    print(a,'a is smaller')
else:
    print(b,'b is smaller')
'''


























