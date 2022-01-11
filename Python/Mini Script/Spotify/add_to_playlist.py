# Adding the current song to your playlist in a current INS key button

import time
import win32gui
import pyautogui
from pynput import keyboard
from os import system, name

# NOTE: To my future me: Make sure to set your browser to 80% and in queue mode & F11 full screen mode
# Mine is in 1920 x 1080 pixel resolution, change accordingly

action = ['up', 'up', 'up', 'right', 'down']
use_app = False

# Default skip location
px, py = 960, 200

ad_titles = [
    # some ads set these titles
    r"Spotify Free",
    r"Advertisement",
]

class MyException(Exception):
    pass

# Check for the specific titles. works better than ctypes
def find_window(title):
    hwnd = win32gui.FindWindowEx(0, 0, 0, title)
    return hwnd  # returns 0 if nothing found


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Restart the app
def restart():
    # Shutting down the app
    pyautogui.hotkey('win', 'ctrl', 'right')
    pyautogui.hotkey('alt', 'f4')

    pyautogui.press('win')
    time.sleep(0.5)

    # Restarting the app
    pyautogui.write('spotify')
    pyautogui.press('enter')
    time.sleep(3)

    # Play the song
    pyautogui.press('space')

    # Click the queue
    pyautogui.click(1765, 1040)

    # Go back
    pyautogui.hotkey('win', 'ctrl', 'left')


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
    
    elif use_app and key == keyboard.Key.page_down:
        restart()


cmd = input('[APP (Y/N)?]: ')

if cmd.upper() == 'Y':
    use_app = True
    action = ['up', 'up', 'right', 'down']
    
clear()
print('Program started... \nINS: Add song\nPAUSE: End the program\nPAGE DOWN: Restart\n')

print('!!! MAKE SURE YOUR SPOTIFY APP IS ZOOMED OUT TWICE FROM THE DEFAULT ZOOM !!!')

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    # for title in ad_titles:
    #     if find_window(title):
    #         restart()
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
