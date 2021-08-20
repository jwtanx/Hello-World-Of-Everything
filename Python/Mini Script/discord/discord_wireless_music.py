# https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function
# https://pypi.org/project/pynput/

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

if choice != 'Y':
    px, py = 585, 1020
    # px, py = 585, 520 # For testing, ctrl + n for a new page vscode
    skip = input('Skip command: ').lower()
    base = re.sub(r'[\w\s]', '', skip)
    if 'n' in skip:
        ap = True
        print('AUTOPLAY: ON')

print('Running... [Esc to stop]')

def clear():
    time.sleep(0.5)
    pyautogui.press('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)


# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        elif event.key == keyboard.Key.media_next:
            pyautogui.click(px, py)
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
        elif event.key == keyboard.Key.media_play_pause:
            # Write .np to get the song info
            pyautogui.write(base + 'np')
            pyautogui.press('enter')
            # clear()
            # pyautogui.write(base + 'leave')
            # pyautogui.press('enter')
            # clear()
            # pyautogui.click(357, 930)
            # pyautogui.press('esc')
            # quit()
        # else:
        #     print('Received event {}'.format(event))
