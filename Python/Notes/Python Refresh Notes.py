# Last updated: Tue, March 16, 2021 - 12:21

PROGRAM
#########################################################################################
'''
#!/usr/bin/env python3
'''
# shebang line(#!...) is needed in the file and only if it's meant to be run as executable
# And if you have python 2 and you want the running to be python 3
# Can double click it but you need to do the code below first
$ chmod +x newFile.py
# Change the mode to executable file

# But seems like Python 3 in Windows does not require this anymore, can type the file name
# and it will execute it

BASICS
#########################################################################################
PRINT
=====
# Python2
print "Hello"

# Python3
print("Hello")

name = 'John'
print('Hello', name, end('!'))
>> Hello John!

print("Hello", end=" ")
print("there!")
# Output: Hello there!

# SEP function
print(30, 11, 2020, sep="-")
# Output: 30-11-2020

for i in range(5):
	print(i, end=" ")
>> 0 1 2 3 4

ESCAPE CHARACTER
=====
# To insert illegal character by using backslash \

'''
\' - Single Quote
\\ - Backslash
\n - New line
\t - tab
\r - Carriage return
\b - backspace
\f - form feed
\ooo - Octal value
\xhh - Hex value
'''

ANOTHER WAY TO INSERT ILLEGAL CHAR WITHOUT ESCAPE KEY
=====
# USING print(r'bla bla bla')

# To escape "'"
print('I don\'t think so...')

# Next line
print("\nThis is next line")

# Raw String
print(r'C:\Desktop\nutellaFolder')

BASIC ARGUMENT SPECIFIERS
=====
%s - String (or any object with a String representation, like numbers)
%d - Integers
%0<number of digits>d - Floating point numbers with a fixed amount of 0 to the left of the number.
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

# Align the string in the middle when printing
print('|{:^24s}|'.format("MyString"))
# Output: |        MyString        |

print("MyString".center(24, "-")
# Output: --------MyString--------

print('|' + "MyString".center(24) + '|')
# Output: |        MyString        |

# Left justify
'hi'.ljust(10)
# 'hi        '

'{0: <16} StackOverflow!'.format('Hi')
# 'Hi               StackOverflow!'

'{message: <{width}}'.format(message='Hi', width=16)
# 'Hi              '

#########################################################################################
EXPRESSIONS
=====
ORDER/PRECEDENCE:
()
**
*, /, //, %
+, -
==, !=, <=, >=, >, <
not
and
or
# left TO right

LOGICAL OPERATORS # For more detailed explanation, take a look at the `02-Operators.py` in this repo/Python
=====
COMPARISON: 
'''
>
>=
<
<=
==
!=
and
or
not
is [Use this in some ooccasion, == is normally for Mathematics]
is not
'''
# To be more specified
# is 	: literraly equal
# `=` 	: holding the same value

a = 6
if a == 5 or 6:
	print('hello') # hello

x = [1,2,3]
tmp = x
print(tmp is x) # Ouput: True

print(id(x))   # 2561080621696 <-- Memory address of the list pointing to
print(id(tmp)) # 2561080621696

# Let's see if we create another list and compare their address and values
y = [1,2,3]
print(tmp is y) # Output: False | Why? Because the 'is'keyword is used for literal meaning, in this case the address of the 'y' and the address of the 'tmp'

print(id(tmp))   # 2561080621696
print(id(y))     # 2561080612352

print(tmp == y) # Output: True  | Why? Because it just checked the values of the both list

COMPARING AMONG VARIABLES
=====
x = 5; y = 3; z = 8
print(x > y < z) # True

student_names = ['alpha','beta','gama','delta']
# using the is keyword:
if student_names is ['alpha','beta','gama','delta']:
    print('both the lists are the same')

# using the == operator
for student in student_names:
    if student == 'beta':
        print('There is a student named beta')

print(1 > '1')
>> TRACEBACK: TypeError

print(1 == '1')
>> False

IF, ELIF, ELSE
=====
if x == 5:
	print('It\'s a five')
elif x > 6: # NOTE: THERE IS NO 'else if' IN PYTHON
	print(' More than 6')
else:
	print('Something else')

print("even" if x % 2 == 0 else "odd")
>> odd

# Special features: To check if there is any value in the sequence
"""
# FALSE VALUES: 
    # False
    # None
    # Zero of any numeric type: 0, 0.00 (Other Negative or positive number will return True)
    # Empty sequence : '' [] ()
    # Empty mapping: {}
"""
x = None
if x:
    print(True)
else:
    print(False)
# False

TERNARY OPERATOR
=====
# [on_true] if [expression] else [on_false] 
min = a if a < b else b

# Python program to demonstrate ternary operator 
a, b = 10, 20
  
# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 
  
# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 

# Python program to demonstrate nested ternary operator 
a, b = 10, 20
  
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a") 

COMMENT
=====
# This is a comment

'''
Here lies comment or documentary
'''

TYPE CONVERSION / TYPE CASTING
=====
x = float(1)
>> x 
>> 1.0

x = str(x)
x = int(x) # Converting a string into a int
x = float(x)

ttl = int("2") + int("5")
>> 7

INPUT
=====
# Python3
x = input("Enter integer for x: ")
x = int(x)
# Python2
y = raw_input('> ')

TRY, EXCEPTION, FINALLY
=====
'''
try:
	# Try running some code
except:
	# Run this block of error occurs
	raise
else:
	# Run if no error in the block
finally:
	# This block will always be executed no matter what
'''

x = 'John'

try:
	x = int(x)
	print('Done converting')
except:
	print(x, "is not a number")
finally:
	print('Goodbye')
	quit() # <## completely exit the program

#########################################################################################
FUNCTION
=====
def add(x, y):
	return x + y

sum = add(2, 5)
print(sum)
>> 7

# Default value when the variable is not passed into
def welcome(name="user"):
    print(f"Hello {name}")

welcome("Steve") # Hello Steve
welcome() # Hello user

# Returning more than 1 value from a function
def convert(seconds):
	h = seconds // 3600
	m = (seconds - h*3600) // 60
	s = seconds - h*3600 - m*60
	return h, m, s

print(convert(5000))

HRS, MINS, SECS = convert(5000)
print(HRS, MINS, SECS)

# >> (1, 23, 20)
# >> 1 23 20

# Default value in the fuction
def welcome(name='user'):
    print('hello', name)
welcome() # Output: hello user

LEAP YEAR
=====
def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


FUNCTION WITH DIFFERENT POSITION OF THE KEYWORD PARAMETER
=====
def welcome(name, age, gender):
	print(f'Welcome {name} ({age} - {gender})')

welcome(gender='M', name='Steve', age=23)

FUNCTION WITH UNSPECIFIED NUMBER OF ARGUMENT [*args]
=====
# Reference: https://www.programiz.com/python-programming/args-and-kwargs
# *args = non keyword argument, no dictionary like parameter
# However, you can enum it
def checklist(*items): # Receiving a tuple of arguments
    # print tuple
    print(items) # ('milk', 'rice', 'bread', 'jam')
    
    for index, item in enumerate(items, 1): # 1 = starting with, it is optional, wihout it the number would start at 0
        print("Item", str(index) , ":", item.capitalize())
        '''
        Item 1 : Milk
        Item 2 : Rice
        Item 3 : Bread
        Item 4 : Jam
        '''

checklist('milk', 'rice', 'bread', 'jam') # Sending a tuple of arguments

# Example 2: without the use of list
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

adder(3,5)			# 8
adder(4,5,6,7)		# 22
adder(1,2,3,5,6)	# 17

FUNCTION WITH UNSPECIFIED NUMBER OF KEYWORD ARGUMENT [**kwargs]
=====
# Reference: https://www.programiz.com/python-programming/args-and-kwargs
# **kwargs = keyword argument, like it has dictionary

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

# Example 2
def message(**orderProd_amt):
    # Print out the dictionary
    print(orderProd_amt.items()) # dict_items([('orderProduct', 'Cookie'), ('amt', 13)])
    print(orderProd_amt)         # {'orderProduct': 'Cookie', 'amt': 13}

    for k, v in orderProd_amt.items():
        print(k,v)
    '''
    orderProduct Cookie
    amt 13
    '''
    # ERROR: ValueError: too many values to unpack (expected 2)
    # for k, v in orderProd_amt:
    #     print(k,v)

    print('I am buying', orderProd_amt["amt"], orderProd_amt["orderProduct"] + "(s) for you.")
	# I am buying 13 Cookie(s) for you.

message(orderProduct = "Cookie", amt = 13)
message(orderProduct = "Bread", amt = 5)

# MORE EXAMPLE
# Reference: https://youtu.be/9Os0o3wzS_I?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&t=881
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['History', 'CS']
info = {'name':'Jane', 'age':29}
student_info(courses, info)

"""
('History', 'CS')
{'name':'Jane', 'age':29}
"""

REPLACE A FUNCTION WITH ANOTHER FUNCTION
=====
def test(name):
    print(name) # Steve

def test2(name):
    print("".join(reversed(name))) # evetS

test = test2
test(name='Steve') # evetS

FUNCTION CAN BE USED AS AN ARGUMENT IN A FUNCTION
=====
def add(x,y):
	return x + y

def combine(func, x, y):
	return(func(x,y), func(x, y))

print(combine(add, 5, 10))

#########################################################################################
LAMBDAS
=====
'''
Reference:
https://realpython.com/python-lambda/
https://www.youtube.com/watch?v=goypZR_lQ7I
'''
def calc(f, x, y):
    return f(x, y)

calc(lambda x, y: x + y, 10, 20))
# NOTE that the lambda x, y: x+y is a function

Simple implementation
=====
(lambda x: x + 1)(2)
3

(lambda x, y: x + y)(2, 3)
5

Putting the LAMBDA Function into a variable
=====
add_one = lambda x: x + 1
add_one(2)
3

FILTER
=====
ls = [1, 2, 3, 4, 6, 10, 212, 23, 2]
hi = 23
lo = 2
print(list(filter(lambda x, l=lo, h=hi: l < x <= h, ls)))


FUNCTION IN JUST ONE LINE OF CODE
=====
c = lamdba: os.system('cls')
# c() will then clear the screen

#########################################################################################
MAP VS LIST COMPREHENSION
=====
# Using the lambda function to do for each of the element in the list
>>> list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
['Cat', 'Dog', 'Cow']
# The simpler way of doing the same thing is using list comprehension
>>> [x.capitalize() for x in ['cat', 'dog', 'cow']]
['Cat', 'Dog', 'Cow']

>>> list(map(lambda x: x+1, [1,2,3]))
[2,3,4]
>>> [x+1 for x in [1,2,3]]
[2,3,4]

list(map(len, ['John', 'Cena', 'Smith']))
[4,4,5]

ls = ["data-%03d.txt" % r for r in range(0, 3)]
ls = [f'lol-{r:03d}' for r in range(0, 3)]

BEHIND THE SCENE OF THE MAP IMPLEMENTATION
=====
def map(function, list):
    re = []
    for element in list:
        re.append(functoin(element))
    return re

ls1 = [1,2,3,4,5]
ls2 = [6,7,8,9,10]

def merge(ls1, ls2):
    re = [x for x in list(map(lambda x, y: x+y, ls1, ls2))]
    print(re)
    return re

merge(ls1, ls2)

#########################################################################################
ITERATOR
=====

NEXT
=====
# Reference: https://www.programiz.com/python-programming/methods/built-in/next
marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# the next element is the first element
marks_1 = next(iterator_marks)

print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)

print(marks_2)

# Output: 65
#         71

NEXT - Syntax
=====
next(iterator, default)

NEXT - Example
=====
random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)

# Output: 5
print(next(random_iterator))

# Output: 9
print(next(random_iterator))

# Output: 'cat'
print(next(random_iterator))

# This will raise Error
# iterator is exhausted
print(next(random_iterator))

NEXT - How to fix the error?
=====
random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

# Output: 5
print(next(random_iterator, '-1'))

# Output: 9
print(next(random_iterator, '-1'))

# random_iterator is exhausted
# Output: '-1'
print(next(random_iterator, '-1'))

print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))

#########################################################################################
ITERTOOLS
=====

GROUPBY
=====
# Reference: https://www.geeksforgeeks.org/itertools-groupby-in-python/
import itertools
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# Key function
key_func = lambda x: x[0]

for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))

# Output
a : [('a', 1), ('a', 2)]
b : [('b', 3), ('b', 4)]

