# 1535559

import re

# List of lucky combination number
LUCK_COMBINATION = [14,15,16,19,
                    22,23,24,26,28,29,
                    32,35,36,39,
                    41,42,44,45,46,49,
                    51,53,54,55,56,59,
                    61,62,63,64,65,66,69,
                    78,79,
                    82,87,89,
                    91,92,93,94,95,96,97,98,99]

FIGHT_COMBINATION = [33,47,74]

# Sum of all the number after the first 3 numbers 0xx - (1234567)
MOST_AUSPICIOUS_SUM = [1,3,5,11,13,15,16,21,23,24,29,31,33,39,
                41,47,48,52,61,63,67,68,81]

AUSPICIOUS_SUM = [6,7,8,17,18,25,32,35,37,45,73]

OK_SUM = [38,57,58,65]

# Getting the suggestion number based on their name
def get_num():

    name = input('\nEnter your name, best at length of seven(7): ')

    name = name.replace(' ', '')[-7:]
    print(f'The name taken to check: {name}\n')
    num = ''

    for c in name:
        cur = (ord(c) - 96) % 9
        if cur == 0:
            cur = 9
        num += str(cur)
    
    check_phone_number(num)

    if len(num) < 7:
        print('Suggesting some new number')
        tmpsum = sum([(int)(c) for c in num])
        n = 7 - len(num)
        for i in range(10**n):
            new = tmpsum + sum([(int)(a) for a in str(i)])
            if new in MOST_AUSPICIOUS_SUM:
                print(f'Lucky number: {i}')
                # TODO: Further insertion and checking
                print('[Possibilities of good number]:')

                # Inserting one by one
                for j in range(len(num)):
                    char = [c for c in num]
                    char.insert(j, str(i))
                    cur = ''.join(char)
                    check_phone_number(cur)


# Checking the number
def check_phone_number(num):

    num = re.sub(r'[^\w]', '', num)[-7:]
    print(f'The number taken to check: 0xx-{num}\n')

    luck_dict = {'Luck':0, 'Fight':0, 'Bad':0}

    for i in range(len(num)-1):

        tmp = (int) (str(num[i]) + str(num[i+1]))

        if tmp in LUCK_COMBINATION:
            print(f'{tmp}: LUCK +1')
            luck_dict['Luck'] += 1

        elif tmp in FIGHT_COMBINATION:
            print(f'{tmp}: FIGHT ~1')
            luck_dict['Fight'] += 1

        else:
            print(f'{tmp}: INAUSPICIOUS -1')
            luck_dict['Bad'] += 1

    # Printing the overall
    print()
    for k, v in luck_dict.items():
        print(f'{k} combination: {v}')

    # Checking sum
    tmpsum = sum([(int)(c) for c in num])
    print(f'\nSum of all 0xx-{num} = {tmpsum}')
    if tmpsum in MOST_AUSPICIOUS_SUM:
        print('Best Luck')
    elif tmpsum in AUSPICIOUS_SUM:
        print('Good Luck')
    elif tmpsum in OK_SUM:
        print('Ok Luck')
    else:
        print('No Luck')



while True:
    choice = input('''\n======================\nPhone Number Luck Detector v0.1
1. Get suggestion based on your name
2. Check your phone number
[Press other key to exit]
Choice: ''')

    try:
        if (int)(choice) == 1:
            get_num()
        elif (int)(choice) == 2:
            while True:
                user = input('Enter your phone number [Q to exit]: ')
                if user == 'Q':
                    break
                check_phone_number(user)
        else:
            print('App closed.')
            break
    except:
        print('App closed.')
        break
