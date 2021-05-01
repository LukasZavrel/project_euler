# %%
import numpy as np

prime_numbers = set([i for i in range(2, 2000000)])
current = 0
primes = []
while current < np.sqrt(2000000):
    current = min(prime_numbers)
    for i in range(current * current, 2000001, current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)

# %%
primes_under_1000 = set([i for i in primes if i < 1000 and i>64])


# %%
def prime_amount(a, b):
    n = 0
    while True:
        if n * n + a * n + b not in primes:
            return n
        else:
            n += 1


# %%
import math

max_primes = 0
size = 1000
for b in sorted(primes_under_1000):
    bound_1 = -math.floor(math.sqrt(4*b))
    if not (bound_1 % 2):
        bound_1 -= 1
    lower_bound = max(bound_1, -size)
    for a in range(lower_bound, size, 2):
        candidate = prime_amount(a, b)
        if candidate > max_primes:
            max_primes = candidate
            a_max, b_max = a, b
            print(a_max, b_max, max_primes)