PRODUCT
=====
# Reference: https://www.geeksforgeeks.org/python-itertools-product/
# How it works?
Input : arr1 = [1, 2, 3] 
arr2 = [5, 6, 7] 
Output : [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

Input : arr1 = [10, 12] 
arr2 = [8, 9, 10] 
Output : [(10, 8), (10, 9), (10, 10), (12, 8), (12, 9), (12, 10)]

# Example code
from itertools import product
 
def cartesian_product(arr1, arr2):
    return list(product(arr1, arr2))
   
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
print(cartesian_product(arr1, arr2))

# Output
[(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)] 

#########################################################################################
FILTER
=====
'''
Return a new sequence where values are taken from the given sequence if they
return True when passes to a given function
'''
list(filter(lambda x : x % 2 == 0, range(1, 5)))
[2, 4]

list(map(lambda x : x % 2 == 0, range(1, 5))) # A map would return the Boolean values
[False, True, False, True]

# List comprehension
[x for x in range(1, 5) if x % 2 == 0]
[2, 4]

# Another way of putting the list according to the number
even = lambda x: x % 2 == 0
list(filter(even, range(11)))
[0, 2, 4, 6, 8, 10]

list(filter(lambda x:x>5, range(11)))
[6, 7, 8, 9, 10]

list(filter(lambda x:len(x)>5, ['Cat', 'Dragon', 'Elephant'])) 
['Dragon', 'Elephant']

#########################################################################################
REDUCE
=====
from functools import reduce

total = reduce(lambda accumulative, current: accumulative + current, [1,2,3], 0) # <-- 0 here means starting total as 0
print(total) # 6

# Another way when having tuple or dict
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
reduce(lambda acc, element: acc + element[0], pairs, 0) # element is the element in the pairs list which is the tuple in this case
# 6

pairs = [(1, 'apple'), (2, 'boy'), (3, 'cat')]
reduce(lambda acc, element: acc + len(element[1]), pairs, 0) # element is the element in the pairs list which is the tuple in this case
# 11

# Using sum function
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x for x, _ in pairs)
# 6

#########################################################################################
WHILE LOOP WITH BREAK & CONTINUE
=====
# NOTE: MAKE SURE YOU HAVE A CONDITION THAT CAN CEASE THE LOOPING 
# IF STUCK IN A INFINITY LOOPING, PRESS `CTRL + C` TO STOP THE PROGRAM

# Indefinite loop
while True:
	line = raw_input("> ") # For python 3 change to input()
	if(line[0] == '#'):
		continue # Skip the below code and continue the next loop
	if line == 'done':
		break
	print(line)

print('Done!')

Example 2:
counter = 5

while counter > 0:
	print(counter)
	counter--

print('Blast off!')

# PRIME FACTOR
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1

  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5

FOR LOOPS
====
# Definite loop

for i in [5,4,3,2,1]:
	print(i)

print('Blast Off')

Example 2:
for i in range(10):
	print(i)

Example 3:
# Print 5 until 11
for i in range(5, 12):
	print(i)

friends = ['John', 'Sarah', 'Albert']

for friend in friends:
	print('Hello', friend)

Example 4:
for i in range(2, 10, 2):
	print(i, end=" ")
# Output: 2 4 6 8

Example 5: Looping through each of the letter in a string
for letter in "abc":
    print(letter)
"""
a
b
c
"""

# BREAK in FOR LOOP: Stop the for loop immediately
num = [1,2,3,4,5]
find = 3
for i in num:
    if i == find:
        print("found!")
        break;
    print(i)

"""
1
2
found!
"""

# CONTINUE in FOR LOOP: Skipping the rest of the code below the continue statement and continue the next loop
num = [1,2,3,4,5]
find = 3
for i in num:
    if i == find:
        print("found!")
        continue;
    print(i)

"""
1
2
found!
4
5
"""

# Factorial using For Loop
factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
"""
Other way #1:
n = 1
fib = 1
for i in range(2, n+1): # Without looping the 1
    fib *= i
print(fib)

Other way #2:
def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result
"""

# Using recursive method
def fac(n, total=1):
    if n == 1: return total
    else: return fac(n-1, total*n)
print(fac(5)) # Output: 120

#########################################################################################
BOOLEAN
=====
check = True

if check:
	print('Yes')

NONE TYPE = NULL (FLAG VALUE)
=====
# Like Java null
# Find the smallest number
min = None

for i in [5, 23, 12, 4, 33]:
	if min is None:
		min = i
	elif i < min:
		min = i

print('Smallest value:', min)

GLOBAL VARIABLE
=====
# Using Global Variable
def getUsername():
    global name
    name = input('Enter your username: ')
    return name

def validUsername(name):
    return len(name) >= 3

while not validUsername(getUsername()):
	print('Invalid username')

print('Good day', name)

RANDOM
=====
import random
random.randint(1, 100)
>> 5

random.uniform(1,100)
>> 5.890128243620637

random.randrange(1, 100)
>> 23

names = ['John', 'Alice', 'James']
classMonitor = random.choice(names)
>> Alice

SHUFFLE
=====
a = [1,2,3,4,5]
random.shuffle(a)
print(a) # [5,3,2,1,4]

CHOICE
=====
ls = [343,15,23,8]
print(random.choice(ls)) # 8 <-- Always random

SAMPLE
=====
'''
sample(['red', 'blue'], counts=[4, 2], k=5)  
	=
sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
'''
a = random.sample(['red', 'blue', 'yellow'], counts=[3, 2, 10], k=5)
print(a) # ['yellow', 'blue', 'yellow', 'yellow', 'yellow'] <-- Always random

#########################################################################################
CHARACTER # ASCII
=====
a = chr(97)
a
>> 'a'

GETTING THE ORDER OF THE CHARACTER
=====
word = "abc"
c = ord(word[0])
c
>> 97

#########################################################################################
INTEGER, FLOAT
=====
int(x), float(x)

ROUNDING OFF
=====
# round(FLOAT, ndigits)
total = 12.259
round(total, 2)
>> 12.26
total
>> 12.259
total = round(total, 2)
total
>> 12.26

# round of nearest tenth, hundredth so on
# ndigits=-1 rounds to the nearest 10, ndigits=-2 rounds to the nearest 100 and so on
print(round(1235, -1)) # 1240
print(round(1255, -2)) # 1300
print(round(1555, -3)) # 2000

IMAGINARY NUMBER
=====
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag) # 0
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag) # 3.0

ABSOLUTE VALUE
=====
abs(-3) = 3     # Return absolute value of -3: Always a positive number will be returned
abs(3)  = 3
abs(-123.42123) = 123.42123

#########################################################################################
STRINGS
=====
fruit = 'pineapple'
letter = fruit[1]
print(letter)
>> i

LENGTH OF A STRING
=====
name = 'John'
len(name)
>> 4

for letter in name:
	print(letter)

# ABOVE CODE DOES THE SAME THINGS AS THE BELOW CODES

index = 0
while index < len(name):
	letter = name[index]
	print(letter)
	index += 1

MULTIPLE LINE STRING
=====
longString = '''This is the first line
This is the second one
Last one
'''

longString = """This is the first line
This is the second one
Last one
"""

SLICING STRINGS
=====
tmp = 'Monty Python'
       0123456789[10][11]
s[0:4]
>> Mont
s[6:7]
>> P
s[6:20]
>> Python

s[:2]
>> Mo
s[8:]
>> thon
s[:]
>> Monty Python

MANIPULATING STRINGS
=====
# Concatenation == concat
a = 'Hello'
b = a + "There"
print(b)
>> HelloThere
b = a + " " + "There"
print(b)
>> Hello There

REVERSING A STRING
=====
# Reference: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

# 1
def reverse(string): 
    string = string[::-1] 
    return string 
'''Explanation : Extended slice offers to put a “step” field as [start,stop,step], and giving no field as start and stop indicates default to 0 and string length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.'''

# 2
def reverse(string): 
    string = "".join(reversed(string)) 
    return string

# 3 Fastest way if the string is not a palindrome
def isPalindrome(x):
	for i in range(len(x)):
		if x[i] != x[-1-i]:
			return False

print(isPalindrome('kayik')) # False

USING in AS A LOGICAL OPERATOR
=====
fruit = 'banana'
'n' in fruit
>> True
'nan' in fruit
>> True

STRING COMPARISON
=====
if word == 'banana':
	print("Yes")

if word < banana:
	print(word, "comes before banana")
elif word > 'banana':
	print(word, "comes after banana")
else:
	print("Yes banana")

STRING LIBRARY
=====
tmp = 'Hello World'
print(tmp.lower())
>> hello world

foo = tmp.lower()
print(foo)
>> hello world

type(tmp)
#>> <class 'str'>

# .count() - Count and return the amount of occurance of the word/letter asked to count
print(tmp.count('l'))
>> 3

# .find() - Find and return the index position of the parameter in a str
# CTRL + F = "FIND THE INDEX"

MATH LIBRARY
=====
import math

math.sqrt(4) # Output: 2
math.sin(0)	 # Output: 0.0
math.cos(0)	 # Output: 1.0

math.floor(2.5) # Output: 2
math.ceil(2.5)  # Output: 3

rad = math.radians(90)
print(math.sin(rad)) # 1

POWER WITHOUT THE POWER FUNCTION
=====
import math

for i in range(1, 6):
    print(i, math.prod(2 for _ in range(i)))

1   2
2   4
3   8
4   16

WEBSITE
=====
import webbrowser
webbrowser.open('https://www.google.com', new=0, autoraise=True)
# new = 0 : Open in the same browser window
# new = 1 : Open in a new tab
# new = 2 : Not much diff with the new = 1
# autoraise = True and False have not much diff

url = 'https://www.github.com'
webbrowser.open_new(url)
webbrowser.open_new_tab(url)

DISPLAY ALL THE METHODS AVAILABLE FOR VARIABLE
=====
dir(tmp)
>> ['capitalize', 'casefold', 'center', ...]

DISPLAY ALL METHODS AND VARIABLES USED
=====
dir()

DELETING THE VARIABLE
=====
del var

FIND THE INDEX
=====
fruit = 'banana'
         012345
pos = fruit.find('na')
>> 2

aa = fruit.find('z')
>> -1

info = 'From geniusGoogle@gmail.com GeniusUser'
pos = info.find('@')
# Second parameter taken in means where to starts
secondPos = info.find(' ', pos)
host = info[pos+1 : secondPos]
>> gmail.com

STRING UPPER & LOWER
=====
tmp = hEllo woRld
tmp.upper()
>> HELLO WORLD

tmp.lower()
>> hello world

tmp.title()
>> Hello World

SEARCH & REPLACE
=====
tmp.replace('Hello', 'Goodbye')
>> Goodbye World

STRIPPING WHITESPACE
=====
greet = '     Hello There  '
greet.lstrip()
>> 'Hello There  '
greet.rstrip()
>> '     Hello There'
greet.strip()
>> 'Hello There'

PREFIXES
=====
# STARTSWITH
tmp = 'Please okay?'
tmp.startswith('Please')
>> True
tmp.startswith('p')
>> False

# ENDSWITH
tmp.endswith("okay?")
>> True

STRING & CHARACTER SET
=====
# PYTHON3 <## in py3, all string are unicode
x = u'한국어'
type(x)
>> <class 'str'>

# PYTHON2
x = u'한국어'
type(x)
>> <class 'unicode'>

REGEX
=====
import re
s = "how much for the maple syrup? $20.99? That's ridiculous!!!"
s = re.sub(r'[^\w]', ' ', s)
s = re.sub(r'[\W]', ' ', s)
>> 'how much for the maple syrup   20 99  That s ridiculous   '

s = re.sub(r'[\W]', '', s)
>> 'howmuchforthemaplesyrup2099Thatsridiculous'

s = re.sub(r'[^\w\S]', '', s)
>> "howmuchforthemaplesyrup?$20.99?That'sridiculous!!!"

s = re.sub(r'[^\w\s]', '', s)
>> 'how much for the maple syrup 2099 Thats ridiculous'

s = re.sub(r'[\w\s]', '', '..   apple')
>> '..'

s = re.sub(r'[\w\s]', '', '..   apple  ..')
>> '....'

# Changing a list to a string then replace them, we can avoid using for loop
test_str = ['123', '456']
b = (str) (test_str) # "['123', '456']"
a = re.sub(r'[\[\]\,]', '', b)

print(a) # '123' '456'
a.replace("'", ':') # :123: :456:


def a(text):
    chars = "&#"
    for c in chars:
        text = text.replace(c, "\\" + c)

