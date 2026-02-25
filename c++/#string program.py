#string problem
#1. to check if  a string is a palindrome
#using slicing
'''a=input("Enter the strings:")
if a==a[::-1]:
    print("palindrome string")
else:
    print("It is not palindrome")
#using loop
b=''
for i in a:
    b=i+b
if b==a:
    print("Palindrome")
else:
    print("Not palindrome")
#using reverse
c=''.join(reversed(a))
if c==a:
    print('Yes')
else:
    print('No')'''
    
'''#2.To check whether the number is symmetrical
#number is symmetrical if the first half is equal to the second half
a=input("enter the string:")
#using slicing
b=len(a)//2
if len(a)%2==0:
    if a[:b]==a[b:][::-1]:
        print("It is symmetric")
    else:
        print("It is not symmetric")
else:
    if a[:b]==a[b+1:]:
        print("It is symmetric")
    else:
        print("It is not symmetric")'''
        
'''#3. reverse word in a goven string
a=input("enter a string:")
b=''
for i in a:
    b=i+b
print(b)
#using join
#it will reverse the order of the whole sentence
c=' '.join(a.split()[::-1])
print(c)'''

'''#4. ways to remove i'th character from the string
a=input("Enter the string:")
b=input("enter the i'th term you want to remove:")
c=a.replace(b,'')
print(c)
#using loop
d=''
for i in a:
    if i!=b:
        d=d+i
print(d)
#using list comprehension
d=' '.join([c for c in a if c!=b])
print(d)
#using filter 
d=''.join(filter(lambda c: c!=b,a))
print(d)'''

'''#5. Check for the substring in string
a=input("Enter the string:")
b=input("Enter the substring:")
if b in a:
    print('Yes')
else:
    print('No')
#using split()
c=a.split()
if b in c:
    print("yes yes")
else:
    print("NO")'''
    
'''#6. Words frequency in String Shorthands
#using collection
from collections import Counter
a=input("enter the words").split()
b=Counter(a)
print(b)
#using list comprehension
c=Counter([word for word in a])
print(c)
#using map
d=Counter(map(str,a))
print(d)'''

'''#7. convert snakecase to pascalcase
#using title
a=input('Enter the strings:')
b=a.replace('_',' ').title().replace(' ','')
print(b)
#using split()
c=''.join(word.capitalize() for word in a.split('_'))
print(c)
#'''

import mathematics
print(add(9,5))
print(substract(9,5))
print(multiply(9,5))
print(divide(9,5))
