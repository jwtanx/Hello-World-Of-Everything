# First we need a file containing your query and duration

import re
import os
import time
import winsound
import pyautogui

# Import a text file path
# TODO: spotify/youtube playlist autoparser

cmd = input('Bot command? (e.g. -p): ')


def notify():
    for _ in range(3):
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)


def run():
    filepath = input('Input your file path: ').replace('"', '')

    with open(filepath, 'r') as f:
        content = f.read()

    q_ls = [q for q in content.split('\n') if q != '']
    print(f'{len(q_ls)} tracks queued.')

    try:
        possible_q = [q[q.index(') ')+2:] for q in q_ls]
    except:
        possible_q = q_ls

    return possible_q


def request(song):
    pyautogui.hotkey('win', 'ctrl', 'right')
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.write(cmd + ' ' + song, interval=0.05)
    pyautogui.press('enter')
    pyautogui.hotkey('win', 'ctrl', 'left')


if cmd:
    query = run()

    for i in range(3, 0, -1):
        print(f'Starting in {i}...')
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    os.system('cls')

    print('Running... [CTRL + C to stop]')

    for q in query:

        duration = q[q.index(':')-1:q.index(':')+3]
        minsec = time.strptime(duration, '%M:%S')

        title = str(q[:q.index(':')-3]).lower()
        cleaned = re.sub(r'[^\w\s]', '', title)
        print(f'Requesting for {title}')
        cleaned = cleaned.replace('  ', ' ')
        request(cleaned)

        time.sleep(minsec.tm_min*60 + minsec.tm_sec)

        notify()