def b(text):
    for ch in ['&','#']:
        if ch in text:
            text = text.replace(ch,"\\"+ch)

import re
def c(text):
    rx = re.compile('([&#])')
    text = rx.sub(r'\\\1', text)

RX = re.compile('([&#])')
def d(text):
    text = RX.sub(r'\\\1', text)

def mk_esc(esc_chars):
    return lambda s: ''.join(['\\' + c if c in esc_chars else c for c in s])
esc = mk_esc('&#')
def e(text):
    esc(text)

# SECOND
def f(text):
    text = text.replace('&', '\&').replace('#', '\#')

def g(text):
    replacements = {"&": "\&", "#": "\#"}
    text = "".join([replacements.get(c, c) for c in text])

# THIRD
def h(text):
    text = text.replace('&', r'\&')
    text = text.replace('#', r'\#')

# FIRST
def i(text):
    text = text.replace('&', r'\&').replace('#', r'\#')

ISNUMERIC
=====
# Check if it is numeric or alphabet
"forest".isnumeric()
>> False

"12345".isnumeric()
>> True

ISDIGIT
=====
"123".isdigit()
>> True

ISALPHA()
=====
"abc".isalpha()
>> True
"abc ".isalpha()
>> False

ISALNUM()
=====
"abc123".isalnum()
>> True
"abc 123".isalnum()
>> False

SPLIT
=====
a = "This is a delicious ice-cream that no one can eat"
ls = a.split(sep=None, maxsplit=3)
print(ls)
>> ['This', 'is', 'a', 'delicious ice-cream that no one can eat']

time = '18:42'
hr, mins = time.split(':')
print(hr)   # 18
print(mins) # 42

JOIN
=====
# Note: str.join(iterable)
lst = "The string is splitted into a list".split(" ")
lst
>> ['The', 'string', 'is', 'splitted', 'into', 'a', 'list']
finalString = " - ".join(lst)
finalString
>> 'The - string - is - splitted - into - a - list'

Formatting String
=====
name = "John"
number = len(name) * 3

print("Hello {}, your lucky number is {}". format(name, number))
>> Hello John, your lucky number is 12

# More systematic way
# Note that name & name are identified separately
print("Your lucky number is {num}, {name}.".format(name = name, num = len(name)*3))
>> Your lucky number is 12, John.

# Easiest way
print(f"Your lucky number is {number}, {name}.") # Make sure the variable in the curly braces is same as the initialized variables
>> Your lucky number is 12, John.

# Example
def student_grade(name, grade):
	# return "{name} received {grade}% on the exam".format(name = name, grade = grade)
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

FORMATTING FLOAT IN STRING
=====
price = 8.7
price_with_gst = price * 1.06
print(price, price_with_gst)
>> 8.7 9.222

# To round up the tax to 2dp
print("Price: RM{:.2f}\nWith Tax: RM{:.2f}".format(price, price_with_gst))
'''
Price: RM8.70
With Tax: RM9.22
'''
# if price_with_gst == 8.185 and rounded off, result will be 8.18

# Significance Figure
print("pi to 4 significant digits = {:.4}".format(math.pi))
>> pi to 4 significant digits = 3.142

# Meaning of the semicolon
print("With tax: RM{gst:.2f}".format(gst = price_with_gst))
>> With tax: RM9.22

# ADVANCED FORMATTING
def toCelcius(x):
	return(x-32)*5/9

for x in range(0, 101, 10):
	print(toCelcius(x))

'''
#17.77777777777778
#12.222222222222221
#6.666666666666667
#1.1111111111111112
4.444444444444445
10.0
15.555555555555555
21.11111111111111
26.666666666666668
32.22222222222222
37.77777777777778
'''

for x in range(0, 101, 10):
	print("{:>3} F | {:>6.2f} C".format(x, toCelcius(x)))
'''
  0 F | #17.78 C
 10 F | #12.22 C
 20 F |  #6.67 C
 30 F |  #1.11 C
 40 F |   4.44 C
 50 F |  10.00 C
 60 F |  15.56 C
 70 F |  21.11 C
 80 F |  26.67 C
 90 F |  32.22 C
100 F |  37.78 C
'''

#########################################################################################
FILES
=====
# Open is not reading the file, it is just making the file avaialble for our code to write
handle = open(filename, mode)
# Above return a handle use to manipulate the file
# File handle is not the data, it's just a way to get at the data but a thing that we can manipulate
test = open('tester.txt', 'r')
print(test)
>> <_io.TextIOWrapper name='Test.txt' mode='r' encoding='cp1252'>

open()
read()
write()
close()

USING WITH OPEN TO READ
=====
with open('files.txt') as datafile:
	data = datafile.read()
print(data)

USING WITH OPEN TO WRITE DATA TO A FILE
=====
string = 'This is a sentence'
with open(r"C:\Users\Files\data.txt", "w") as writer:
	writer.write(string)

OR

writer = open(r'C:\Users\Files\Lol.txt', "w")
writer.write(string)
writer.close() # IMPORTANT TO CLOSE FOR THIS METHOD

NEWLINE CHARACTER
=====
# Non#printing character that move to the next line
test = 'Hello\nWorld'
print(test)
>> Hello
>> World

# Newline [\n] is one character
test = 'X\nY'
len(test)
>> 3

FILE HANDLE AS A SEQUENCE
=====
f = open('test.txt', 'r')
for cheese in f:
	print(cheese)

COUNTING LINES
=====
count = 0
f = open('test.txt', 'r')
for cheese in f:
	count += 1
	print(cheese)
print("Line", count)

# Above will end up one extra empty line after one line
# To solve, rstrip()
f = open('Test.txt')
for cheese in f:
	cheese = cheese.rstrip()
	print(cheese)

# Example 2
f = open('test.txt', 'r')
for cheese in f:
	cheese = cheese.rstrip()
	if not cheese.startswith('Hello'):
		continue
	else:
		print(cheese)


READING THE *WHOLE* FILE
=====
# READ ALL THE STUFF WITH THE NEWLINE INTO A SINGLE STRING
test = open('test.txt')
data = test.read()

print(data)
>> Hello there user, asduhunuioahvb...
len(data)
>> 56223
data[:5]
>> Hello

HOW TO DEAL WITH NON-EXISTING FILE
=====
try:
	data = open('test.txt')
except:
	print('File not found')
	quit()

#########################################################################################
LISTS
=====
# Creating a list
A = list()
A = []

# A COLLECTION
friends = ['Ali', 'Ah Kau', 'Muthu']

# A list can be included with diff type of data
mix = ['Ali', 29, 175.5, 89.2, 'Sarah']
print(mix[1]) # 29
print(mix[5]) # 'Sarah'
print(mix[-1]) # 'Sarah'
print(mix[0]) # 'Ali'
print(mix[-5]) # 'Ali'
print(mix[-6]) # IndexError: list index out of range
print(mix[6]) # IndexError: list index out of range

# List in a list
ll = [1, [23,2], 55]
print(ll[1][1]) # 2

# Clear the list
emp = [] # or emp = list()

# Printing the elements of the list using for loop
for data in mix:
	print(data, end = " ") # 'Ali' 29 175.5 89.2 'Sarah'

# Print the list at once
print(mix) # ['Ali', 29, 175.5, 89.2, 'Sarah']

PUTTING FUNCTION IN A LIST
=====
ls = ['Ali', help]
ls[1](int)
>>> Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if...

CREATE A LIST OF NUMBER ASCENDING WIHOUT LOOP
=====
num_list = list(range(100))
print(num_list) # [0, 1, 2, ..., 99]

ls = list(range(3,8))
print(ls) # [3,4,5,6,7]

ls = list(range(0, 10, 2))
print(ls) # [0, 2, 4, 6, 8]

LOOKING INSIDE THE LISTS
=====
friends = ['Ali', 'Ah Kau', 'Muthu']
print(friends[2])
>> Muthu

print(friends[:2])
>> ['Ali', 'Ah Kau']

n = [5,4,3,2,1]
print(n[2:4]) # [3,2] NOTE: the [x:y] --> x is inclusive while y is not inclusive

GET THE INDEX OF THE ELEMENT IN A LIST
=====
grocery = ['cookie', 'bacon', 'vege']
print(grocery.index('bacon')) # 1

letter = ['a', 'b', 'a']
print(letter.index('a')) # 0

num = [1,2,3]
print(num.index(1)) # 0

LISTS ARE MUTABLE/CHANGEABLE
=====
String: immutable
test = 'hello'
test[1]
>> e

test[1] = 'o'
# TRACEBACK: TypeError: 'str' object does not support item assignment

players = [93, 23, 45, 1, 9]
players[2] = 7

players
>> [93, 23, 7, 1, 9]

len(players)
>> 5

LIST CONCATENATION
=====
ls = [1,2,3]
ls *= 2
print(ls) # [1,2,3,1,2,3]

ls1 = [4,5,6]
print(ls + ls1) # [1, 2, 3, 1, 2, 3, 4, 5, 6]

COUNTING ELEMENT IN A LIST
=====
ls = [1, 2, 3, 1, 2, 3, 4, 5, 6]
print(ls.count(3))
>> 2

RANGE
=====
print(range(4))
>> [0, 1, 2, 3]

print(range(len(players)))
>> [0, 1, 2, 3, 4]

LOOPS
=====
for f in friends:
	print(f)

for i in range(len(friends)):
	print(friend[i])

SLICING LISTS
=====
# UP TO BUT NOT INCLUDING
tmp = [1,2,3,4,5,6,7,8]
tmp[1:3]
>> [2,3]

tmp[:4]
>> [1,2,3,4]

tmp[3:]
>> [4,5,6,7,8]

tmp[:]
>> [1,2,3,4,5,6,7,8]

LIST FUNCTION
=====
x = list()
y = [1,2,3,4]
z = list(y)
print(z)
>> [1,2,3,4]

type(x)
>> <type 'list'>
dir(z)
>> ['append', 'count', 'sort', ...]

APPEND
=====
# Always append at the end of the list unless you want to insert
thing = list()
thing.append(99)
thing.append('apples')

print(thing)
>> [99, 'apples']

INSERT
=====
fruits = ['apple', 'banana', 'pineapple', 'melon']
fruits.insert(1, 'orange')
>> ['apple', 'orange', 'banana', 'pineapple', 'melon']

fruits.insert(999, 'Possible Fruit')
>> ['apple', 'orange', 'banana', 'pineapple', 'melon', 'Possible Fruit']

REMOVE
=====
fruits.remove('Possible Fruit')
>> ['apple', 'orange', 'banana', 'pineapple', 'melon']

fruits.remove('Pear')
>> TRACEBACK: ValueError list.remove(x): x not in list

ls = [1,5,1,2,3,4,1]
ls.remove(1) # [5, 1, 2, 3, 4, 1]

POP
=====
fruits.pop()
>> 'melon'
>> ['apple', 'orange', 'banana', 'pineapple']

CHECK IF AN ITEM IN THE LIST
=====
num = [123, 2, 45, 67, 89]
2 in num
>> True
77 in num
>> False
77 not in num
>> True

a = [1,2,3]
b = [4,5,6]
a.append(b)
print(a)
>> [1, 2, 3, [4, 5, 6]]

SORT
=====
# This function modifies the list you chose
name = ['Sarah', 'John' ,'Ali']
print(name)
>> ['Sarah', 'John' ,'Ali']
name.sort()
print(name)
>> ['Ali', 'John', 'Sarah']
name[1]
>> 'John'

# NOTE: Works for the numbers too
x = [3,1,2]
x.sort()
print(x) [1,2,3]

# SORTING IN REVERSE ORDER
n = [1,2,3]
n.sort(reverse=True)
print(n) # [3,2,1]

# Another method
reversed = n[::-1]

SORTED
=====
# This function return you a new sorted list without modifying the original list
names = ['Sarah', 'John' ,'Ali']
newList = sorted(names)
newList
>> ['Ali', 'John', 'Sarah']
names
>> ['Sarah', 'John' ,'Ali']

Sorted with a function
=====
# https://www.programiz.com/python-programming/methods/built-in/sorted
# take the second element for sort
def take_second(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)
# Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

Sorted with multiple keys
=====
# https://www.programiz.com/python-programming/methods/built-in/sorted
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100, Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)

sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)
# [('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]

# Explanation: Tuple comparison is OR condition
>>> (1,3) > (1, 4)
False
>>> (1, 4) < (2,2)
True
>>> (1, 4, 1) < (2, 1)
True

Using LAMBDA instead of function
=====
sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))

print(sorted_list)


