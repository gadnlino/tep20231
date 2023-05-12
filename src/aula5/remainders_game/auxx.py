
import random

n = 1_000_000
k = 740891

ns = []

for __ in range(n):
    ns.append(str(random.randint(0, 1_000_000)))

print(f'{n} {k}')
print(' '.join(ns))