# Music skipping tool using page down key

# https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function
# https://pypi.org/project/pynput/

from pynput.keyboard import Key, Listener
import pyautogui
import time

# Default skip location
px, py = 485, 925

choice = input('Hydra 1? (y/n): ').upper()
skip = ''

if choice != 'Y':
    px, py = 585, 1020
    skip = input('Skip command: ').lower()

print('Running... [Pause to stop]')

def on_press(key):
    pass

def on_release(key):
    if key == Key.pause:
        # Stop listener
        return False
    elif key == Key.media_next:
        pyautogui.hotkey('win', 'ctrl', 'right')
        time.sleep(0.5)
        pyautogui.click(px, py)

        if choice != 'Y':
            pyautogui.write(skip)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('up')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('del')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.5)

        print("Skipped")
        pyautogui.hotkey('win', 'ctrl', 'left')

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
