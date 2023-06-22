import sys

f = open(sys.argv[1])

def line_empty(l):
    stripped_line = l.strip()
    if len(stripped_line) == 0:
        return True
    if stripped_line[0] == '#':
        return True
    return False

for line in (line for line in f if not line_empty(line)):
    print(line, end='')
