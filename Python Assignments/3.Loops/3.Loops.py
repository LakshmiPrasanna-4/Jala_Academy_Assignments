#1.Bright IT using for loop

a="BRIGHT IT"
for i in range(1,11,1):
    print(i,a)

#2.Print 1 to 20 using while loop.

n=20
i=1
while i<=20:
    print(i)
    i=i+1

    
#3.Equal and not equal operator.

a=int(input())
b=int(input())
print(a==b)
print(a!=b)


#4.Even and Odd Numbers

n=int(input())
print('Even Numbers')
for i in range(1,n+1):
    if i%2==0:
        print(i)
print('Odd Numbers')
for i in range(n+1):
    if i%2!=0:
        print(i)

#5.Largest among 3 numbers.

a=10
b=20
c=30
if a>b and a>c:
    print(a,'a is greater')
elif b>c:
    print(b,'b is greater')
else:
    print(c,'c is greater')
    


#6.Even Numbers between 10 and 20 using while.

a=10
b=20
while(a<=b):
    if a%2==0:
        print(a)
    a=a+1


#7.Print 1 to 10 numbers using do while loop.

i=1
do:
    print(i)
    i=i+1
while(i<=10)


#8.Armstrong Number or not.

n=int(input('Enter a Number:'))
t=n
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(s==t):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')


#9.Prime Number or not.

n=int(input('Enter a Number:'))
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if(c==2):
    print('Prime Number')
else:
    print('Not a Prime Number')



#10.Palindrome Number or not.

n=int(input('Enter a Number:'))
t=n
s=0
while n!=0:
    r=n%10
    s=(s*10)+r
    n=n//10
if(s==t):
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')
            


#11.Even or Odd

n=int(input('Enter a Number:'))
if n%2==0:
    print('Even Number')
else:
    print('Odd Number')



#12.Male or Female

g=input('Enter a Character:')
if g=='M':
    print('Male')
elif g=='F':
    print('Female')
else:
    print('Invalid')
























   
