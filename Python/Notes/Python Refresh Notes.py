# Last updated: Sat, February 06, 2021 - 23:50

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

LOGICAL OPERATORS
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

x = [1,2,3]
tmp = x
print(tmp is x) # Ouput: True

y = [1,2,3]
print(tmp is y) # Output: False
print(tmp == y) # Output: True

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
elif x > 6:
	print(' More than 6')
else:
	print('Something else')

print("even" if x % 2 == 0 else "odd")
>> odd

COMMENT
=====
# This is a comment

'''
Here lies comment or documentary
'''

TYPE CONVERSION
=====
x = float(1)
>> x 
>> 1.0

x = str(x)
x = int(x)
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
x = 'John'

try:
	x = int(x)
	print('Done converting')
except:
	print(x, "is not a number")
finally:
	print('Goodbye')
	quit() # <## completely exit the program

FUNCTION
=====
def add(x, y):
	return x + y

sum = add(2, 5)
print(sum)
>> 7

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

WHILE LOOP WITH BREAK & CONTINUE
=====
# Indefinite loop
while True:
	line = raw_input("> ") # For python 3 change to input()
	if(line[0] == '#'):
		continue
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

random.randrange(1, 100):
>> 23

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
total = 12.259
round(total, 2)
>> 12.26
total
>> 12.259
total = round(total, 2)
total
>> 12.26

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

print(tmp.count('l'))
>> 3

MATH LIBRARY
=====
import math

math.sqrt(4) # Output: 2
math.sin(0)	 # Output: 0.0
math.cos(0)	 # Output: 1.0

DISPLAY ALL THE METHODS AVAILABLE FOR VARIABLE
=====
dir(tmp)
>> ['capitalize', 'casefold', 'center', ...]

FIND THE INDEX
=====
fruit = 'banana'
         012345
pos = fruit.find('na')
>> 2

aa = fruit.find('z')
>> #1

info = 'From geniusGoogle@gmail.com GeniusUser'
pos = info.find('@')
# Second parameter taken in means where to starts
secondPos = info.find(' ', pos)
host = info[pos+1 : secondPos]
>> gmail.com

STRING UPPER & LOWER
=====
tmp.upper()
>> HELLO WORLD

tmp.lower()
>> hello world

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
re.sub(r'[^\w]', ' ', s)
re.sub(r'[\W]', ' ', s)
>> 'how much for the maple syrup   20 99  That s ridiculous   '

re.sub(r'[^\w\S]', ' ', s)
>> "howmuchforthemaplesyrup?$20.99?That'sridiculous!!!"

re.sub(r'[^\w\s]', '', s)
>> 'how much for the maple syrup 2099 Thats ridiculous'

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

Timed like this:
python #mtimeit #s"import time_functions" "time_functions.a('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.b('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.c('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.d('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.e('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.f('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.g('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.h('abc&def#ghi')"
python #mtimeit #s"import time_functions" "time_functions.i('abc&def#ghi')"

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

JOIN
=====
# Note: str.join(iterable)
lst = "The string is splitted into a list".split(" ")
lst
>> ['The', 'string', 'is', 'splitted', 'into', 'a', 'list']
finalString = "#".join(lst)
finalString
>> 'The#string#is#splitted#into#a#list'

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
# A COLLECTION
friends = ['Ali', 'Ah Kau', 'Muthu']

# A list can be included with diff type of data
mix = ['Ali', 29, 175.5, 89.2, 'Sarah']

# List in a list
ll = [1, [23,2], 55]

# Empty list
emp = []

for data in mix:
	print(data)

CREATE A LIST OF NUMBER ASCENDING WIHOUT LOOP
=====
num_list = list(range(100))
print(num_list) # [0, 1, 2, ..., 99]

LOOKING INSIDE THE LISTS
=====
friends = ['Ali', 'Ah Kau', 'Muthu']
print(friends[2])
>> Muthu

print(friends[:2])
>> ['Ali', 'Ah Kau']

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

LIST COUNTING
=====
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

SORTED
=====
# This function return you a new sorted list without modifying the original list
names = ['Sarah', 'John' ,'Ali']
newList = sorted(names)
newList
>> ['Ali', 'John', 'Sarah']
names
>> ['Sarah', 'John' ,'Ali']

SORTED BY KEY
=====
# What if we want to sort the list according to the length of the word
names = ['Carlos', 'Pewdiepie' ,'Ali']
newList = sorted(names, key=len)
newList
>> ['Ali', 'Carlos', 'Pewdiepie']

BUILD-IN FUNCTION FOR LIST
=====
nums = [12,25,38,49,53,6]
len(nums)
>> 6
max(nums)
>> 53
min(nums)
>> 6
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

# Print number which is divisible by 3
print([x for x in range(0, 40) if x % 3 == 0])
>> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]

# MORE LIST METHODS
list.reverse() # Reverses the order of items of the list
list.clear() # Removes all the items of the list
list.copy() # Creates a copy of the list
list.extend(other_list) # Appends all the elements of other_list at the end of list

#########################################################################################
DICTIONARIES
=====
# IT HAS LABEL TO IT
# KEY-VALUE PAIR LIKE HASHMAP
# Not in order
purse = {'RM50': 1, 'RM20': 5, 'RM5': 3}
purse['RM5'] # 3
purse.get('RM5') # 3
purse.get('RM1', 0) # 0 because default value = 0 when the key 'RM1' is not found

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

DELETING KEY WITH ITS VALUE
=====
del wallet['RM50']
print(wallet)
>> {'RM20': 10, 'RM5': 7, 'RM1': 12}

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

#########################################################################################
TUPLES
=====
# More efficient version of list that you cant modify
# We can say the position inside the tuple has its meaning
# immutable, cannot be sorted like list

x = ('Ali', 'Sarah', 'Abu')
x[1]
>> 'Sarah'

num = (55,2,45,122,98)
print(num)
>> (55,2,45,122,98)

print(max(num))
>> 122

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

#########################################################################################
ENUMERATE WITH TUPLE
=====
# The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.
players = ["Ali", "Sarah", "Ah Meng"]
for index, person in enumerate(players):
	print("{} - {}".format(index+1, person))

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
SETS
setA = {123, 23, 65}

set('abc').intersection('cbs').
>> {'b', 'c'}

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

# new set with elements common to s and t
s.intersection(t)
s & t

# new set with elements in s but not in t
s.difference(t)
s - t

# new set with elements in either s or t but not both
s.symmetric_difference(t)
s ^ t

# new set with a shallow copy of s
s.copy()

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

#########################################################################################
Object-Oriented Programming (OOP)
=====
type("x")
# >> <class 'str'>

dir(int)
# >> displays list of methods for int

help(int)
# >> displays list of documentation for int

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
DATE TIME
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

TIMEDELTA
=====
# days can be replaced by hours, minutes and seconds
print(now + datetime.timedelta(days = 5))
>> 2020-07-24 17:41:12.923716

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