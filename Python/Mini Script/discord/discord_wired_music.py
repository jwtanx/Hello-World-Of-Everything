from pynput import keyboard
import pyautogui
import time
import re

# Default skip location
px, py = 628, 945

choice = input('Hydra 1? (y/n): ').upper()
base = ''
skip = ''
ap = False


def clear():
    time.sleep(0.5)
    pyautogui.press('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)


if choice != 'Y':
    px, py = 585, 1020
    # px, py = 585, 520 # For testing, ctrl + n for a new page vscode
    skip = input('Skip command: ').lower()
    base = re.sub(r'[\w\s]', '', skip)
    if 'n' in skip:
        ap = True
        print('AUTOPLAY: ON')

print('Running... [Esc to stop]')


class MyException(Exception):
    pass


def on_press(key):
    if key == keyboard.Key.esc:
        quit()
    elif key == keyboard.Key.media_next:
        pyautogui.click(px, py)
        global ap
        if ap:
            clear()
            pyautogui.write(base + 'ap')
            pyautogui.press('enter')
            clear()
            ap = False
        if choice != 'Y':
            pyautogui.write(skip)
            pyautogui.press('enter')
            clear()
            # pyautogui.write('`testing ai sorry if it skips yours`')
            # pyautogui.press('enter')
    elif key == keyboard.Key.media_play_pause:
        clear()
        pyautogui.write(base + 'clear')
        pyautogui.press('enter')
        clear()
        pyautogui.click(357, 930)
        pyautogui.press('esc')
    # else:
    #     print('Received key {}'.format(key))


# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
