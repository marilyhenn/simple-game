import random

a = {
    "player": 0,
    "bot": 0
}

def even(num: int):
    if num%2 == 0:
        return False
    else:
        return True
while True:
    b = random.randint(100, 1000)
    if even(b):
        continue
    c = random.randint(100, 1000)
    if even(c):
        continue
    d = random.randint(0, 1)