SORTED BY KEY
=====
# What if we want to sort the list according to the length of the word
names = ['Carlos', 'Pewdiepie' ,'Ali']
newList = sorted(names, key=len)
newList
>> ['Ali', 'Carlos', 'Pewdiepie']

BUILD-IN FUNCTION FOR LIST: FIND THE MAX, MIN, SUM, *
=====
nums = [12,25,38,49,53,6]
len(nums)
>> 6
max(nums)
>> 53
min(nums)
>> 6

# KEY FOR MIN AND MAX
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)

sum(nums)
>> 183

# To get average
print(sum(nums) / len(nums))

numlist = list()

while True:
	n = input("Enter a num: ")
	if n == 'done':
		break
	else:
		numlist.append(float(n))

average = sum(numlist) / len(numlist)

LISTS & STRINGS
=====
SPLIT
tmp = "ABC with cows"

tmpList = tmp.split()
>> ['ABC', 'with', 'cows']
len(tmpList)
>> 3
tmpList[1]
>> 'with'

for w in tmpList:
	print(w)
>> 'ABC'
>> 'with'
>> 'cows'

# SPLIT THE WHITESPACE AS WELL
tmp = 'hello       there hahaha'
tmpList = tmp.split()
>> ['hello', 'there', 'hahaha']

tmp = 'hello;there;world'
tmpList = tmp.split()
>> ['hello;there;world']
tmpList = tmp.split(';')
>> ['hello', 'there', 'world']

# LIST COMPREHENSION
multiples = []
for i in range(1, 11):
	multiples.appned(i*7)

print(multiples)
>> [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Better version = use list comprehension
print([i*7 for i in range(1,11)])
>> [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

language = ['Python', 'Java', 'C++', 'Javascript']
print([len(x) for x in language])
>> [6, 4, 3, 10]

Flatten the 2d list
=====
list_of_list = [[1,2,3],[4,5,6],[7,8]]
flatten_list_of_list = [j for i in list_of_list for j in i]
print(flatten_list_of_list)
output: [1, 2, 3, 4, 5, 6, 7, 8]

Identity matrix
=====
identity_matrix = [[ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]
print(identity_matrix)
eye = [[1 if i==j else 0 for i in range(3)] for j in range(3)]
output: [1, 0, 0], [0, 1, 0], [0, 0, 1]]

Transpose
=====
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(3)]
print(transposed_matrix)
output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# IF statement in list comprehension
def count_negatives(nums):
    return len([n for n in nums if n < 0])

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [n > thresh for n in L]

# Print number which is divisible by 3
print([x for x in range(0, 40) if x % 3 == 0])
>> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]

# MORE LIST METHODS
list.reverse() # Reverses the order of items of the list
x = [1,2,3]
x.reverse()
print(x) # [3,2,1]

list.clear() # Removes all the items of the list
list.copy() # Creates a copy of the list
list.extend(other_list) # Appends all the elements of other_list at the end of list

x = [1,2,3]
y = [4,5]
x.extend(y)
print(x) # [1,2,3,4,5]

# NOTE: If you use append, it will cause list in a list
# Example
x = [1,2,3]
y = [4,5]
x.append(y)
print(x) # [1,2,3,[4,5]]

# BLACKJACK: COMPARING BETWEEN TWO HANDS
def getVal(cards):
    
    val = 0; aces = 0
    
    for c in cards:
        if c in ['J', 'Q', 'K']:
            val += 10
        elif c == 'A':
            aces += 1
        else:
            val += int(c)
        
    if aces == 1 and val <= 10:
        val += 11
    else:
        val += aces
        
    return val

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    
    # Initializing the score
    h1 = getVal(hand_1)
    h2 = getVal(hand_2)
    
    return h1 <= 21 and (h1 > h2 or h2 > 21)

Checking if all the elements in a list are identical
=====
# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
# Method 1
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

# Method 2
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

#########################################################################################
DICTIONARIES
=====
# Creating a dictionary
A = dict()
A = {}

# IT HAS LABEL TO IT
# KEY-VALUE PAIR LIKE HASHMAP
# Not in order
purse = {'RM50': 1, 'RM20': 5, 'RM5': 3}
purse['RM5'] # 3
purse.get('RM5') # 3
purse['RM1'] # ERROR: KeyError: 'RM1'
purse.get('RM1', 0) # 0 because default value is set to 0 when the key 'RM1' is not found
purse.get('RM1', 'Not found!') # Not found!

# NOTE: Without the 0 parameter added, it will return None if the key is not found
purse.get('RM1') # None

wallet = dict()
wallet['RM50'] = 3
wallet['RM20'] = 10
wallet['RM5'] = 7

print(wallet)
>> {'RM50': 3, 'RM20': 10, 'RM5': 7}

wallet['RM50'] += 2
print(wallet['RM50'])
>> 5

APPENDING NEW KEY
=====
wallet['RM1'] = 12
print(wallet)
>> {'RM50': 3, 'RM20': 10, 'RM5': 7, 'RM1': 12}

EDITING THE VALUE OF A KEY
=====
wallet['RM50'] = 0
print(wallet)
>> {'RM50': 0, 'RM20': 10, 'RM5': 7, 'RM1': 12}

ADDING KEY AND UPDATING FEW KEYS AND THEIR RESPECIVE VALUE AT THE SAMETIME
=====
student1 = {'name':'John', 'age':19, 'courses':['CS', 'ALGO']}
student1.update({'name':'Jane', 'age':29, 'phone':'213-1234'})
print(student1)
# {'name': 'Jane', 'age': 29, 'courses': ['CS', 'ALGO'], 'phone': '213-1234'}

DELETING KEY WITH ITS VALUE
=====
del wallet['RM50']
print(wallet)
>> {'RM20': 10, 'RM5': 7, 'RM1': 12}

# NOTE: Another way to delete
student1 = {'name':'John', 'age':19, 'courses':['CS', 'ALGO']}
s1courseList = student1.pop('courses') # ['CS', 'ALGO']
print('student1') # {'name': 'John', 'age': 19}

FINDING KEYS THAT DONT EXIST
=====
hashmap = dict()
print(hashmap['Ali'])
>> TRACEBACK, KeyError: 'Ali'
'Ali' in hashmap
>> True

ADDING LIST OF KEYS INTO DICTIONARIES
=====
hashmap = dict()
names = ['Ali', 'Abu', 'Sarah', 'Ali', 'Ali','Ah Kau']
for name in names:
	if name not in hashmap:
		hashmap[name] = 1
	else:
		hashmap[name] += 1

print(hashmap)
>> {'Ali': 3, 'Abu': 1, 'Sarah': 1, 'Ah Kau': 1}
# Simplified version below

LENGTH OF THE KEYS IN A DICT
=====
student1 = {'name':'John', 'age':19, 'courses':['CS', 'ALGO']}
print(len(student1)) # 3

GETTING THE KEYS
=====
print(student1.keys()) # dict_keys(['name', 'age', 'courses'])

GETTING THE VALUES
=====
print(student1.values()) # dict_values(['John', 19, ['CS', 'ALGO']])

GETTING THE KEYS AND VALUE USING .items()
=====
print(student1.items()) # dict_items([('name', 'John'), ('age', 19), ('courses', ['CS', 'ALGO'])])
print(student1) # {'name': 'John', 'age': 19, 'courses': ['CS', 'ALGO']}

PRINTING THE KEYS AND VALUES USING FOR LOOP
=====
>>> for k, v in student1: # NOTE: Make sure to have .items() to get the keys and values
...     print(k, v)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)

# Correct method
>>> for k, v in student1.items():
...     print(k, v)
...
name John
age 19
courses ['CS', 'ALGO']


ITERATING THE CONTENTS OF DICTIONARY
=====
# DISPLAYING KEYS
for n in hashmap:
	print(n)

# Another way of printing the keys
for n in hashmap.keys():
	print(n)
'''
Ali
Abu
Sarah
Ah Kau
'''

# Displaying the keys in a list
print([n for n in hashmap.keys()])
>> ['Ali', 'Abu', 'Sarah', 'Ah Kau']

# DISPLAYING VALUES
for v in hashmap.values():
	print(v)
'''
3
1
1
1
'''

# Displaying the values in a list
print([c for c in hashmap.values()])
>> [3, 1, 1, 1]

TYPE FOR KEYS IN DICTIONARIES
=====
# Keys can only be immutable type: Numbers, Booleans, Strings, Tuples
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for shirt in wardrobe:
	for col in wardrobe[shirt]:
		print("{} {}".format(col, shirt))

wardrobe["shirt"][1] = "pink"
>> {'shirt': ['red', 'pink', 'white'], 'jeans': ['blue', 'black']}

GET METHOD
=====
name = 'Ali'
x = names.get(name, 0)
# put the value into x, but if there is no key, default value for x is 0
x = names.get(name, 5)
# put the value into x, but if there is no key, default value for x is 5
x = names.get(name)
>> None
# put the value into x, but if there is no key, default value for x is None

# With this, there is no traceback KeyError
hashmap = dict()
names = ['Ali', 'Abu', 'Sarah', 'Ali', 'Ali','Ah Kau']

for name in names:
	hashmap[name] = hashmap.get(name, 0) + 1

print(hashmap)

FUNCTION RETURNING DICTIONARY
=====
# Count letters
def count_letters(txt):
	result = dict()

	for char in txt:
		result[char] = result.get(char, 0) + 1

	return result

print(count_letters(input('> ')))

'''
> This is a String
{'T': 1, 'h': 1, 'i': 3, 's': 2, ' ': 3, 'a': 1, 'S': 1, 't': 1, 'r': 1, 'n': 1, 'g': 1}
'''

USING DICT TO ACT LIKE A SWITCH CASE
=====
# Ref: https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
# 1: Problem occurs when the `x` is not found
def f(x):
    return {
        'a': 1,
        'b': 2
    }[x]

# 2
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found

COUNTING PATTERN
=====
counts = dict()
line = input("Enter line of text: ")
words = line.split()

print('List of words:', words)

for w in words:
	counts[w] = counts.get(w, 0) + 1

print(counts)

TO GET THE WORD WITH MOST FREQUENCY
=====
max = 0
highestFreqWord = ''
for key in counts:
	if counts[key] > max:
		max = counts[key]
		highestFreqWord = key

print('Key with highest frequency:', highestFreqWord, '\nCount:', counts.get(highestFreqWord))
print('Key with highest frequency:', highestFreqWord, '\nCount:', counts[highestFreqWord])
print('Key with highest frequency:', highestFreqWord, '\nCount:', max)

GETTING THE HIGHEST OCCURENCE OF THE ITEM IN A LIST
=====
ls = ['F', 'F', 'M', 'M', 'M', 'M']
commonGender = max(ls, key=ls.count)

RETRIEVING KEYS & VALUES
=====
hashmap = {'Ali': 3, 'Abu': 1, 'Sarah': 1, 'Ah Kau': 1}
print(list(hashmap))
>> ['Ali', 'Abu', 'Sarah', 'Ah Kau']
print(hashmap.keys())
>> dict_keys(['Ali', 'Abu', 'Sarah', 'Ah Kau'])
print(list(hashmap.keys()))
>> ['Ali', 'Abu', 'Sarah', 'Ah Kau']
print(hashmap.values())
>> dict_values([3, 1, 1, 1])
print(list(hashmap.values()))
>> [3, 1, 1, 1]

TUPLE
=====
print(hashmap.items())
>> dict_items([('Ali', 3), ('Abu', 1), ('Sarah', 1), ('Ah Kau', 1)])

TUPLE CONCATENATION
=====
a = (1,2,3)
b = a*2
print(b)

USING TUPLE TO DISPLAY THE KEY AND VALUES
=====
hashmap = {'Ali': 3, 'Abu': 1, 'Sarah': 1, 'Ah Kau': 1}

for k, v in hashmap.items():
	print(k, v)

>> Ali 3
>> Abu 1
>> Sarah 1
>> Ah Kau 1

file_counts = {'txt': 5, 'jpeg': 12, 'pdf': 9}

for extension, counts in file_counts.items(): # REMEMBER TO PUT .items()
	print("There are {} number of .{} file(s)".format(counts, extension))

'''
There are 5 number of .txt file(s)
There are 12 number of .jpeg file(s)
There are 9 number of .pdf file(s)
'''

# OPERATIONS
len(dictionary) # Returns the number of items in the dictionary
for key in dictionary # Iterates over each key in the dictionary
for key, value in dictionary.items() # Iterates over each key,value pair in the dictionary
if key in dictionary # Checks whether the key is in the dictionary
dictionary[key] # Accesses the item with key key of the dictionary
dictionary[key] = value # Sets the value associated with key
del dictionary[key] # Removes the item with key key from the dictionary

