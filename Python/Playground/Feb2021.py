# Last updated: Sat, February 06, 2021 - 16:20

quit()

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
