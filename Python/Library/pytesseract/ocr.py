import cv2
import pytesseract
import pyperclip

img = cv2.imread(input("Filepath: ").replace("\\", "/"))

text = pytesseract.image_to_string(img)
print(text)

print("\n-------------------------------------------------\n")
print("Copied to clipboard")
pyperclip.copy(text)

print(input("ENTER TO EXIT..."))