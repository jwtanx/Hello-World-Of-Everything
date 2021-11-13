str = input('Enter your words: ')

hex_ = str.encode("utf-8").hex().upper()

print('Full text')
print(hex_)

print()
print('Cleaned: ')

for i, h in enumerate(hex_):
    if i != 0 and i % 2 == 0:
        print(' ', end='')
    print(h, end='')
    