import sys

print('alle', sys.argv)

for i in range(len(sys.argv)):
    print(i, sys.argv[i], 'type', type(sys.argv[i]))
