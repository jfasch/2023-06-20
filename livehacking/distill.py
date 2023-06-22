import sys

f = open(sys.argv[1])

for line in f:
    stripped_line = line.strip()
    if len(stripped_line) == 0:
        continue
    if stripped_line[0] == '#':
        continue
    print(line, end='')
