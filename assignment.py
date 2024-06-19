Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Arithmetic Operations#
result = 3+5*2-8/4

result
11.0
math = (9^2)-5
math
6
math = (9**2)-5
math
76
rem = 25%4
rem
1
#Variable Assignment & Operations#
x = 10
y = 3
x//y
3

def swap(var1,var2):
    if(len(str(var1))>=1 & len(str(var2))>=1):
        var3 = var1
        var1 = var2
        var2 = var3
        print(var1,var2)

        
swap(3,5)
5 3

def avgNumb(val1,val2,val3):
    fnavg = (val1+val2+val3)/3
    print(fnavg)

    
avgNumb(5,7,10)
7.333333333333333
#String Operations#
'Hello' + ' ' + 'World!'
'Hello World!'
print("abc" * (3//len("abc") + 1))
abcabc
print("abc" * (3//len("abc") + 1))
abcabc
print("abc" * (3//len("abc") + 3))
abcabcabcabc

s = "Python"
print(s[:3])
Pyt
#String Operations#
#Logical Operations#

a = 5
b = 10
if(a<b & a>0):
    print("A is less than B & A is  greater than 0")
else:
    print("A might be greater than B or less than 0")

    
A might be greater than B or less than 0

def evennum(num):
    validate = num%2
    if(validate == 0):
        print("Even Number")
    else:
        print("Not an Even Number")

        
evennum(3)
Not an Even Number
evennum(8)
Even Number
#Comparison Operations#
True
True
strinS = s
strinPy = "Python"
strinS = "s"
if(strinS != strinPy):
    print(strinS+" is not equal to"+strinPy)
else:
    print(strinS+" is equal to"+strinPy)

    
s is not equal toPython
>>> x = 8
>>> y = 4
>>> multiple = x%y
>>> if(multiple == 0):
...     print(str(x)+ " IS a multiple of "+str(y))
... else:
...     print(str(x)+" Is not a multiple of "+str(y))
... 
...     
8 IS a multiple of 4
>>> #List Operations#
>>> listadd = [1,2,3] + [4,5]
>>> listadd
[1, 2, 3, 4, 5]
>>> lst = [10,20,30,40]
>>> lst[1]
20
>>> lst = [1,2,3,4]
>>> lst.append(50)
>>> lst
[1, 2, 3, 4, 50]
>>> d = {'a':1, 'b':2, 'c':3}
>>> d['b']
2

>>> d['d'] = 4
>>> d
{'b': 2, 'd': 4, 'a': 1, 'c': 3}
>>> 

>>> verify = 'none'
>>> for val in d:
	if d.keys() == 'e':
		break
		print("There exists Key E in the dicitionary")
	else:
		break
		print("Key E does not exist in the dictionary")

		
>>> #Type Conversion#
>>> int('123') + float('4.56')
127.56
>>> str(5)
'5'
>>> s = "3.14"
>>> float(s)
3.14
>>> #Simple Assignment#
>>> answer = 42
>>> x = 10
>>> y = 20
>>> def swap(a,b):
	z = a
	a = b
	b = z
	print(a,b)

	
>>> swap(x,y)
20 10
>>> greeting = "Hello, World!"
>>> greeting
'Hello, World!'
>>> #Multiple Assignments#
>>> a = 3
>>> b = 4
>>> c = 5
>>> a = 3, b = 4, c = 5
SyntaxError: can't assign to literal
>>> a,b,c = 3,4,5
>>> p = q = r = 100
>>> q
100
>>> #Updating Variables#

>>> #Updating Variables#
>>> counter = 0
>>> counter += 1
>>> counter
1
>>> total = 50
>>> total -=15
>>> total
35
>>> balance = 1000
>>> balance *=2
>>> balance
2000
>>> #String Assignment#
>>> alphabet = str('abcde')
>>> alphabet
'abcde'
>>> name = 'Alice'
>>> name = 'Bob'
>>> name
'Bob'
>>> good = "Good"
>>> morning = "Morning"
>>> greeting = good+' '+morning
>>> greeting
'Good Morning'
>>> #List Assignment#
>>> 
>>> numbers = [1,2,3,4,5]
>>> fruits = ["apple","banana","cherry"]
>>> colors = ["red","blue","green"]
>>> colors.insert(1,"yellow")
>>> colors
['red', 'yellow', 'blue', 'green']
>>> #Dictionary Assignment#
>>> person = {"name":"John", "age":30}
>>> person
{'name': 'John', 'age': 30}
>>> inventory = {"apples":10,"bananas":20,"oranges":15}
>>> inventory
{'bananas': 20, 'apples': 10, 'oranges': 15}
>>> scores = {"math":90,"sciences":85}
>>> scores["english"]= 88
>>> scores
{'english': 88, 'math': 90, 'sciences': 85}
>>> #Tuple Assignments#
>>> coordinates = (1,2,3)
>>> person_info = ("Alice",25)
>>> person_info
('Alice', 25)
>>> dimensions = (1920,1080)
>>> width = dimensions[0]
>>> height = dimensions[1]
>>> width
1920
>>> height
1080
>>> #Casting Assignment#
>>> num = int("123")
>>> num
123
>>> float_num = float("45.67")
>>> float_num
45.67
>>> x = 5.89
>>> int_part = int(x)
>>> int_part
5
>>> #Boolean Assignment#
>>> is_active = True
>>> if 5>3:
	has_access = True
	print(has_access)

	
True
>>> a = 10
>>> b = 20
>>> if a==b:
	are_equal = True
else:
	are_equal = False

	
>>> print(are_equal)
False
>>> #None Type Assignment#
>>> unknown = None
>>> result = None
>>> result = 100
>>> result
100
>>> placeholder = None
>>> if placeholder is None:
	is_None = "It's a none type assignment"

	
>>> if placeholder is None:
	is_None = "It's a none type assignment"

	
>>> if placeholder is None:
	is_None = "It's a none type assignment"
else:
	is_None = "It's a none type assignment"

	
>>> print(is_None)
It's a none type assignment
>>> #Basic Arithmetic#
>>> result = 15 + 4
>>> result
19
>>> val = 9 // 2
>>> val
4
>>> valq = 9 / 2
>>> valq
4.5
>>> rem = 23 % 5
>>> rem
3
>>> #Type Conversion#
>>> conv = 45
>>> new_conv = float(45)
>>> new_conv
45.0
>>> num = 3.14159
>>> new_num = int(num)
>>> new_num
3
>>> int(4.7)
4
>>> "Hello "+"World"
'Hello World'
>>> s = "Python"
>>> s[:3]
'Pyt'
>>> s = "Hi"
>>> s * 3
'HiHiHi'
>>> #String Methods#
>>> s = "   hello world  "
>>> s.lstrip()
'hello world  '
>>> s.rstrip()
'   hello world'
>>> stg = "Python Programming"
>>> stg.upper()
'PYTHON PROGRAMMING'
>>> s = "hello"
>>> s.replace("ll","pp")
'heppo'
>>> #Boolean#
>>> True
True
>>> False
False
>>> False
False
>>> False
False
>>> a = 5
>>> b = 10
>>> if a != b:
	print("A is not equal to B")
else:
	print("A is equal to B")

	
A is not equal to B
>>> #Basic List Operations#
>>> ele = [1,2,3,4,5]
>>> ele[0]
1
>>> ele[3] = 10
>>> ele
[1, 2, 3, 10, 5]
>>> ele = [1,2,3,4,5]
>>> ele[0]
1
>>> ele[2] = 10
>>> ele
[1, 2, 10, 4, 5]
>>> #List Method#
>>> ele.append(6)
>>> ele
[1, 2, 10, 4, 5, 6]
>>> ele2 = (7,8,9)
>>> ele.extend(ele2)
>>> ele
[1, 2, 10, 4, 5, 6, 7, 8, 9]
>>> ele.insert(0,0)
>>> ele
[0, 1, 2, 10, 4, 5, 6, 7, 8, 9]
