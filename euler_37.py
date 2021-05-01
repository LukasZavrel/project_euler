# %%
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


# %%
def truncatable_prime(nr):
    if nr < 10:
        return 0
    str_nr = str(nr)
    for i in range(1,len(str_nr)):
        if int(str_nr[i:]) not in primes or int(str_nr[:-i]) not in primes:
            return 0
    return 1


# %%
total_amount = 0
counter = 0
for prime in sorted(primes):
    if truncatable_prime(prime):
        total_amount += prime
        counter += 1
        print(prime)
    if counter == 11:
        break
#%%
print(total_amount)