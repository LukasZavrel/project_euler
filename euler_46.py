#%%
import numpy as np
max_prime = 10**6
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
for i in range(1,10**6,2):
    if i not in primes:
        conjecture_holds = False
        for j in range(int(np.sqrt(i))):
            if i - 2 * j**2 in primes:
                conjecture_holds = True
                break
        if not conjecture_holds:
            print(i)
