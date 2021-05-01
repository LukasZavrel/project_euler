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
def distinct_divisors(num):
    if num in prime_numbers or num==1:
        return 1
    distinct = 0
    counter = 0
    while num > 1:
        curr_prime = primes[counter]
        exponent_counter = 0
        while not num % curr_prime:
            num = num // curr_prime
            exponent_counter += 1
        if exponent_counter:
            distinct += 1
        counter += 1
    return distinct


# %%
counter = 1
field = [False]*4
while counter<10**6:
    field = [*field[1:], distinct_divisors(counter) == len(field)]
    if all(field):
        print(counter-len(field)+1)
        break
    counter += 1

