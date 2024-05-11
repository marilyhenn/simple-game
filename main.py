import random

a = {
    "player": 0,
    "bot": 0
}


def even(num: int):
    if num % 2 == 0:
        return False
    else:
        return True


while True:
    first = random.randint(100, 1000)
    if even(first):
        continue
    second = random.randint(100, 1000)
    if even(second):
        continue
    plus_minus = random.randint(0, 1)
    if plus_minus == 1:
        result = first + second
        print(result)
    elif plus_minus == 0:
        result = first - second
        print(result)
