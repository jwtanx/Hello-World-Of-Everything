''' Upside down pyramid '''

def build(Floors):
    for i in range(Floors, 0, -1):
        for j in range(0, Floors-i):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()

build(5)    