# METHODS
dict.get(key, default) # Returns the element corresponding to key, or default if it's not present
dict.keys() # Returns a sequence containing the keys in the dictionary
dict.values() # Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) # Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() # Removes all the items of the dictionary

# COMPREHENSION
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
"""
{'Mercury': 'M',
 'Venus': 'V',
 'Earth': 'E',
 'Mars': 'M',
 'Jupiter': 'J',
 'Saturn': 'S',
 'Uranus': 'U',
 'Neptune': 'N'}
"""

Sorting dictionary based on the values
=====
# https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    print(i[0], i[1])

'''
espresso 72
latte 56
cappuccino 54
americano 48
cortado 41
'''

#########################################################################################
TUPLES
=====
# More efficient version of list that you cant modify
# We can say the position inside the tuple has its meaning
# immutable, cannot be sorted like list

# Creating a tuple
A = tuple()
A = ()

x = ('Ali', 'Sarah', 'Abu')
x[1]
>> 'Sarah'

# Tuples not allow assignment, cannot be appended   
x[1] = 'Muthu'
>> ERROR: TypeError: 'tuple' object does not support item assignment

num = (55,2,45,122,98)
print(num)
>> (55,2,45,122,98)

print(max(num))
>> 122

GETTING RATIO
=====
x = 0.125
x.as_integer_ratio() # (1, 8)

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator) # 0.125

SWAPPING THE INTEGER WITHOUT USING TMP
=====
a = 1
b = 0
a, b = b, a
print(a, b)

FUNCTION RETURNING 1 OR MORE VALUES
=====
# Returning more than 1 value from a function
def convert(seconds):
	h = seconds // 3600
	m = (seconds - h*3600) // 60
	s = seconds - h*3600 - m*60
	return h, m, s

result = convert(5000)
type(result)
>> <class 'tuple'>

hrs, mins, secs = result
print(hrs, mins, secs)
>> 1 23 20

FOR LOOP
=====
for n in num:
	print(n)

num[1] = 12
>> Traceback error

# Not mutable thats why this allows the data to be stored more densely than lists

# Things NOT to be do with tuples
x.sort()
x.append(1)
x.reverse()
>> TRACEBACK: error

x = tuple()
dir(x)
>> ['count', 'index']

ASSIGNMENT
=====
(x, y) = (4, 'Fred')

print(y)
>> Fred

(a, b) = (213, 345)
print(a)
>> 213

(a, b) = (8)
>> TRACEBACK: error

ITEMS()
=====
d = dict()
d['RM50'] = 3
d['RM10'] = 10

for (k, v) in d.items():
	print(k, v)

>> RM50 3
>> RM10 10

tups = d.items()
print(tups)
>> dict_items([('RM50', 3), ('RM10', 10)])

COMPARABLE
=====
(0,1,2) < (5,1,2)
>> True
# Check first one first, 0 < 5? yes then return True and dont see behind anymore

('John', 'Sally') > ('Ali', 'Sam')
>> True

SORTING LIST OF TUPLES
=====
hashmap = {'Ali': 3, 'Abu': 1, 'Sarah': 1, 'Ah Kau': 1}
hashmap.items()
>> dict_items([('Ali', 3), ('Abu', 1), ('Sarah', 1), ('Ah Kau', 1)])

sorted(hashmap.items())
>> [('Abu', 1), ('Ah Kau', 1), ('Ali', 3), ('Sarah', 1)]

SORTED BY KEYS
=====
hashmap = {'C': 3, 'B': 123, 'A': -5}
sorted(hashmap.items())
>> [('A', -5), ('B', 123), ('C', 3)]

for k, v in hashmap.items():
	print(k, v)

>> C 3
>> B 123
>> A -5

for k, v in sorted(hashmap.items()):
	print(k, v)

>> A -5
>> B 123
>> C 3

SORTED BY KEYS LENGTH
=====
# https://stackoverflow.com/questions/11753758/dictionary-sorting-by-key-length
newlist = yourdict.items()
sortedlist = sorted(newlist, key=lambda s: len(s[0]))

SORTED BY VALUES
=====
hashmap = {'C': 3, 'B': 123, 'A': -5}
tmp = list()
for k, v in hashmap.items():
	tmp.append( (v, k) )

print(tmp)
>> [(3, 'C'), (123, 'B'), (-5, 'A')]

tmp = sorted(tmp)
>> [(-5, 'A'), (3, 'C'), (123, 'B')]

tmp = sorted(tmp, reverse=True)
>> [(123, 'B'), (3, 'C'), (-5, 'A')]

GET THE TOP 10 WORD FREQUENCY
=====
f = open('tomeo.txt')
counts = dict()

for line in f:
	words = line.split()
	for word in words:
		counts[word] = count.get(word, 0) + 1

# LONG VERSION
lst = list()
for k, v in counts.items():
	newtup = (v, k)
	lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
	print(k, v)

# SHORTER VERSION
print(sorted( [ (v, k) for k, v in c.items() ] ) )
>> [(-5, 'A'), (3, 'C'), (123, 'B')]

# READUP LIST COMPREHENSION = CREATES A DYNAMIC LIST

lst = ( [ (v, k) for k, v in hashmap.items() ] )
>> [(3, 'C'), (123, 'B'), (-5, 'A')]
lst.sort()
>> [(-5, 'A'), (3, 'C'), (123, 'B')]

ENUMERATE WITH TUPLE
=====
# The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.
players = ["Ali", "Sarah", "Ah Meng"]
for index, person in enumerate(players, start=1):
	print("{} - {}".format(index, person))

'''
1 - Ali
2 - Sarah
3 - Ah Meng
'''

# Return the tuple (index, character) for the "Hello"
for character in enumerate("Hello"):
    print(character)
'''
(0, 'H')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
'''

# Indexing each character for the "Hello" starting from 0
for index, character in enumerate("Hello"):
    print(str(index) + " " + character)
'''
0 H
1 e
2 l
3 l
4 o
'''

#Indexing each character for the "Hello" starting from 100
# enumerate(iterable, start=0)
for index, character in enumerate("Hello", 100):
    print(str(index) + " " + character)
'''
100 H
101 e
102 l
103 l
104 o
'''

#########################################################################################
ZIP
=====
# Taking two list and make them into a dictionary or a list of tuple
# Reference : https://realpython.com/python-zip-function/

items = ['Book', 'Orange', 'Bread', 'CD']
price = [31.99, 0.99, 3.17, 12.01]

# NOTE: ZIP is iterable
for i, p in zip(items, price):
    print(i, p)

'''
Book 31.99
Orange 0.99
Bread 3.17
CD 12.01
'''

# But you cannot call it without using the list or the dict function
print(zip(items, price))
# <zip object at 0x000001A7F03F1E40>

# Into list
print(list(zip(items, price)))
# [('Book', 31.99), ('Orange', 0.99), ('Bread', 3.17), ('CD', 12.01)]

# Into list using sorted
print(sorted(zip(items, price)))
# [('Book', 31.99), ('Bread', 3.17), ('CD', 12.01), ('Orange', 0.99)]

# Into dictionary
print(dict(zip(items, price)))
# {'Book': 31.99, 'Orange': 0.99, 'Bread': 3.17, 'CD': 12.01}

# Updating the value for one of the keys in dictionary
grocery = dict(zip(items, price))
new_price_for_orange = [1.09]
key_to_update = ['Orange']
grocery.update(zip(key_to_update, new_price_for_orange))
print(grocery)
#  {'Book': 31.99, 'Orange': 1.09, 'Bread': 3.17, 'CD': 12.01}

