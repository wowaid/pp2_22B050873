import math
a = [int(s) for s in input().split()]
def func(list):
    return math.prod(list)
print(func(a))