# Adding the current song to your playlist in a current INS key button

import time
import pyautogui
from pynput import keyboard
from os import system, name

# NOTE: To my future me: Make sure to set your browser to 80% and in queue mode & F11 full screen mode
# Mine is in 1920 x 1080 pixel resolution, change accordingly

action = ['up', 'up', 'up', 'right', 'down']

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Default skip location
px, py = 960, 200


class MyException(Exception):
    pass


def on_press(key):
    # https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
    if key == keyboard.Key.pause:
        quit()
    elif key == keyboard.Key.insert:
        # Make sure you put your spotify browser in the next Windows
        pyautogui.hotkey('win', 'ctrl', 'right')
        time.sleep(0.5)

        # Close the ads banner
        pyautogui.click(1405, 285)

        # Just in case there is duplication for the previous song
        pyautogui.press('esc')
        time.sleep(0.25)

        pyautogui.rightClick(px, py)

        # 3 up -> right -> down
        pyautogui.press(action)
        pyautogui.press('enter')

        pyautogui.hotkey('win', 'ctrl', 'left')


cmd = input('[APP (Y/N)?]: ')

if cmd.upper() == 'Y':
    action = ['up', 'up', 'right', 'down']
    
clear()
print('Program started... \nINS: Add song\nPAUSE: End the program')
# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
