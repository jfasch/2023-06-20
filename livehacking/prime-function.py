import sys

def is_prime(n):
    if n == 1:
        return False
    
    for divisor_candidate in range(2, n):
        if n % divisor_candidate == 0:
            return False
    return True

number = int(sys.argv[1])

if number <= 0:
    print('du dumpfbacke, die definitionsmenge sind die natuerlichen zahlen')
    sys.exit(1)

if is_prime(number):
    print('prime')
else:
    print('not prime')

