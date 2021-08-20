import pyautogui
import time
import random

sentence = ["ehhh?", "ok", "oic", "heh", "hmm", "hmmmmmm", "eyyy", "huh", "bruh",
            "i didnt know that", "you!", "ey bruh", "loll", "hehe", "anyway...", "pog", "meh"]

emoji = [":e", ":p", "=p", "0.0", "o.o", ":/", ":]", ":]]"]

count = 50


def clear():
    time.sleep(1)
    pyautogui.press('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)


while True and count:
    generated = ''
    if random.randint(0, 10) >= 7:
        generated += random.choice(sentence) + ' ' + random.choice(emoji)
    else:
        if random.randint(0, 10) <= 7:
            generated += random.choice(sentence)
        else:
            generated += random.choice(emoji)
    pyautogui.write(generated, interval=0.1)
    pyautogui.press('enter')
    count -= 1
    clear()
    time.sleep(random.randint(4, 8))
