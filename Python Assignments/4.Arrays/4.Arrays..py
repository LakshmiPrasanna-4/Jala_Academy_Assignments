#1.Adding Array integer values.

def arr(n):
    a=[]
    s=0
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s
n=int(input('Enter number of terms:'))
k=arr(n)
print(k)


#2.Average of array of integers.

def avg(n):
    a=[]
    s=0
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s//n
n=int(input('Enter a number of terms:'))
k=avg(n)
print(k)


#3.Index of an Element.

n=int(input('Enter number of terms:'))
a=[]
p=len(a)
for i in range(n):
    k=int(input())
    a.append(k)
m=int(input('Enter a number to know its index:'))
if m in a:
    print('Element Found',a[m-1])
else:
    print('Element not found')



#4.Finding specific value.

def spec(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    m=int(input('Enter a Specific value:'))
    if m in a:
        return True
    else:
        return False
            
n=int(input('Enter number of terms:'))
k=spec(n)
if k==True:
    print('Has a Specific Value')
else:
    print('Does not contain specific value')



#5.Removing a specific element from an array.

def rem(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    m=int(input('Enter a specific element to remove'))
    a.remove(m)
    for i in a:
        print(i,end=' ')
n=int(input('Enter number of terms:'))
rem(n)


#6.Copying one array into another.

def cpy(n):
    a=[]
    b=[]
    for i in range(1,n+1):
        k=list(map(int,input().split()))
        a.append(k)
    for i in a:
        print(i,end=' ')
    print()
    c=a.copy();
    print("The copy array is:",c)
n=int(input('Enter number of terms:'))
cpy(n)



#7.Inserting an element at a specific position.

def ins(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    p=int(input('Enter position to insert an element'))
    o=int(input('Enter an element to insert'))
    i=a.insert(p,o)
    for i in a:
        print(i,end=' ')
n=int(input('Enter number of terms:'))
ins(n)



#8.Maximum and Minimum value from an array.

def mm(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    maxx=a[0]
    minn=a[0]
    for i in a:
        if i>maxx:
            maxx=i
        if i<minn:
            minn=i
    print('Maximum value ',maxx)
    print('Minimum value ',minn)
n=int(input('Enter number of terms:'))
mm(n)



#9.Reversing an array of integer values.

def res(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        print(a[::-1],end=' ')
        break
n=int(input('Enter number of terms:'))
res(n)

#10.Finding duplicates values in an array.

def dup(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        if a.count(i)>1:
            print(i)
            break
n=int(input('Enter number of terms:'))
dup(n)


#11.Common values between two arrays.

def com(a,b):
    return list(set(a) & set(b))

a = [1, 2, 3, 4, 5]
b= [3, 4, 5, 6, 7]
print("Common values:",com(a,b))


#12.Removing duplicate values from an array.

def dup(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        if a.count(i)>1:
            a.remove(i)
            a.remove(i)
    print(a)
n=int(input('Enter number of terms:'))
dup(n)



#13.Finding second largest element in an array.

def sm(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    maxx=a[0]
    for i in a:
        if i>maxx:
            maxx=i
    a.remove(maxx)
    smaxx=a[0]
    for i in a:
        if i>smaxx:
            smaxx=i
    print('Second Largest Number',smaxx)            
n=int(input('Enter number of terms:'))
sm(n)


#14.Finding second smallest element in an array.

def sm(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    minn=a[0]
    for i in a:
        if i<minn:
            minn=i
    a.remove(minn)
    sminn=a[0]
    for i in a:
        if i<sminn:
            sminn=i
    print('Second Largest Number',sminn)            
n=int(input('Enter number of terms:'))
sm(n)


#15.Finding even and odd numbers in an array.

def eo(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    print('The even numbers are:')
    for i in a:
        if i%2==0:
            print(i)
    print('The odd numbers are:')
    for i in a:
        if i%2!=0:
            print(i)

n=int(input('Enter number of terms:'))
eo(n)

#16.Difference between largest and smallest value.

def ls(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    maxx=a[0]
    minn=a[0]
    for i in a:
        if i>maxx:
            maxx=i
        if i<minn:
            minn=i
    print(maxx-minn)
n=int(input('Enter number of terms:'))
ls(n)


#17.Verify to check if an array contains specific element 12 and 23.

def ce(a,e1,e2):
    return e1 in a and e2 in a

a = [12, 23, 34, 45]
print("Contains 12 and 23:", ce(a, 12, 23))

#18.Removing duplicate elements and return new array.

def dup(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        if a.count(i)>1:
            a.remove(i)
            a.remove(i)
    print(a)
n=int(input('Enter number of terms:'))
dup(n)























































