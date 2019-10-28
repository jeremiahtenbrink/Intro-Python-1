import math


def IsPrime(n: int):
    if n < 2: return False
    if n < 4: return True
    for x in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % x == 0:
            return False

    return True


print(IsPrime(3))
print(IsPrime(9))
print(IsPrime(2969))
print(IsPrime(2970))
