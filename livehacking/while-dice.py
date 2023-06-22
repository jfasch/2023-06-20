import random

max_tries = 9
num_tries = 0
while num_tries < max_tries:
    num_tries += 1
    eyes = random.randrange(1, 7)
    if eyes == 6:
        print('yay')
        break
else:
    print('lose')
