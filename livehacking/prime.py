import sys

number = int(sys.argv[1])

if number == 1:
    print('not prime')
    sys.exit(0)

if number <= 0:
    print('du dumpfbacke, die definitionsmenge sind die natuerlichen zahlen')
    sys.exit(1)

for divisor_candidate in range(2, number):
    if number % divisor_candidate == 0:
        print('not prime')
        break
else:
    print('prime')
