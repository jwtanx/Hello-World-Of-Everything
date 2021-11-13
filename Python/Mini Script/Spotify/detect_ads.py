import win32gui
from add_to_playlist import restart

# Check for the specific titles. works better than ctypes
def find_window(title):
    hwnd = win32gui.FindWindowEx(0, 0, 0, title)
    return hwnd  # returns 0 if nothing found


ad_titles = [
    # some ads set these titles
    r"Spotify Free",
    r"Advertisement",
]

while True:
    for title in ad_titles:
        if find_window(title):
            restart()
