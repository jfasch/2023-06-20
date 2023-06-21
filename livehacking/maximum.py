import sys

iterable = (int(elem) for elem in sys.argv[1:])

print(max(iterable))