UNZIP
=====
# Unzipping the values into two tuples
# Refencence : https://careerkarma.com/blog/python-zip/ 
employees_zipped = [('Candice', 2), ('Ava', 9), ('Andrew', 18), ('Lucas', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
# ('Candice', 'Ava', 'Andrew', 'Lucas')
print(employee_numbers)
# (2, 9, 18, 28)

# Changing them into the list
employee_names, employee_numbers = list(employee_names), list(employee_numbers)

#########################################################################################
SETS
=====
# Creating a set
A = set()
A = {} # WRONG, this is a dictionary

setA = {123, 23, 65}
setB = {23, 2, 65}
print(setA.intersection(setB)) # {23, 65} 

set('abc').intersection('cbs').
>> {'b', 'c'}

# No duplicated element will be stored
A = {1,2,3,4,1}
print(A) # {1,2,3,4}

# using set() to remove duplicated from list 
test_list = list(set(test_list))

Instances of Set and ImmutableSet both provide the following operations:
=====
# number of elements in set s (cardinality)
len(s)

# test x for membership in s
x in s

# test x for non-membership in s
x not in s

# test whether every element in s is in t
s.issubset(t)
s <= t

# test whether every element in t is in s
s.issuperset(t)
s >= t

# new set with elements from both s and t
s.union(t)
s | t
setA = {1,2,3}
setB = {4,5,6}
print(setA.union(setB)) # {1,2,3,4,5,6}

# new set with elements common to s and t
s.intersection(t)
s & t
setA = {123, 23, 65}
setB = {23, 2, 65}
print(setA.intersection(setB)) # {23, 65} 

# new set with elements in s but not in t
s.difference(t)
s - t
setA = {123, 23, 65, 10}
setB = {23, 2, 65, 3}
print(setA.difference(setB)) # {10, 123} 
print(setB.difference(setA)) # {2, 3} 

# new set with elements in either s or t but not both == [a.intersection(b)]'
s.symmetric_difference(t)
s ^ t

# new set with a shallow copy of s
s.copy()
setA = {1,2,3}
setC = setA.copy()

print(setC) # {1,2,3}
setC.add(10000)
print(setC) # {1,2,3,10000}
print(setA) # {1,2,3}

The following table lists operations available in ImmutableSet but not found in Set:
=====
# returns a hash value for s
hash(s)

The following table lists operations available in Set but not found in ImmutableSet:
=====
# return set s with elements added from t
s.update(t)
s |= t

# return set s keeping only elements also found in t
s.intersection_update(t)
s &= t

#return set s after removing elements found in t
s.difference_update(t)
s -= t

# return set s with elements from s or t but not both
s.symmetric_difference_update(t)
s ^= t

# add element x to set s
s.add(x)

# remove x from set s; raises KeyError if not present
s.remove(x)

# removes x from set s if present
s.discard(x)

# remove and return an arbitrary element from s; raises KeyError if empty
s.pop()

# remove all elements from set s
s.clear()

Getting the intersection of the sets in a list of sets
=====
# Create the list of sets
lst = [{1, 2, 3}, {1, 4}, {1, 2, 3}]

# One-Liner to intersect a list of sets
print(lst[0].intersection(*lst))
# {1}

#########################################################################################
Object-Oriented Programming (OOP)
=====
type("x")
# >> <class 'str'>

dir(int)
# >> displays list of methods for int

help(int)
# >> displays list of documentation for int

print(help(str.lower))
# >> displays list of documentation for str.lower() method

# q to quit or quit to leave help session

CLASS
=====
# With or w/out () also can but I am sure that () is needed when you are parsing in parameters
# No I am wrong, see def __init__(), but putting () in the first line like below still works
class Apple():
	color = None
	flavor = None

# Creating an object, () is a must, it is like Java
RedApple = Apple() 

RedApple.color = "Red"
RedApple.flavor = "Sweet & Sour"

print('This apple is {} and it is {}.'.format(RedApple.color, RedApple.flavor))
# >> This apple is Red and it is Sweet & Sour.

# Another class
class Flower:
	color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower
violet.color = "Blue"

this_pun_is_for_you = "VERY CRINGY PUN INDEED"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

PASS
=====
# Just defining a new class and have not include the content for the class yet
class test:
	pass

tester = test()

FUNCTION IN A CLASS
=====
# 'self' = parameter represents the instance that the method is being executed on.
class Dog:
	name = "Bolt"
	def sound(self):
		print("Woof! I am {}!".format(self.name))

newDog = Dog()
newDog.sound()
>> Woof! I am Bolt!

newDog.name = 'Wing'
newDog.sound()
>> Woof! I am Wing!

RETRIEVING PROCESSED DATA FROM A CLASS FUNCTION
class piglet:
	year = 0

	def pig_years(self):
		return self.year * 18

hamlet = piglet()
hamlet.year = 2
print(hamlet.pig_years())
>> 36

__INIT__
=====
# Parsing in parameters into constructor of a class
class Apple:
	def __init__(self, name, color, flavor):
		self.name = name
		self.color = color
		self.flavor = flavor

	def display(self):
		print('{} apple is {} and it is {}'.format(self.name, self.color, self.flavor))

jonagold = Apple('Jonagold', 'red', 'sweet')
jonagold.display()
>> Jonagold apple is red and it is sweet

__STR__
=====
# Java's toString() method
class Apple:
	def __init__(self, name, color, flavor):
		self.name = name
		self.color = color
		self.flavor = flavor

	def __str__(self):
		return '{} apple is {} and it is {}'.format(self.name, self.color, self.flavor)

jonagold = Apple('Jonagold', 'red', 'sweet')
print(jonagold)
>> Jonagold apple is red and it is sweet

PROPERTY DECORATORS - GETTERS, SETTERS AND DELETERS
=====
''' Reference: https://www.youtube.com/watch?v=jCzT9XFZ5bw '''

class student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@edu.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Fullname deleted')
        self.first = None
        self.last = None


student1 = student('John', 'Cena')
print(student1.first)
print(student1.email) # With the @property decorator, you don't need .email() <--
print(student1.fullname) # With the @property decorator, you don't need .fullname() <--

# How to use the @fullname.setter
student1.fullname = 'Steve Jobs'
print(student1.first)
print(student1.email) # With the @property decorator, you don't need .email() <--
print(student1.fullname) # With the @property decorator, you don't need .fullname() <--

# How to use the @fullname.deleter
del student1.fullname


HELP FOR THE CLASSES YOU MADE
=====
class Apple:
	blah blah blah
	...

>>> help(Apple)
# Display list of documentation that define the methods you created in your classes
# !!! Methods are just like functions, but they can only be used through a class !!!
# Function are outside the classes
# But not much info when your coworker see it, they might not understand it

DOCSTRING
=====
# To solve the above problem, double quote(""") or single quote(''') also work 

def toSecond(h, m, s):
	"""Returns the amt of seconds from h, m, s"""
	return h*3600 + m*60 + s

help(toSecond)
# toSecond(h, m, s):
#     Returns the amt of seconds from h, m, s

# Example 2 of Docstring
class Apple:
	"""This is a class for Apple"""
	def __init__(self, name, color, flavor):
		"""This is a constructor"""
		self.name = name
		self.color = color
		self.flavor = flavor

	def __str__(self):
		"""toString() method"""
		return '{} apple is {} and it is {}'.format(self.name, self.color, self.flavor)

help(Apple.__str__)

# Docstring always one line below the function/class that you are documenting
# and has to be indented the same

#########################################################################################
INHERITANCE
=====
class Fruit:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

	def __str__(self):
		return "This fruit is {} and it is {}".format(self.color, self.flavor)

class Apple(Fruit):
	pass

class Grape(Fruit):
	pass

jonagold = Apple('Red', 'Sweet')
carnelian = Grape('Green', 'Sour')

print(jonagold)
print(carnelian)
'''
This fruit is Red and it is Sweet
This fruit is Green and it is Sour
'''

# Modifying the instance variable of the parent class from siblings class's object
class Animal:
	sound = ""
	def __init__(self, name):
		self.name = name

	def speak(self):
		print("{sound}! I am {name}! {sound}!".format(name = self.name, sound = self.sound))
		
class Dog(Animal):
	sound = 'Woof'

bolt = Dog('Bolt')
bolt.speak()
>> Woof! I am Bolt! Woof!

ISINSTANCE
=====
# To check if an object is instance of a class
print(isinstance(bolt, Animal))
>> True

print(isinstance(bolt, Dog))
>> True

class Cat(Animal):
	pass

print(isinstance(bolt, Cat))
>> False

#########################################################################################
MODULES
=====
# YOU CAN CREATE YOUR OWN MODULE

PUT IN CODE INSTALL FOR USER
=====
get_ipython().system('pip install BeautifulSoup4')

RANDOM
=====
import random

random.randint(1, 10)
>> 5
random.randint(1, 10)
>> 2
random.randint(1, 10)
>> 7

#############################################
DATETIME
=====
import datetime

now = datetime.datetime.now()
type(now)
>> <class 'datetime.datetime'>
# Why double datetime because the module datetime provides a datetime class

print(now) # This is accessing the __str__ method
>> 2020-07-19 17:41:12.923716

>>> now
# datetime.datetime(2020, 7, 19, 17, 41, 12, 923716)

now.year
>> 2020

INSERT YOUR OWN TIME
=====

print(a) # 0100-01-01 11:34:59

ADVANCE TIME
=====
# Two types of import

#1: import datetime only
import datetime
now = datetime.datetime.now()

#2: From the library datetime, import the class datetime
from datetime import datetime, date

today = datetime.today()
now = datetime.now()
cal = date.today() # datetime.date.today() works the same

print(today) # 2021-02-07 16:51:59.073516
print(now)   # 2021-02-07 16:51:59.073515
print(cal)   # 2021-02-07
# Both have the same but datetime.now() provides an optional timezone, and can give more precision.

print('\nTimetuple')
print(today.timetuple())  # time.struct_time(tm_year=2021, tm_mon=2, tm_mday=7, tm_hour=16, tm_min=51, tm_sec=59, tm_wday=6, tm_yday=38, tm_isdst=-1)
print(now.timetuple())    # time.struct_time(tm_year=2021, tm_mon=2, tm_mday=7, tm_hour=16, tm_min=51, tm_sec=59, tm_wday=6, tm_yday=38, tm_isdst=-1)
print(cal.timetuple())    # time.struct_time(tm_year=2021, tm_mon=2, tm_mday=7, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=38, tm_isdst=-1)
print(cal.timetuple()[0]) # Year: 2021
print(cal.timetuple()[1]) # Month: 2
print(cal.timetuple()[2]) # Day: 7
print(cal.timetuple()[3]) # 24-Hour: 0
print(cal.timetuple()[4]) # Minute: 0
print(cal.timetuple()[5]) # Second: 0
print(cal.timetuple()[6]) # Weekday: 6
print(cal.timetuple()[7]) # Day of year: 38
print(cal.timetuple()[8]) # Daylight saving flag: -1
# A value of 1 indicates that the daylight savings is in effect, 0 if daylight savings is not in effect and -1 if the information is not available.

print('\nFormats')
print(f'{now:%c}') # Sun Feb  7 16:51:59 2021
print('{0:%c}'.format(now)) # Locale’s date and time representation: Sun Feb  7 16:51:59 2021
print('{0:%a}'.format(now)) # Weekday Name (Abbr): Sun
print('{0:%A}'.format(now)) # Weekday Name (Full name): Sunday
print('{0:%w}'.format(now)) # Weekday Decimal: 0
print('{0:%d}'.format(now)) # Day of month (Zero-padded): 07
print('{0:%b}'.format(now)) # Month (Abbr): Feb
print('{0:%B}'.format(now)) # Month (Full name): February
print('{0:%m}'.format(now)) # Month (Zero-padded): 02
print('{0:%y}'.format(now)) # Year without century (Zero-padded): 21
print('{0:%Y}'.format(now)) # Year (Full): 2021
print('{0:%H}'.format(now)) # 24-Hour: 16
print('{0:%I}'.format(now)) # 12-Hour: 04
print('{0:%M}'.format(now)) # Minute (Zero-padded): 51
print('{0:%S}'.format(now)) # Second (Zero-padded): 59
print('{0:%f}'.format(now)) # Microsecond (Zero-padded): 073515
print('{0:%p}'.format(now)) # AM/PM: PM
print('{0:%z}'.format(now)) # UTC offset: None
print('{0:%j}'.format(now)) # Day of the year (Zero-padded): 038
print('{0:%U}'.format(now)) # Week of the year (Zero-padded); Sunday as the first day of the week: 06
print('{0:%W}'.format(now)) # Week of the year (Zero-padded); Monday as the first day of the week: 05
print('{0:%x}'.format(now)) # Locale’s appropriate date representation: 02/07/21
print('{0:%X}'.format(now)) # Locale’s appropriate time representation: 16:51:59

print('\nPrinting it')
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(now, "day", "month", "time"))
# The day is 07, the month is February, the time is 04:51PM.
print('{0:%A %Y-%m-%d %H:%M:%S}'.format(now)) # Sunday 2021-02-07 17:54:19
print(f'{now:%A %Y-%m-%d %H:%M:%S}') # Same result as above
print(now.strftime('%a')) # Sun

# Reference:
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
# https://stackoverflow.com/questions/15509617/how-to-obtain-the-day-of-the-week-in-a-3-letter-format-from-a-datetime-object-in
# https://docs.python.org/3.6/library/datetime.html#datetime.datetime.now
# https://overiq.com/python-3-time-module/

PARSING DATETIME
=====
# Ref: https://stackoverflow.com/questions/466345/converting-string-into-datetime
from datetime import datetime
datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

import time
time_object = time.strptime('1:33', '%M:%S')

# strptime = "string parse time"
# strftime = "string format time"

TIMEDELTA
=====
# days can be replaced by hours, minutes and seconds
print(now + datetime.timedelta(days = 5))
>> 2020-07-24 17:41:12.923716

ADVANCE TIMEDELTA
=====
timedelta(days: float=..., seconds: float=..., microseconds: float=..., milliseconds: float=..., minutes: float=..., hours: float=..., weeks: float=..., *, fold: int=...)

CALENDAR
=====
import calendar

Checking Leap Year
=====
print(calendar.isleap(2017)) # False
print(calendar.isleap(2020)) # True

Checking the time taken to run your program
=====
import time
start = time.time()

main()

print(f'The time taken: {(time.time() - start)*1000:.2f} ms')

#############################################
PSUTIL: GET CPU LOAD
=====
import psutil

def check_cpu_exceeded(percent):
	usage = psutil.cpu_percent(1)
	return usage > percent


if check_cpu_exceeded(75):
	print('ERROR: CPU is overloaded')
else:
	print('STATUS: OK')

# print('ERROR: CPU is overloaded' if check_cpu_exceeded(75) else 'STATUS: OK')

#############################################
SHUTIL: DISK SPACE AVAILIBILITY
=====
import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
	'''Return True if enough space, False otherwise'''
	du = shutil.disk_usage(disk)

	# Calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	# Calculate how many free gigabytes
	gb_free = du.free / 2**30
	if percent_free < min_percent or gb_free < min_absolute:
		return False
	return True

# Check for at least 2 GB and 10% free
if not check_disk_usage('/', 2, 10)
	print('Error: Not enough disk space')
	sys.exit(1)

print('STATUS: OK')
sys.exit(0)

#############################################
SYSTEM EXIT
=====
import sys

print('hello')
sys.exit(1) # 1 = Exit with error
sys.exit(0) # 0 = Just exit

#############################################
OS - Operating System
=====
import os
import sys

def check_reboot():
	'''Returns True if the PC has a pending reboot'''
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print('Pending reboot.')
		system.exit(1)
	print('Everything\'s ok')
	sys.exit(0)

main()

CHANGING THE FILE EXTENSION GENERALLY
=====
import os

filepath = '/fol.der/this.is.an.img.png'

# Our goal here is to change the png or jpeg behind into txt
'.'.join(os.path.split(filepath)[1].split('.')[:-1]) + '.txt'
# OUTPUT: 'this.is.an.img.txt'

CHANGING THE FULL DIRECTORY
=====
'.'.join(filepath.split('.')[:-1]) + '.txt'
# OUTPUT: '/fol.der/this.is.an.img.txt'

RUN A COMMAND ON THE OS
=====
# os.popen("INSERT_YOUR_COMMAND")
os.popen(calc) # Open calculator app

GETTING THE CURRENT PATH FOR THE CURRENT FILE
=====
os.getcwd()

RESTART THE CURRENT PROGRAM WIHOUT WHILE LOOP OR EXITING
=====
# Ref: https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input

import os, sys
# os.execl(sys.executable, sys.executable, *sys.argv)
os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
# But make sure there is no spaces in your path for the above code

import subprocess
subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"') # Not tried yet

COPYING STRING TO THE CLIPBOARD
=====
# Ref: https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard
import subprocess 
data = "hello world"
subprocess.run("clip", universal_newlines=True, input=data)

# Check step to unicode it and copy to clipboard by searching unicode with clipboard

CLEAR THE SCREEN OF THE TERMINAL
=====
# https://www.geeksforgeeks.org/clear-screen-python/
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

import os
cmd = 'cls' if os.name == 'nt' else 'clear'
# 'nt' stands for Windows

clear = lambda: os.system(cmd)
clear()

CHECKING IF A DIRECTORY IS A FOLDER
=====
os.path.isdir('src')

CHECKING IF A DIRECTORY IS A FILE
=====
os.path.isfile('src')

#########################################################################################
REGULAR EXPRESSIOB - REGEX
=====
!!! MUST import re
# Quick Guides
# ^			Matches the beginning of a line
# $			Matches the end of the line
# .			Matches any character
# \s		Matches whitespace
# \S		Matches any non-whitespace character
# *			Repeats a character zero or more times
# *?		Repeats a character zero or more times (non-greedy)
# +			Repeats a character one or more times
# +?		Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# (			Indicates where string extraction is to start
# )			Indicates where string extraction is to end

# More info - https://docs.python.org/3/howto/regex.html

re.search() vs str.find()
=====
'''
re.search() return boolean value
re.findall() return the matching string
'''
# To check whether a string matches regular expression
# similar to the find() method for string
handler = open('test.txt')

for line in handler:
	line = line.rstrip()
	if re.search('From:', line):
		print(line)

# Compared to find()
# find('Abc') return the index of the 'A' in 'Abc' 
handler = open('test.txt')

for line in handler:
	line = line.rstrip()
	if line.find('From:') >= 0:
		print(line)

re.findall()
=====
# To extract portions of string that matches regular expression
# similar to combination find() and slicing eg. sentence[3:9] method but more powerful
# More info on 'Extracting Data' below

re.search() vs str.startswith()
=====
h = open('test.txt')

for ln in h:
	ln = ln.rstrip() 
	# '^F' here means starts with the char 'F'
	if re.search('^From:', ln):
		print(line)

# Compared to startswith()
for ln in h:
	ln = ln.rstrip()
	if ln.startswith('From:'):
		print(ln)

Wild-Card Character
=====
re.search('^X.*:', line)

# '.' = dot means any character
# '*' = zero or more times
# '^X.*' means we are looking for line that begins with 'X' followed by any number of characters
# and followed by colon

# Examples of line that matches
'X-Sieve:'
'X-DSPAM-Result:'
'X-DSPAM-Confidence:'
'X-Content-Type-Message-Body:'

Fine-Tuning by excluding line that has spaces
=====
# Example of line we want to exclude
'X-Plan A with new timetable:'

re.search('^X-\\S+:')
# Double slash or single slash also work
# \S 	= non-whitespace character
# '+' 	= oen or more time
# '\S+' = Greater than or equal to 1 non-whitespace character
# We want an 'X' followed by '-' followed by any non-white special character one or more time
# and followed by a colon

Extracting Data
=====
# SQUARE BRACKET
[0-9] 	= one digit
[0-9]+ 	= '+' sign means one or more digits

x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
>> ['2', '19', '42']
# Notice that the list is array of strings

# If nothing is found, an empty list is returned
z = re.findall('[AEIOU]+', x)
print(z)
>> []

# Example 2
x = 'I AM tHE beST haha HAHA haZ19Zz' # Never been tbh, or not yet :))
y = re.findall('[A-Z]+', x)
print(y)
>> ['I', 'AM', 'HE', 'ST', 'HAHA', 'Z', 'Z']

Greeding matching
=====
# Returns the largest possible matching value
'^F.+:'
# Above means find if the string starts with character 'F' followed by any character one or more time
# and then starts with a colon

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
>> ['From: Using the :']
# Instead of ['From:'], it returns the biggest possible value
# Both the asterisk '*' and the plus '+' push outwards as far as push as wide as they can.

Non-Greedy Matching
=====
# To solve the problem above
'^F.+?'
# with a '?' behind '*' or '+', they dont push out
# Above means find if the string starts with character 'F' followed by any character one or more time
# BUT don't be greedy and followed by ':'

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
>> ['From:']

Fine-Tuning String Extration
=====
# Say we want to extract email from a string
x = 'From github@gmail.com Sat Jan 5 09:12:22 2020'
y = re.findall('\\S+@\\S+', x)
print(y)
>> ['github@gmail.com']
# Above is greedy matching to left and to the right

# If use non-greedy matching '?'
y = re.findall('\\S+@\\S+?', x)
>> ['github@g']

y = re.findall('\\S@\\S+?', x)
>> ['b@g']

x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@gmail.com'
y = re.findall('\\S+@\\S+', x)
>> ['john@gmail.com', 'github@gmail.com']

y = re.findall('\S?@\S+', x)
>> ['n@gmail.com', 'b@gmail.com']

y = re.findall('\S+?@\S+?', x)
>> ['john@g', 'github@g']

Parenthesis '()'
=====
# inform re where to start and ends
'(' = starts at
')' = ends at

# Extracting the exact location in the string
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020'
y = re.findall('^From (\\S+@\\S+)', x)
# If the line starts with 'From', extract the data from \S+@\S+
>> ['john@gmail.com']

x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@gmail.com'
y = re.findall('^From (\\S+@\\S+)', x)
>> ['john@gmail.com']
# Notice that github@gmail.com is not included in the list y

# What happens without parenthesis
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@gmail.com'
y = re.findall('^From \\S+@\\S+', x)
>> ['From john@gmail.com']

Extracting domain name
=====
# Using the traditional way string slicing to get the mail domain
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@gmail.com'
atpos = x.find('@')
sppos = x.find(' ', atpos) # Find the index of the first ' ' after atpos
domain = x[atpos+1:sppos]
>> 'gmail.com'

# Using dual split
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@gmail.com'
email = x.split()[1]
domain = email.split('@')[1]
print(domain)
>> 'gmail.com'

# Using re.findall()
y = re.findall('^From \\S+@(\\S+)', x)

# Another regex version
'@([^ ]*)'
# Loop til find '@'
# [^ ] get all chars except a space = [\\S]
# also same as '@([\\S]*)'

x = 'From john@gmail.com Sat Jan 5 09:12:22 2020'
y = re.findall('@([^ ]*)', x)
>> ['gmail.com']

x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@yahoo.com'
y = re.findall('@([^ ]*)', x)
>> ['gmail.com', 'yahoo.com']

# To get the first mail domain only
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@yahoo.com'
y = re.findall('@([^ ]*)', x)[0]
>> 'gmail.com'

# Fine-tune this by using startign with 'From'
# So is the line does not have 'From' on the starting hand, it will skip it
x = 'From john@gmail.com Sat Jan 5 09:12:22 2020 to github@yahoo.com'
y = re.findall('^From .*@([^ ]*)', x)
>> ['yahoo.com']
# Get the second domain name

# To get the first domain name, we need to use non-greedy matching = '?'
y = re.findall('^From .*?@([^ ]*)', x)
>> ['gmail.com']

Extracting a floating value
=====
x = 'X-DSPAM-Confidence: 0.8765'
y = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', x)
>> 0.8765

x = 'X-DSPAM-Confidence: 0.8765x5'
y = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', x)
>> 0.8765
# Notice that 'x5' is not included

x = 'X-DSPAM-Confidence: 0.8765'
y = re.findall('^X-DSPAM-Confidence: ([0-9]+)', x)
>> 0
# Notice that '.8765' is not included

x = 'X-DSPAM-Confidence: 10.123'
>>> y = re.findall('([0-9]+)', x)
['10', '123']

Escape Character
=====
# '\'
# For eg '\$[0-9.]+' means check if there is a $ sign 
# As '$' is part of regex as well 
# '$' = Matches the end of the line
x = 'We bought the gift for $10.00'
y = re.findall('\$[0-9.]+', x)
# same as y = re.findall('\\$[0-9.]+', x)
>> ['$10.00']

#########################################################################################
SOCKETS
=====
import socket

Setting up a connection
=====
# NOT SENDING DATA, JUST SETTING UP CONNECTION
# Like dialing a phone number

# Below line is setting up a connection but not yet connected
# A stream means it's a series of characters that just keep coming back
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Actual connection with parameters domain name and port number
mysocket.connect( ('data.pr4e.org', 80) )
# mysocket.connect((host, port number))

TELNET
=====
# In Windows, need download, Linux, Mac has this in-built
$ telnet data.pr4e.org 80

'''
GET http://data.pr4e.org/page.htm HTTP/1.0
'''

HTTP REQUESTS
=====
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# \r\n = Enter
mysock.send(cmd)

while True:
	# Getting 512 characters
	data = mysock.recv(512)

	# If we get no data = end of file || end of transmission
	if(len(data) < 1):
		break
	print(data.decode())
mysock.close()

# Output Metadata followed by the html text
'''
HTTP/1.1 200 OK
Date: Sun, 14 Mar 2010 23:53:41 GMT
Server: Apache
Last-Modified: Tue, 29 Dec 2009 01:32:12 GMT
ETag: "412ied8-a3-emi23s"
Accept-Ranges: bytes
Content-Length: 167
Connection: close
Content-Type: text/plain

This is the text output. Today I went to supermarket to buy ice-cream
It was a windy day...
I saw a cashier running to the toilet. I ran up as well.
Seems like there is free toilet paper.
'''

Check status
=====
1. F12
2. Network
3. Header
4. Status Code: 200 
# 200 = Ok
# 404 = Error
# 302 = Redirect to another page

#########################################################################################
UNICODE
=====
# Unicode is this universal code for hundreds of millions of different characters and hundreds of different character sets. Not 128 like ASCII

Unicode Characters and Strings
=====
# Representing simple strings
# 'ord' is ordinal, displaying the number correspond to the letter or special characters in ASCII table
# ord() function displays the numeric value of a simple ASCII character

# Note that the upper case character has lower ordinal compared to the lower case
print(ord('H'))
>> 72
print(ord('h'))
>> 104

# '\n' is a new line and '\n' is a single character
print(ord('\n'))
>> 10

UTF-8
=====
# Recommended if you're moving a file between two systems. Or if you're moving network data between two systems

Python2 vs Python3
=====
# In Python3, all strings are unicode

# Python2
x = '여보세요'
type(x)
>> <type 'str'>

x = u'여보세요'
type(x)
>> <type 'unicode'>

# Python3
x = '여보세요'
type(x)
>> <type 'str'>

x = u'여보세요'
type(x)
>> <type 'str'>

Byte Strings
=====
# Raw, unencoded string
# Might be UTF-8, UTF-16, UTF-32 or even ASCII, we do not know what the encoding is

# Python2
x = b'abc'
type(x)
>> <type 'str'>

# Python3
x = b'abc'
type(x)
>> <type 'bytes'>

decode()
=====
# By default, Python decodes them to UTF-8 or ASCII 

while True:
	# Getting 512 characters
	data = mysock.recv(512)

	# If we get no data = end of file || end of transmission
	if(len(data) < 1):
		break
	mystring = data.decode()
	print(mystring)

mysock.close()

type(data)
>> <type 'bytes'>

type(mystring)
>> <type 'unicode'>

encode()
=====
# Takes strings and turn them into bytes

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

type(cmd)
<type 'bytes'>

Unicode [REF: COPY TO CLIPBOARD]
=====
# Ref: https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
print u"Stöcker"                # works
print "Stöcker".decode("utf-8") # works
print "Stöcker"                 # fails

RETRIEVING WEB PAGES
=====
# USING URLLIB

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())

