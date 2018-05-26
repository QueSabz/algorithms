import math


# Group 1

def f1(n):
    return n ** 0.999999 * math.log(n)


def f2(n):
    return 10000000 * n


def f3(n):
    return 1.000001 ** n


def f4(n):
    return n ** 2


bigNumber = 100000000
results = [("f1", f1(bigNumber)), ("f2", f2(bigNumber)), ("f3", f3(bigNumber)), ("f4", f4(bigNumber))]
results.sort(key=lambda tup: tup[1])
print(results)
