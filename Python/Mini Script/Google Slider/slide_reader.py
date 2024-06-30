"""
This script will use Firefox screenshot feature to copy the slide pictures and
paste it into your slide. Please note that this only work for Windows at the
moment. Will do implementation for Mac in the future. Ubuntu is not supported.
"""
import os
import time
import logging
import pyautogui
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(os.path.basename(__file__))

# Coordinates of the top left corner of the slide: Set yourself
# To find your, screenshot your whole screen and open it in Paint
TOP_LEFT = (400, 280)
slides = int(input("Enter the number of slides you want to copy: "))
logger.info("Please make sure you have the slide open in Firefox")
logger.info("Make sure that the other Windows can be accessible by Alt + Tab")
ready = input("Press [Enter] to start then quickly switch to Firefox")
logger.info("Starting in 5 seconds...")
time.sleep(5)

# =========================================================================== #

for i in range(slides):
    # Move cursor to the top left of the slide
    pyautogui.moveTo(TOP_LEFT)

    # Hold shift and right click
    pyautogui.keyDown("shift")
    pyautogui.rightClick()

    # Press T to screen shot
    pyautogui.press("t")
    pyautogui.keyUp("shift")

    # Move cursor down by a pixel
    pyautogui.moveRel(0, 1 if i // 2 == 0 else -1)

    # Left click to copy
    pyautogui.click()

    # Copy it
    pyautogui.hotkey("ctrl", "c")

    # Open the slide by switching windows tab
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)

    # Add a slide if it is not the first slide
    if i != 0:
        pyautogui.hotkey("ctrl", "m")

    # Paste the slide
    pyautogui.hotkey("ctrl", "v")

    # Tab back
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)
    pyautogui.press("down")