# Word counting
counts = dict()

for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

PARSING WEB PAGES
=====
# While parsing HTML, there are many errors. To solve this problem we need to import external lib

# Install Beautiful Soup
1. Open CMD
2. Type... 

# For Python 2
pip install beautifulsoup4

# For Python 3
pip3 install beautifulsoup4

3. import it into your script
from bs4 import BeautifulSoup

Getting href link
=====
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
# read() return a combined string all in one

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
	# Get the href key or none
	print(tag.get('href', None))

'''
OUTPUT
=====
Enter URL: https://www.coursera.org/learn/python-network-data/lecture/1oHBS/12-5-parsing-web-pages

https://www.facebook.com/Coursera
https://www.linkedin.com/company/coursera
https://twitter.com/coursera
https://www.youtube.com/user/coursera
https://www.instagram.com/coursera/

'''

To ignore SSL certificate error
=====
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
# read() return a combined string all in one

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
	# Get the href key or none
	print(tag.get('href', None))

# You will need to decode the tag by x = tag.decode() if you want x to be string type

Retrieve all the anchor tag
=====
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

#########################################################################################
Data On The Web
=====
# HTML Request/Response can be understood because of an agreed way to represent data going between applications and across networks
# Common format: JSON, XML

Wire Protocol
=====
# eg. Python's dict sending via internet to Java's hashmap
# Incompatible, so "Wire Protocol" is used, sending data on some format we agreed on

