# Ref: https://pyautogui.readthedocs.io/en/latest/keyboard.html
# Ref: https://pypi.org/project/PyAutoGUI/

import subprocess
import pyautogui
import time

team = [['AMJAD', 'MOHAMMED', 'ALI'],
        ['LEE', 'ONG', 'JOHN'],
        ['ELYNN', 'OOI', 'SEOW']]

# Getting the total participants
TOTAL = sum(len(row) for row in team)

# Delay
delaysecond = 3
for i in range(delaysecond, 0, -1):
    print(f'Start in {i}...')
    time.sleep(1)

# Duplicate the dummy cert according to the total
px, py = 155, 300
pyautogui.click(px, py)
pyautogui.hotkey('ctrl', 'c')

for i in range(TOTAL-1):
    pyautogui.hotkey('ctrl', 'v')

# Go back to the first slide
pyautogui.press('home')

counter = 0
NAME_X, NAME_Y = 1090, 550

for row in range(len(team)):
    for member in team[row]:
        print(f'Currently pasting {member}')

        # Pointing to the name position
        pyautogui.doubleClick(NAME_X, NAME_Y)

        # Copy the name
        subprocess.run("clip", universal_newlines=True, input=member)

        # Pasting the name
        pyautogui.hotkey('ctrl', 'v')
        counter += 1

        # Next slide
        pyautogui.press('pgdn')

        # Add some delay
        time.sleep(0.05)

assert counter == TOTAL

# data = "hello world"
# subprocess.run("clip", universal_newlines=True, input=data)
