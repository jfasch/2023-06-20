import time

def f():
    print('jetzt gleich 1')
    yield 1
    print('jetzt gleich 2')
    yield 2
    print('und aus')

numbers = f()

for elem in numbers:
    time.sleep(2)
    print('FOR')
    print(elem)
