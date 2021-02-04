# Last updated: Thu, February 04, 2021 - 11:14

############################################################
# Reference: Coursera - Google Python Crash Course Week 1 Cheat Sheet
# Arithmetic Operators
"""
a + b   : Adds a and b
a - b   : Subtracts b from a
a * b   : Multiplies a and b
a / b   : Divides a by b
a ** b  : Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the
        square root of a)
a // b  : The integer part of the integer division of a by b
a % b   : The remainder part of the integer division of a by b
"""
print("\nArithmetic Operators")

# Addition
def add(num1, num2):
    return num1 + num2
print("The sum is", add(3,4)) # Output: The sum is 7

# Division
print(5/2)  # Output: 2.5
print(5//2) # Output: 2

# Remainder
print(5%2)  # Output: 1

# Power
def pow(num1, num2):
    print(num1**num2)
pow(2,5) # Output: 32

# Python math library's power function
import math
print(math.pow(2,3))        # Output: 8.0
print((int)(math.pow(2,3))) # Output: 8

############################################################
# Comparison Operators
"""
Reference: https://www.programiz.com/python-programming/operators
x == y  : Equals
x != y  : Not Equals
x < y   : Lesser than
x > y   : Greater than
x <= y  : Lesser than or Equal to
x >= y  : Greater than or Equal to
"""
print("\nComparison Operators")

x = 5
y = 2
print(x == y)   # Output: False
print(x != y)   # Output: True
print(x < y)    # Output: False
print(x > y)    # Output: True
print(x <= y)   # Output: False
print(x >= y)   # Output: True

# Difference
def diff(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1
print(diff(5, 10))  # Output: 5

# What makes python special when comparing between numbers
x = 1; y = 2; z = 3
print(x < y < z)    # Output: True

x = 1; y = 3; z = 3
print(x > y == z)   # Output: False

############################################################
# Logical Operators
"""
Boolean values
1. True
2. False

and : True when both operands are True
or  : True when one of the operands is True
not : True when the operand is False [Negation/Opposite of the operand]
Precedence: not > and > or
"""
print('\nLogical Operators')

# NOTE: Make sure the T and F are capitalized
x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not y)    # Output: True

############################################################
# Bitwise Operators
"""
Reference: https://www.geeksforgeeks.org/python-bitwise-operators/
x & y   Bitwise AND
x | y   Bitwise OR
~x      Bitwise NOT
x ^ y   Bitwise XOR
x>>     Bitwise right shift
x<<     Bitwise left shift

Bitwise AND
0 & 0   : 0
0 & 1   : 0
1 & 0   : 0
1 & 1   : 1

Bitwise OR
0 | 0   : 0
0 | 1   : 1
1 | 0   : 1
1 | 1   : 1

Bitwise NOT
~0      : -1
~1      : -2
NOTE: More detailed explanation below

Bitwise XOR
0 ^ 0   : 0
0 ^ 1   : 1
1 ^ 0   : 1
1 ^ 1   : 0

Bitwise left shift
a = 5 = 0000 0101
b = -10 = 1111 0110
NOTE: The first '1' on the far left side is -256
NOTE: -10 = 1111 0110 because (-128 + 64 + 32 + 16 + 4 + 2)
a << 1 = 0000 1010 = 10
a << 2 = 0001 0100 = 20 

b << 1
1111 0110 << 1 = 1110 1100 (-128 + 64 + 32 + 8 + 4) = -20
b << 2
1111 0110 << 2 = 1101 1000 (-128 + 64 + 16 + 8) = -40

Bitwise right shift
a = 5 = 0000 0101
a >> 1 = 0000 0010 = 2

Logic Gates Basic
Reference: https://www.geeksforgeeks.org/logic-gates-in-python/

Converting decimals to binary
Reference: https://realpython.com/python-data-types/
x = 9
bin(x) = 0b1001

What is bit shifting for?
Reference: https://stackoverflow.com/questions/520625/have-you-ever-had-to-use-bit-shifting-in-real-projects
1. Need bit-shifting for nearly all your arithmetic when coding in a system that does not have floating point supported in hardware
2. Generate hashes
3. Polynomial arithmetic (CRC, Reed-Solomon Codes are the mainstream applications)
"""
print("\nBitwise Operators")

# Bitwise AND operator
"""
a = 6 = 0110 (Binary)
b = 5 = 0101 (Binary)

a & b = 0110
         &
        0101
      = 0000
      = 0 (Decimal)
"""

# Bitwise NOT operator
"""
a = 9 = 1001 (Binary)

~a = ~1001
   = -(1001 + 1)
   = -(1010)
   = -10 (Decimal)
"""
a = 9
print(bin(a)) # Output: 0b1001
b = ~a
print(bin(b)) # Output: -0b1010 

############################################################
# Assignment Operators
"""
x = 1   : x = 1
x += 2  : x = x + 2
x -= 3  : x = x - 3
x *= 4  : x = x * 4
x /= 5  : x = x / 5
x %= 6  : x = x % 6
x //= 7 : x = x // 7
x **= 8 : x = x ** 8

BITWISE
x &= 9  : x = x & 9
x |= 8  : x = x | 8
x ^= 7  : x = x ^ 7
x >>= 2 : x = x >> 2
x <<= 3 : x = x << 3 
"""
print('\nAssignment Operators')

# Initialize x first
x = 3

# Adding it
x += 2
print(x) # Output: 5

# Power
x **= 2
print(x) # Output: 25 

# Division: Getting the Numerator
x //= 10
print(x) # Output: 2

# Multiplication
x *= 8
print(x) # Output: 16

# Complete division
x /= 10
print(x) # Output: 1.6

# Assigment operator with bitwise
# XOR Example
x = 1
x ^= 0
print(x) # Output: 1

############################################################
# Identity Operators
"""
Reference: https://www.programiz.com/python-programming/operators
is      : True if the operands are identical (refer to the same object)
is not  : True if the operands are not identical (do not refer to the same object)

"""
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = "Hello"
x3 = [1,2,3]
y3 = [1,2,3]
tmp = x3

print(x1 is not y1) # Output: False
print(x2 is y2)     # Output: True
print(x3 is y3)     # Output: False
# Reason: They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.
print(tmp is x3)    # Output: True
print(x3 is tmp)    # Output: True

import random
random.shuffle(tmp) # When tmp is called to be shuffled, the list object that x3 and tmp are referenced to will be shuffled.
print(tmp)          # Say [1, 3, 2]
print(x3)           # Same as tmp
print(x3 is tmp)    # Output: True. Although it is shuffled the reference remained the same
# NOTE: Variable names in python are only references to objects, x3 and tmp are referenced to the same list object.

############################################################
# Memebership Operators
"""
Reference: https://www.programiz.com/python-programming/operators
Used for string, list, tuple, set and dictionary

in      : True if value/variable is found in the sequence
not in  : True if value/variable is not found in the sequence
"""

x = 'Hello World'
y = {1: 'a', 'b': 2}
z = (1, 2, 'Foo')
w = [1,'Bar',3]

print('H' in x)         # Output: True
print('world' not in x) # Output: True
print(1 in y)           # Output: True
print('a' in y)         # Output: False
print('b' in y)         # Output: True
print(2 in z)           # Output: True
print('Bar' in w)       # Output: True

############################################################
# Last updated: Thu, February 04, 2021 - 11:14
############################################################