# Adding the current song to your playlist in a current INS key button

import time
import pyautogui
from pynput import keyboard

# NOTE: To my future me: Make sure to set your browser to 80% and in queue mode & F11 full screen mode
# Mine is in 1920 x 1080 pixel resolution, change accordingly

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
        pyautogui.rightClick(px, py)

        # 3 up -> right -> down
        pyautogui.press(['up', 'up', 'up', 'right', 'down'])
        pyautogui.press('enter')

        pyautogui.hotkey('win', 'ctrl', 'left')


cmd = input('[ENTER TO START]')

if cmd:
    print('Program started... \nINS: Add song\nPAUSE: End the program')
    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))
