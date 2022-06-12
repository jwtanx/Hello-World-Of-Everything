import pyperclip

str = input('Enter your words: ')

hex_ = str.encode("utf-8").hex().upper()

print('Full text')
print(hex_)

finalized = " ".join([hex_[i:i+2] for i in range(0, len(hex_), 2)])

print()
print(f'Copied: {finalized}')
pyperclip.copy(finalized)

# for i, h in enumerate(hex_):
#     if i != 0 and i % 2 == 0:
#         print(' ', end='')
#     print(h, end='')