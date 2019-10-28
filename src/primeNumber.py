import math


def is_prime(n: int):
    if n < 2:
        return False
    if n < 4:
        return True
    for x in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % x == 0:
            return False

    return True


print(is_prime(3))
print(is_prime(9))
print(is_prime(2969))
print(is_prime(2970))
