import random
import keyboard

primes = set(range(2,5001))
for n in range(2,5001):
    p = n
    while p<=5000:
        p += n
        primes.discard(p)
print(primes)