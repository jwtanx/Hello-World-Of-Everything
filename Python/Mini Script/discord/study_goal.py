# Automatically add goals and delete the goal

import time
import pyautogui
import winsound
from datetime import date

# DEFAULTS
HOURS = 2
WORDS = f'Work {date.today()}'

start = True if len(input('[Press ENTER to start]')) >= 0 else False
worked = 0


def clear():
    time.sleep(1)
    pyautogui.press('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)


def notify():
    for _ in range(3):
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)


def check_in():
    time.sleep(1)
    pyautogui.hotkey('win', 'ctrl', 'right')

    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.write(WORDS)
    pyautogui.press('enter')
    # clear()

    pyautogui.hotkey('win', 'ctrl', 'left')


if start:
    for i in range(3, 0, -1):
        print(f'Starting in {i}...')
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    print('Running... [CTRL + C to stop]')

    while True:
        # TODO: Sound effect before checking in [DONE]
        check_in()
        time.sleep(HOURS * 60 * 60)
        worked += HOURS
        print(f'{worked} hours used.')
        notify()
