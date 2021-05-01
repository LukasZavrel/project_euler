#%%
import numpy as np

max_prime = 10 ** 6
prime_numbers = set([i for i in range(2, max_prime)])
current = 0
primes = []
while current < np.sqrt(max_prime):
    current = min(prime_numbers)
    for i in range(current * current, max_prime + 1, current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)

#%%
no_even_primes = set([2])
for prime in primes:
    something_even = False
    for number in str(prime):
        if int(number) % 2 == 0:
            something_even = True
    if not something_even:
        no_even_primes.add(prime)

#%%
def generate_rotations(nr):
    str_nr = str(nr)
    all_rotations = set([nr])
    for _ in range(len(str_nr)):
        str_nr = f'{str_nr[-1]}{str_nr[:-1]}'
        all_rotations.add(int(str_nr))
    return all_rotations

import itertools
def is_circular_prime(prime):
    if all([rotation in primes for rotation in generate_rotations(prime)]):
        print(prime)
        return 1
    return 0
#%%
total_sum = 0
for cand_prime in no_even_primes:
    total_sum += is_circular_prime(cand_prime)
#%%
print(total_sum)
