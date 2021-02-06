# Last updated: Sat, February 06, 2021 - 16:20

quit()

#8 String: Put a word repeatedly in each of the slit between the letters
# Eg: ABC would output `AABCBABCC`
text = 'ABC'
print(text.join(reversed(text)))

#7 String: Print a mirror text without the need of for loop
text = 'Abc' # Output should be 'AbccbA'
print(text + text[::-1])

#6 String: Palindrome
# Palindrome: sequence of characters which reads the same backward as forward
userInput = input('Enter a sentence/word: ') # Try racecar
print(userInput == "".join(reversed(userInput))) # True
print(userInput == userInput[::-1]) # True
'''Explanation : Extended slice offers to put a “step” field as [start,stop,step], and giving no field as start and stop indicates default to 0 and string length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.'''

#5 List: Sum all the even number
nums = [5, 1, 20, 88, 16, 17, 23, 25, 66, 45, 86, 72]
sum = 0

for i in nums:
    if i%2 == 0: sum += i

print(sum) # 348

#4 If-Else: Leap year
year = int(input('Year: '))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('{year} is a loop year.')
else:
    print('{year} is not a loop year.')

#3 Modulus: Finding day of the week
start = int(input("Starting day: "))
length = int(input("Holiday length: "))

dayOfWeek = (start + length) % 7

def getDOW(x=0):
    return "The day is: " + {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }.get(x, 'Doomsday') + "!"

print(getDOW(dayOfWeek))

#2 Modulus: Finding the hours
start = int(input("Current time (hour): "))
length = int(input("How long you plan study (hour): "))
end = (start + length) % 24
print("You will end your study at:", end)

#1 String: Horizontal message to vertical message
string = "Don't chase money.\nChase Problems,\nThen solve it."
strList = string.split('\n')
length = 0

for word in strList:
    if len(word) > length:
        length = len(word)

for word in strList:
    if len(word) != length:
        strList[strList.index(word)] += " "*(length - len(word))

for i in range (length):
    for j in range(len(strList)):
        print(strList[j][i], end="")
    print()
