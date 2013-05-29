import math

def is_prime(n):
    sqrt = math.sqrt(n)
    for i in range(2, int(sqrt)):
        if i % n == 0:
            return False
    return True



nl = range(2, 10000)
pl = []

while nl:
    pn = nl.pop(0)

    nl = filter(lambda x: x%pn != 0, nl)

    pl.append(pn)


print pl


for i in pl:
    print i, is_prime(i)
