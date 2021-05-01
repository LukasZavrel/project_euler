#%%
import numpy as np
max_prime = 10**4
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
for i in range(10**3,10**4-6660):
    j = i+3330
    k = i+6660
    if i in primes and j in primes and k in primes:
        if set(int(c) for c in str(i)) == set(int(c) for c in str(j)) == set(int(c) for c in str(k)):
            print(i)
result = 2969
print(f'{result}{result+3330}{result+6660}')