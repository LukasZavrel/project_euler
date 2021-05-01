#%%
import numpy as np
max_prime = 10**5
prime_numbers = set([i for i in range(2, max_prime)])
current = 0
primes = []
while current<np.sqrt(max_prime):
    current = min(prime_numbers)
    for i in range(current*current,max_prime+1,current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)

#%%
import itertools
potential_primes = sorted(list(itertools.permutations(range(1,8))), reverse=True)
for pot in potential_primes:
    nr = int(''.join([str(i) for i in pot]))
    is_prime = True
    for prime in primes:
        if prime < nr:
            if nr % prime == 0:
                is_prime = False
                break
    if is_prime:
        print(nr)
