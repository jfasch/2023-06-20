import random

max_tries = 9
for _ in range(8):
    eyes = random.randrange(1, 7)
    if eyes == 6:
        print('yay')
        break
else:
    print('lose')