Python -> (Serialize) -> XML / JSON -> (De-serialize) -> Java

XML vs JSON
=====
# XML is older, complex
# JSON is modern and light-weight

XML
=====
# Extensible Markup Language
# Marking up data to send across the network
# Help information systems share structured data
# Simplified version of SGML(Standard Generalized Markup Language)

XML Elements or nodes
=====
<people>
	<person>
		<name>Chuck</name>	# <-- Simple element
		<age>50</age>		# <-- Simple element
		<phone>123</phone>	# <-- Simple element
	</person>
	<person>				# -+
		<name>Adam</name>	#  |
		<age>30</age>		#  +--> Complex element
		<phone>456</phone>	#  |
	</person>				# -+
</people>

XML Basics
=====
<person>					# Start tag
	<name>Chuck</name>		# Chuck = Text content
	<phone type="intl">		# type="intl" = Attribute (Always at the start tag)
		123 456
	</phone>
	<email hide="yes" />	# <email ... /> = Self-closing tag
</person>					# End tag

XML as Paths
=====
<a>
	<b>X</b>
	<c>
		<d>Y</d>
		<e>Z</e>
	</c>
</a>

/a/b 	= X
/a/c/d 	= Y
/a/c/e 	= Z

XML Schema
=====
# Describing a "contract" as to what is acceptable XML
# Description of the legal format of an XML document

XML Validation
=====
# Act of verifying the data is in the right format
# XML document and XML Schema Contract are send to the validator to process XML validation

# XML Document
<person>
	<lastname>Chuck</lastname>
	<age>50</age>
	<dateborn>1990-01-31</dateborn>
</person>

# XML Schema Contract
<xs:complexType name="person">
	<xs:sequence>
	<xs:element name="lastname" type="xs:string"/>
	<xs:element name="age" type="xs:integer"/>
	<xs:element name="dateborn" type="xs:date"/>
	</xs:sequence>
</xs:complexType>

XSD XML Schema (W3C Spec)
=====
# W3C = World Wide Web Consortium
# Commonly called XSD due to the extension *.xsd

XSD Constraints
=====
<xs:element name="person">
	</xs:complexType>
		<xs:sequence>
		<xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1"/>
		<xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10"/>
		</xs:sequence>
	</xs:complexType>
<xs:element>

<person>
	<full_name>Tove Refsners</full_name>
	<child_name>Adam</child_name>
	<child_name>Jim</child_name>
	<child_name>Loli</child_name>
	<child_name>Borg</child_name>
</person>

XSD Data Types
=====
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="price" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>
<xs:element name="age" type="xs:positiveInteger">


<customer>John Smith</customer>
<start>2002-12-25</start>
<startdate>2002-11-13T09:30:10Z</startdate> # Z = Timezone
<price>999.50</price>
<weeks>30</weeks>

Enumerate
=====
<xs:element name:"Country">
	<xs:restriction base="xs:string">
		<xs:enumeration value:"FR"/>
		<xs:enumeration value:"DE"/>
		<xs:enumeration value:"ES"/>
		<xs:enumeration value:"UK"/>
		<xs:enumeration value:"US"/>
	</xs:restriction>
</xs:element>

# Only can use the location that is from the enum list

Unlimited maxOccurs
=====
<xs:element: name="item" maxOccurs="unbounded"/>

Required data
=====
<xs:attribute name="orderid" type="xs:string" use="required"/>

PARSING XML
=====
import xml.etree.ElementTree as ET

data = '''<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 234 567 890
	</phone>
	<email hide="yes">
</person>'''

tree = ET.fromstring(data)
# Above line could traceback if your XML is bad

print('Name:', tree.find('name').text)
>> Chuck

print('Attr:', tree.find('email').get('hide'))
# Get the value of the attribute
>> yes

findall()
=====
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
# Above will insert all the users into the list

print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

#########################################################################################
JavaScript Object Notation (JSON)
=====
# Unlike XML, JSON is like we're not going use the Python syntax, we're not going use the Java syntax, but we are going to use the JavaScript syntax in the middle. So JSON is very native to JavaScript.

Dictionary
=====
import json

data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

Saving the dictionary as JSON
=====
import json
   
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
   
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)


List
=====
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

Application Programming Interfaces (API)
=====
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # return dict()
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

'''
Output
Enter location: Kuala Lumpur
Retrieving http://py4e-data.dr-chuck.net/json?address=Kuala+Lumpur&key=42
Retrieved 1623 characters
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Kuala Lumpur",
                    "short_name": "Kuala Lumpur",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Federal Territory of Kuala Lumpur",
                    "short_name": "Federal Territory of Kuala Lumpur",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Malaysia",
                    "short_name": "MY",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 3.2433789,
                        "lng": 101.758529
                    },
                    "southwest": {
                        "lat": 3.0336329,
                        "lng": 101.61545
                    }
                },
                "location": {
                    "lat": 3.139003,
                    "lng": 101.686855
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 3.2433789,
                        "lng": 101.758529
                    },
                    "southwest": {
                        "lat": 3.0336329,
                        "lng": 101.61545
                    }
                }
            },
            "place_id": "ChIJ5-rvAcdJzDERfSgcL1uO2fQ",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}
lat 3.139003 lng 101.686855
Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia
'''

Updated Version
=====
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	url = serviceurl + urllib.parse.urlencode({'address': address})

	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

Twitter API
=====
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])

#########################################################################################
MODULES & LIBRARY
=====
# You can create your own modules, say "SpecialFind.py"
secretCode = '012098qwer'

def findIndex(sequence, target):
    for index, element in enumerate(sequence):
        if element == target:
            return index
    # Return -1 when not found the specified element            
    return -1

Importing Modules
=====
# In the other python script file
import SpecialFind

fruit = ['Apple', 'Orange', 'Banana', 'Watermelon']
fruitToFind = 'Watermelon'

indexOfFruitToFind = SpecialFind.findIndex(fruit, fruitToFind)

print(indexOfFruitToFind) # 3

Make Abbreviation For the Module Imported
=====
import SpecialFind as abc
indexOfFruitToFind = abc.findIndex(fruit, fruitToFind)
print(abc.secretCode) # 012098qwer

Only Import The Selected Function From The Module
=====
from SpecialFind import findIndex as fi # 'as fi' is optional
indexOfFruitToFind = fi(fruit, fruitToFind)
print(secretCode) # NameError: name 'secret' is not defined

Only Import The Specified Function And Variable From A Module
=====
from SpecialFind import findIndex as fi, secretCode
indexOfFruitToFind = fi(fruit, fruitToFind)
print(secretCode) # 012098qwer

Importing everything from a module
=====
from SpecialFind import *
indexOfFruitToFind = findIndex(fruit, fruitToFind)
print(secretCode) # 012098qwer

indexOfFruitToFind = SpecialFind.findIndex(fruit, fruitToFind) # ERROR: 'SpecialFind.' is not needed
print(SpecialFind.secretCode) # ERROR: 'SpecialFind.' is not needed

GETTING THE FILE PATH OF THE MODULE
=====
import datetime
import os
import calendar

print(datetime.__file__)
print(os.__file__)
print(calendar.__file__)

# C:\Users\Acer\AppData\Local\Programs\Python\Python39\lib\datetime.py
# C:\Users\Acer\AppData\Local\Programs\Python\Python39\lib\os.py
# C:\Users\Acer\AppData\Local\Programs\Python\Python39\lib\calendar.py

GETTING THE SOURCE_CODE OF A FUNCTION
=====
# INSPECT LIBRARY
# Need to install first = pip install inspect
import inspect
lines = inspect.getsource(FunctionName)
print(lines)

NUMPY
=====
import numpy as np

rolls = np.random.randint(low=1, high=6, size=10)
print(rolls)
>> array([1, 5, 3, 4, 2, 2, 1, 1, 1, 4])

rolls.mean()
>> 2.4

type(rolls)
>> 'numpy.ndarray'

ls = rolls.tolist()
print(ls) # [1, 5, 3, 4, 2, 2, 1, 1, 1, 4]

[3, 4, 1, 2, 2, 1] + 10
# ERROR BUT WITH NUMPY BROADCAST CAN
rolls + 10
array([11, 15, 13, 14, 12, 12, 11, 11, 11, 14])

# At which indices are the dice less than 3?
rolls < 3
array([ True, False, False, False,  True,  True,  True,  True,  True, False])

NUMPY: Creating a matrix
=====
xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
# print("xlist = {}\nx =\n{}".format(xlist, x))

print("xlist =", xlist)
print("x =\n" + str(x))
print(type(x))

"""
xlist = [[1, 2, 3], [2, 4, 6]]
x =
[[1 2 3]
 [2 4 6]]
<class 'numpy.ndarray'>
"""

# Get the last element of the second row of our numpy array
x[1,-1] # 6

# Get the last element of the second sublist of our nested list?
xlist[1,-1] # Type_Error
xlist[-1][-1]

SYSTEM
=====
import sys
print(sys.version_info)
s = sys.version_info
print(f'The version of Python Kaggle is using: {s[0]}.{s[1]}.{s[2]}')
"""
sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
The version of Python Kaggle is using: 3.7.9
"""

TENSORFLOW
=====
import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
print(a + b) # tf.Tensor(2, shape=(), dtype=int32)

MATPLOTLIB
=====
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    
    # Complete steps 2 and 3 here
    graph.set_ylim(0)
    graph.set_ylabel('Balance')
    graph.set_xlabel('Number of pulls')
    
    # Formatting
    graph.yaxis.set_major_formatter(mp.ticker.FuncFormatter('${}'.format))
    
    """
    def prettify_graph(graph):
        graph.set_title("Results of 500 slot machine pulls")
        
        # Make the y-axis begin at 0
        graph.set_ylim(bottom=0)
        
        # Label the y-axis
        graph.set_ylabel("Balance")
        
        # Bonus: format the numbers on the y-axis as dollar amounts
        # An array of the values displayed on the y-axis (150, 175, 200, etc.)
        ticks = graph.get_yticks()
        
        # Format those values into strings beginning with dollar sign
        new_labels = ['${}'.format(int(amt)) for amt in ticks]
        
        # Set the new labels
        graph.set_yticklabels(new_labels)
    """
    
    
graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph


WINSOUND
=====
# Ref: https://docs.python.org/3/library/winsound.html
# Ref: https://stackoverflow.com/questions/44472162/how-do-play-audio-playsound-in-background-of-python-script

import winsound
list_of_sounds = ['SystemAsterisk', 'SystemExclamation', 'SystemExit', 'SystemHand', 'SystemQuestion']
# Only SystemHand is different than the rest

# Play asynchronously while running another code
winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC | winsound.SND_ALIAS )

# Play the sound before going to the next code
winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)

# To stop playing the sound
winsound.PlaySound(None, winsound.SND_ASYNC)

# Beep beep sound where freq from 37 to 32767, and duration in ms
winsound.Beep(frequency, duration)
winsound.Beep(1000, 2000) # 1000hz and 2000 means 2 seconds

BASE64 Image
=====
import base64

with open("image.ext", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())


# Decode it
import cStringIO
import PIL.Image

# assume data contains your decoded image
file_like = cStringIO.StringIO(data)

img = PIL.Image.open(file_like)
img.show()

COPY
=====
# https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper/17246744#17246744
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

# Using normal assignment operatings to copy:
d = c
print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]

# Using a shallow copy:
d = copy.copy(c)
print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]

# Using a deep copy:
d = copy.deepcopy(c)
print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object

# Getting the address in hex format
d = c
hex(id(c)) == hex(id(d))      # True - d is the same object as c

ENCODING AND DECODING IN HEX
=====
# Encoding
"hello".encode("utf-8").hex()
# '68656c6c6f'

# Decoding
bytearray.fromhex("68 65 6C 6C 6F").decode()
bytearray.fromhex("68 65 6c 6c 6f").decode()
bytearray.fromhex("68656c6c6f").decode()
bytes.fromhex('68656c6c6f').decode('utf-8')
# 'hello'


SIMPLEJSON
=====
# pip install simplejson
# How to export the json null data from df or python that has None value in it?
df_vals = list(df.T.to_dict().values())
simplejson.loads(simplejson.dumps(df_vals, ignore_nan=True))

# OR...

dic = df.to_dict('index')
df_vals = list(dic.values())
simplejson.loads(simplejson.dumps(df_vals, ignore_nan=True))
