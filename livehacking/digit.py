import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

try:
    digit = int(sys.argv[1])
except ValueError:
    print('geh bitte, das ist aber kein integer!')
    sys.exit(1)

try:
    translation = translation_table[digit]
except KeyError:
    print('geh bitte, das ist aber keine ziffer!')
    sys.exit(2)

print(translation)
